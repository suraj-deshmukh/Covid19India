# Covid19India
A Python Library to get India's Total Covid patients stats as well State wise stats


## Usage

### To get India's total count

	In [1]: from pprint import pprint                                                                                                                                                                           
	
	In [2]: from Covid19India import CovidIndia                                                                                                                                                                 
	
	In [3]: obj = CovidIndia()                                                                                                                                                                                  
	
	In [4]: total = obj.gettotal()                                                                                                                                                                              
	
	In [5]: pprint(total)                                                                                                                                                                                       
	{'active': 41472, 'confirmed': 62939, 'deaths': 2109, 'recovered': 19358}

### To get Indian States and UT wise data

	In [6]: state = obj.getstatetotal()                                                                                                                                                                         
	
	In [7]: pprint(state)                                                                                                                                                                                       
	{'Andaman and Nicobar Islands': {'active': 0,
									 'confirmed': 33,
									 'deaths': 0,
									 'recovered': 33},
	 'Andhra Pradesh': {'active': 999,
						'confirmed': 1930,
						'deaths': 44,
						'recovered': 887},
	 'Arunachal Pradesh': {'active': 0,
						   'confirmed': 1,
						   'deaths': 0,
						   'recovered': 1},
	 'Assam': {'active': 27, 'confirmed': 63, 'deaths': 2, 'recovered': 34},
	 'Bihar': {'active': 264, 'confirmed': 591, 'deaths': 5, 'recovered': 322},
	 'Chandigarh': {'active': 143, 'confirmed': 169, 'deaths': 2, 'recovered': 24},
	 'Chhattisgarh': {'active': 16, 'confirmed': 59, 'deaths': 0, 'recovered': 43},
	 'Dadar Nagar Haveli': {'active': 1,
							'confirmed': 1,
							'deaths': 0,
							'recovered': 0},
	 'Delhi': {'active': 4449, 'confirmed': 6542, 'deaths': 73, 'recovered': 2020},
	 'Goa': {'active': 0, 'confirmed': 7, 'deaths': 0, 'recovered': 7},
	 'Gujarat': {'active': 5233,
				 'confirmed': 7796,
				 'deaths': 472,
				 'recovered': 2091},
	 'Haryana': {'active': 376, 'confirmed': 675, 'deaths': 9, 'recovered': 290},
	 'Himachal Pradesh': {'active': 10,
						  'confirmed': 50,
						  'deaths': 2,
						  'recovered': 38},
	 'Jammu and Kashmir': {'active': 459,
						   'confirmed': 836,
						   'deaths': 9,
						   'recovered': 368},
	 'Jharkhand': {'active': 75, 'confirmed': 156, 'deaths': 3, 'recovered': 78},
	 'Karnataka': {'active': 378, 'confirmed': 794, 'deaths': 30, 'recovered': 386},
	 'Kerala': {'active': 16, 'confirmed': 505, 'deaths': 4, 'recovered': 485},
	 'Ladakh': {'active': 25, 'confirmed': 42, 'deaths': 0, 'recovered': 17},
	 'Madhya Pradesh': {'active': 1723,
						'confirmed': 3614,
						'deaths': 215,
						'recovered': 1676},
	 'Maharashtra': {'active': 15649,
					 'confirmed': 20228,
					 'deaths': 779,
					 'recovered': 3800},
	 'Manipur': {'active': 0, 'confirmed': 2, 'deaths': 0, 'recovered': 2},
	 'Meghalaya': {'active': 2, 'confirmed': 13, 'deaths': 1, 'recovered': 10},
	 'Mizoram': {'active': 0, 'confirmed': 1, 'deaths': 0, 'recovered': 1},
	 'Odisha': {'active': 229, 'confirmed': 294, 'deaths': 2, 'recovered': 63},
	 'Puducherry': {'active': 3, 'confirmed': 9, 'deaths': 0, 'recovered': 6},
	 'Punjab': {'active': 1574, 'confirmed': 1762, 'deaths': 31, 'recovered': 157},
	 'Rajasthan': {'active': 1576,
				   'confirmed': 3708,
				   'deaths': 106,
				   'recovered': 2026},
	 'Tamil Nadu': {'active': 4667,
					'confirmed': 6535,
					'deaths': 44,
					'recovered': 1824},
	 'Telengana': {'active': 383,
				   'confirmed': 1163,
				   'deaths': 30,
				   'recovered': 750},
	 'Tripura': {'active': 132, 'confirmed': 134, 'deaths': 0, 'recovered': 2},
	 'Uttar Pradesh': {'active': 1800,
					   'confirmed': 3373,
					   'deaths': 74,
					   'recovered': 1499},
	 'Uttarakhand': {'active': 20, 'confirmed': 67, 'deaths': 1, 'recovered': 46},
	 'West Bengal': {'active': 1243,
					 'confirmed': 1786,
					 'deaths': 171,
					 'recovered': 372}}

