import requests
from bs4 import BeautifulSoup

class CovidIndia:
    ''' 
    The CovidIndia class to get Covid Patients Total Stats as well as Statewise Stats.
    
    '''
    def __init__(self, ):
        self.__base_url = 'https://www.mohfw.gov.in/'
        self.__html = None
        
    def __getcontent(self, ):
        try:
            r = requests.get(self.__base_url)
            r.raise_for_status() # raise exception for non 200 status code
            return r.text
        except Exception as e:
            raise(e)
        
    def __gettotalstats(self, ):
        '''
        internal function to parse total data
        '''
        stats = self.__html.select_one('.site-stats-count') #css class selector
        ul = stats.select_one('ul')
        total = {}
        total['active'] = int(ul.select_one('.bg-blue').select_one('strong').text)
        total['recovered'] = int(ul.select_one('.bg-green').select_one('strong').text) + int(ul.select_one('.bg-orange').select_one('strong').text)
        total['deaths'] = int(ul.select_one('.bg-red').select_one('strong').text)
        total['confirmed'] = total['active'] + total['recovered'] + total['deaths']
        return total
    
    def __getstatesstat(self, ):
        '''
        internal function to parse state wise data
        '''
        table = self.__html.select_one('.table-responsive')
        tdata = table.select_one('tbody')
        state = {}
        for i in tdata.find_all('tr'):
            td = i.find_all('td')
            if len(td) == 5 and len(td[0]) > 0:
                try:
                    confirmed = int(td[2].text)
                    recovered = int(td[3].text)
                    deaths =  int(td[4].text)
                    active =  confirmed - recovered - deaths 
                    state[td[1].text] = {
                        'active': active,
                        'recovered': recovered,
                        'confirmed': confirmed,
                        'deaths': deaths,
                    }
                except Exception as e:
                    pass
        return state
    
    def __gettime(self, ):
        time = self.__html.select_one('.status-update')
        if time:
            time = time.text.replace("COVID-19 INDIA as on :", "").strip()
            return time
        return ""
        
    def getstats(self, ):
        """
        Return Dict containing India's covid stats
        
        obj = CovidIndia()
        obj.gettotal()
        
        Returns:
        dict{'active': int, 'recovered': int, 'deaths': int, 'confirmed': int}        
        """
        try:
            resp = self.__getcontent()
            self.__html = BeautifulSoup(resp, 'html.parser')
            total = self.__gettotalstats()
            state = self.__getstatesstat()
            time = self.__gettime()
            return {'states': state, 'total': total, 'time': time}
        except Exception as e:
            return "Unable to Fetch Data", e
    
    def gethistorical(self, ):
        try:
            r = requests.get("https://corona.lmao.ninja/v2/historical/india?lastdays=10000")
            r.raise_for_status() # raise exception for non 200 status code
            return r.json()['timeline']
        except Exception  as e:
            return "Unable to Fetch Data", e
        
# if __name__ == '__main__':
#     obj = CovidIndia()
#     print(obj.getstats())
