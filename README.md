# Covid19India
A Python Library to get India's Total Covid patients stats as well State wise stats


## Usage

### To get India's total count

	In [1]: obj = CovidIndia()                                                                                                                                                                                  

	In [2]: total = obj.gettotal()                                                                                                                                                                              

	In [3]: total                                                                                                                                                                                               
	Out[3]: {'active': 41472, 'recovered': 19358, 'deaths': 2109, 'confirmed': 62939}

### To get Indian States and UT wise data

	In [4]: state = obj.getstatetotal()                                                                                                                                                                         

	In [5]: state                                                                                                                                                                                               
	Out[5]: 
	{'Andaman and Nicobar Islands': {'active': 0,
	  'recovered': 33,
	  'confirmed': 33,
	  'deaths': 0},
	 'Andhra Pradesh': {'active': 999,
	  'recovered': 887,
	  'confirmed': 1930,
	  'deaths': 44},
	 'Arunachal Pradesh': {'active': 0,
	  'recovered': 1,
	  'confirmed': 1,
	  'deaths': 0},
	 'Assam': {'active': 27, 'recovered': 34, 'confirmed': 63, 'deaths': 2},
	 'Bihar': {'active': 264, 'recovered': 322, 'confirmed': 591, 'deaths': 5},
	 'Chandigarh': {'active': 143, 'recovered': 24, 'confirmed': 169, 'deaths': 2},
	 'Chhattisgarh': {'active': 16, 'recovered': 43, 'confirmed': 59, 'deaths': 0},
	 'Dadar Nagar Haveli': {'active': 1,
	  'recovered': 0,
	  'confirmed': 1,
	  'deaths': 0},
	 'Delhi': {'active': 4449, 'recovered': 2020, 'confirmed': 6542, 'deaths': 73},
	 'Goa': {'active': 0, 'recovered': 7, 'confirmed': 7, 'deaths': 0},
	 'Gujarat': {'active': 5233,
	  'recovered': 2091,
	  'confirmed': 7796,
	  'deaths': 472},
	 'Haryana': {'active': 376, 'recovered': 290, 'confirmed': 675, 'deaths': 9},
	 'Himachal Pradesh': {'active': 10,
	  'recovered': 38,
	  'confirmed': 50,
	  'deaths': 2},
	 'Jammu and Kashmir': {'active': 459,
	  'recovered': 368,
	  'confirmed': 836,
	  'deaths': 9},
	 'Jharkhand': {'active': 75, 'recovered': 78, 'confirmed': 156, 'deaths': 3},
	 'Karnataka': {'active': 378,
	  'recovered': 386,
	  'confirmed': 794,
	  'deaths': 30},
	 'Kerala': {'active': 16, 'recovered': 485, 'confirmed': 505, 'deaths': 4},
	 'Ladakh': {'active': 25, 'recovered': 17, 'confirmed': 42, 'deaths': 0},
	 'Madhya Pradesh': {'active': 1723,
	  'recovered': 1676,
	  'confirmed': 3614,
	  'deaths': 215},
	 'Maharashtra': {'active': 15649,
	  'recovered': 3800,
	  'confirmed': 20228,
	  'deaths': 779},
	 'Manipur': {'active': 0, 'recovered': 2, 'confirmed': 2, 'deaths': 0},
	 'Meghalaya': {'active': 2, 'recovered': 10, 'confirmed': 13, 'deaths': 1},
	 'Mizoram': {'active': 0, 'recovered': 1, 'confirmed': 1, 'deaths': 0},
	 'Odisha': {'active': 229, 'recovered': 63, 'confirmed': 294, 'deaths': 2},
	 'Puducherry': {'active': 3, 'recovered': 6, 'confirmed': 9, 'deaths': 0},
	 'Punjab': {'active': 1574, 'recovered': 157, 'confirmed': 1762, 'deaths': 31},
	 'Rajasthan': {'active': 1576,
	  'recovered': 2026,
	  'confirmed': 3708,
	  'deaths': 106},
	 'Tamil Nadu': {'active': 4667,
	  'recovered': 1824,
	  'confirmed': 6535,
	  'deaths': 44},
	 'Telengana': {'active': 383,
	  'recovered': 750,
	  'confirmed': 1163,
	  'deaths': 30},
	 'Tripura': {'active': 132, 'recovered': 2, 'confirmed': 134, 'deaths': 0},
	 'Uttarakhand': {'active': 20, 'recovered': 46, 'confirmed': 67, 'deaths': 1},
	 'Uttar Pradesh': {'active': 1800,
	  'recovered': 1499,
	  'confirmed': 3373,
	  'deaths': 74},
	 'West Bengal': {'active': 1243,
	  'recovered': 372,
	  'confirmed': 1786,
	  'deaths': 171}}
