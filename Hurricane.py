# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damage(value):
    if value == "Damages not recorded":
        return "Damages not recorded"
    elif value[-1] == "B":
        return float(value[:-1]) * 1000000000
    else:
        return float(value[:-1]) * 1000000

new_damages = [update_damage(value) for value in damages]
# print(new_damages)
# END TEST

# write your construct hurricane dictionary function here:
def hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, new_damages, deaths):
  hurricane_comp = {}
  for i in range(len(names)):
    inner_dict = {"Name": names[i], "Month": months[i], "Year": years[i], "Max sustained wind": max_sustained_winds[i], "Areas affected": areas_affected[i], "Damage": new_damages[i], "Deaths": deaths[i]}
    hurricane_comp[names[i]] = inner_dict

  return hurricane_comp    
  
hurricane_database=hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, new_damages, deaths)

# print(hurricane_database)
# END TEST

# write your construct hurricane by year dictionary function here:
def unique_value(list_with_rep): # helper to create a list without repetitions
  uni_value = []
  for value in list_with_rep:
    if value not in uni_value:
      uni_value.append(value)
  return uni_value


def hurricane_by_year(years):
  uni_years = unique_value(years)
  
  hurricane_year = {}
  for year in uni_years:
    cane_year = []
    for hurricane in hurricane_database:
      if year == hurricane_database[hurricane]["Year"]:
        cane_year.append(hurricane_database[hurricane])
    hurricane_year[year] = cane_year

  return hurricane_year

# test_year=hurricane_by_year(years)
# print(test_year[2005])
# END TEST

# write your count affected areas function here:
def hurricane_for_area(areas_affected):
  unify_list = []
  for element in areas_affected:
    unify_list += element
  
  single_list = unique_value(unify_list)
  hurricane_area = {}
  for value in single_list:
    hurricane_area[value] = unify_list.count(value)
  return hurricane_area

test_areas_affected = hurricane_for_area(areas_affected)
# print(test_areas_affected)
# END TEST

# write your find most affected area function here:
def find_most_affected(test_areas_affected):
  area_hits = 0
  area_affected = ""
  for area in test_areas_affected:
    if test_areas_affected[area] > area_hits:
      area_hits = test_areas_affected[area]
      area_affected = area
  return ("The most affected area is " + area_affected + " hit " + str(area_hits) + " times.")       

# print(find_most_affected(test_areas_affected))
# END TEST

# write your greatest number of deaths function here:
def hurricane_biggest_deaths(hurricane_database):
  name = ""
  deaths = 0
  for element in hurricane_database:
    if hurricane_database[element]["Deaths"] > deaths:
      deaths = hurricane_database[element]["Deaths"]
      name = element
  return "The hurricane that caused the greatest number of deaths is " + name + ", it caused " + str(deaths) + " deaths."

# print(hurricane_biggest_deaths(hurricane_database))      
# END TEST

# write your catgeorize by mortality function here:
mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
def mortality_rating(hurricane_database):
  for element in hurricane_database:
    if hurricane_database[element]["Deaths"] == 0:
      hurricane_database[element]["Mortality rating"] = 0
    elif hurricane_database[element]["Deaths"] < 100 and hurricane_database[element]["Deaths"] > 0:
      hurricane_database[element]["Mortality rating"] = 1
    elif hurricane_database[element]["Deaths"] < 500 and hurricane_database[element]["Deaths"] > 100:
      hurricane_database[element]["Mortality rating"] = 2
    elif hurricane_database[element]["Deaths"] < 1000 and hurricane_database[element]["Deaths"] > 500:
      hurricane_database[element]["Mortality rating"] = 3
    elif hurricane_database[element]["Deaths"] < 10000 and hurricane_database[element]["Deaths"] > 1000:
      hurricane_database[element]["Mortality rating"] = 4
    else:
      hurricane_database[element]["Mortality rating"] = 5
  
  mortality_dict = {key: [] for key in range(6)}
  for element in hurricane_database:
    if hurricane_database[element]["Mortality rating"] == 0:
      mortality_dict[0].append(hurricane_database[element])
    elif hurricane_database[element]["Mortality rating"] == 1:
      mortality_dict[1].append(hurricane_database[element])
    elif hurricane_database[element]["Mortality rating"] == 2:
      mortality_dict[2].append(hurricane_database[element])
    elif hurricane_database[element]["Mortality rating"] == 3:
      mortality_dict[3].append(hurricane_database[element])
    elif hurricane_database[element]["Mortality rating"] == 4:
      mortality_dict[4].append(hurricane_database[element])
    else:
      mortality_dict[5].append(hurricane_database[element])
  
  return mortality_dict

# mort_dict = mortality_rating(hurricane_database)
# print(mort_dict[5])
# END TEST

# write your greatest damage function here:
def hurricane_biggest_damages(hurricane_database):
  name = ""
  damage = 0
  for element in hurricane_database:
    if hurricane_database[element]["Damage"] == 'Damages not recorded':
      pass    
    elif hurricane_database[element]["Damage"] > damage:
      damage = hurricane_database[element]["Damage"]
      name = element
  return "The hurricane that caused the greatest damage is " + name + ", it caused " + str(damage) + " dollars of damages."

# print(hurricane_biggest_damages(hurricane_database))      
# END TEST

# write your catgeorize by damage function here:
def damage_rating(hurricane_database):
  for element in hurricane_database:
    if hurricane_database[element]["Damage"] == 0 or hurricane_database[element]["Damage"] == "Damages not recorded" :
      hurricane_database[element]["Damage rating"] = 0
    elif hurricane_database[element]["Damage"] < 100000000 and hurricane_database[element]["Damage"] > 0:
      hurricane_database[element]["Damage rating"] = 1
    elif hurricane_database[element]["Damage"] < 1000000000 and hurricane_database[element]["Damage"] > 100000000:
      hurricane_database[element]["Damage rating"] = 2
    elif hurricane_database[element]["Damage"] < 10000000000 and hurricane_database[element]["Damage"] > 1000000000:
      hurricane_database[element]["Damage rating"] = 3
    elif hurricane_database[element]["Damage"] < 50000000000 and hurricane_database[element]["Damage"] > 10000000000:
      hurricane_database[element]["Damage rating"] = 4
    else:
      hurricane_database[element]["Damage rating"] = 5
  
  damage_dict = {key: [] for key in range(6)}
  for element in hurricane_database:
    if hurricane_database[element]["Damage rating"] == 0:
      damage_dict[0].append(hurricane_database[element])
    elif hurricane_database[element]["Damage rating"] == 1:
      damage_dict[1].append(hurricane_database[element])
    elif hurricane_database[element]["Damage rating"] == 2:
      damage_dict[2].append(hurricane_database[element])
    elif hurricane_database[element]["Damage rating"] == 3:
      damage_dict[3].append(hurricane_database[element])
    elif hurricane_database[element]["Damage rating"] == 4:
      damage_dict[4].append(hurricane_database[element])
    else:
      damage_dict[5].append(hurricane_database[element])
  
  return damage_dict

# damage_dict = damage_rating(hurricane_database)
# print(damage_dict[1])
# END TEST




