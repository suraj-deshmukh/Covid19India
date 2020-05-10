import requests
from bs4 import BeautifulSoup

class CovidIndia:
    ''' 
    The CovidIndia class to get Covid Patients Total Stats as well as Statewise Stats.
    
    '''
    def __init__(self, ):
        self.__base_url = 'https://www.mohfw.gov.in/'
        
    def getcontent(self, ):
        try:
            r = requests.get(self.__base_url)
            r.raise_for_status() # raise exception for non 200 status code
            return r.text
        except Exception as e:
            raise(e)
        
    def gettotal(self, ):
        """
        Return Dict containing India's covid stats
        
        obj = CovidIndia()
        obj.gettotal()
        
        Returns:
        dict{'active': int, 'recovered': int, 'deaths': int, 'confirmed': int}        
        """
        try:
            resp = self.getcontent()
            html = BeautifulSoup(resp, 'html.parser')
            stats = html.select_one('.site-stats-count') #css class selector
            ul = stats.select_one('ul')
            total = {}
            total['active'] = int(ul.select_one('.bg-blue').select_one('strong').text)
            total['recovered'] = int(ul.select_one('.bg-green').select_one('strong').text) + int(ul.select_one('.bg-orange').select_one('strong').text)
            total['deaths'] = int(ul.select_one('.bg-red').select_one('strong').text)
            total['confirmed'] = total['active'] + total['recovered'] + total['deaths']
            return total
        except Exception as e:
            return "Unable to Fetch Data", e

    def getstatetotal(self, ):
        """
        Return Dict containing Indian states wise covid stats
        
        obj = CovidIndia()
        obj.getstatetotal()
        
        Returns:
        dict{'State Name'}:{'active': int, 'recovered': int, 'deaths': int, 'confirmed': int}        
        """
        try:
            resp = self.getcontent()
            html = BeautifulSoup(resp, 'html.parser')
            table = html.select_one('.table-responsive')
            tdata = table.select_one('tbody')
            state = {}
            for i in tdata.find_all('tr'):
                td = i.find_all('td')
                if len(td) == 5:
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
            return state
        except Exception as e:
            return "Unable to Fetch Data", e
            
            
if __name__ == '__main__':
    obj = CovidIndia()
    total = obj.gettotal()
    state = obj.getstatetotal()
        
