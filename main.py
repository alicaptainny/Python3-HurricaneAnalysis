# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# 1
def update_damages(damages):
    updated_damages = []
    for damage in damages:
        if damage == "Damages not recorded":
            updated_damages.append(damage)
        else:
            if damage.endswith('B'):
                damage_value = float(damage[:-1]) * 1e9
            elif damage.endswith('M'):
                damage_value = float(damage[:-1]) * 1e6
            updated_damages.append(damage_value)
    return updated_damages

# Test the function
damages = ["Damages not recorded", '100M', 'Damages not recorded', '40M', '27.9M']
updated_damages = update_damages(damages)
print(updated_damages)
# 2
def construct_hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricanes_dict = {}
    for i in range(len(names)):
        hurricane_data = {
            'Name': names[i],
            'Month': months[i],
            'Year': years[i],
            'Max Sustained Wind': max_sustained_winds[i],
            'Areas Affected': areas_affected[i],
            'Damage': damages[i],
            'Deaths': deaths[i]
        }
        hurricanes_dict[names[i]] = hurricane_data
    return hurricanes_dict

# Test the function
names = ["Cuba I", "San Felipe II Okeechobee", "Bahamas"]
months = ["October", "September", "September"]
years = [1924, 1928, 1932]
max_sustained_winds = [165, 160, 160]
areas_affected = [["Central America", "Mexico"], ["Florida", "The Bahamas"], ["The Bahamas", "Northeastern United States"]]
damages = ["Damages not recorded", '100M', 'Damages not recorded']
deaths = [90, 4000, 16]

hurricanes_dict = construct_hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
print(hurricanes_dict)

# 3
def organize_hurricanes_by_year(hurricanes_dict):
    hurricanes_by_year = {}
    for hurricane_data in hurricanes_dict.values():
        year = hurricane_data['Year']
        if year not in hurricanes_by_year:
            hurricanes_by_year[year] = []
        hurricanes_by_year[year].append(hurricane_data)
    return hurricanes_by_year

# Test the function
hurricanes_by_year = organize_hurricanes_by_year(hurricanes_dict)
print(hurricanes_by_year)
# 4
def count_affected_areas(hurricanes_dict):
    affected_areas_count = {}
    for hurricane_data in hurricanes_dict.values():
        areas_affected = hurricane_data['Areas Affected']
        for area in areas_affected:
            if area not in affected_areas_count:
                affected_areas_count[area] = 0
            affected_areas_count[area] += 1
    return affected_areas_count

# Test the function
affected_areas_count = count_affected_areas(hurricanes_dict)
print(affected_areas_count)
# 5
def most_affected_area(affected_areas_count):
    max_affected_area = max(affected_areas_count, key=affected_areas_count.get)
    max_occurrences = affected_areas_count[max_affected_area]
    return max_affected_area, max_occurrences

# Test the function
most_affected, occurrences = most_affected_area(affected_areas_count)
print("Most affected area:", most_affected)
print("Number of occurrences:", occurrences)
# 6
def deadliest_hurricane(hurricanes_dict):
    max_deaths_hurricane = max(hurricanes_dict.values(), key=lambda x: x['Deaths'])
    max_deaths = max_deaths_hurricane['Deaths']
    hurricane_name = max_deaths_hurricane['Name']
    return hurricane_name, max_deaths

# Test the function
deadliest_name, max_deaths = deadliest_hurricane(hurricanes_dict)
print("Deadliest hurricane:", deadliest_name)
print("Number of deaths:", max_deaths)
# 7
def rate_hurricanes_mortality(hurricanes_dict):
    mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
    hurricanes_by_mortality = {rating: [] for rating in mortality_scale}

    for hurricane_data in hurricanes_dict.values():
        deaths = hurricane_data['Deaths']
        for rating, upper_bound in mortality_scale.items():
            if deaths <= upper_bound:
                hurricanes_by_mortality[rating].append(hurricane_data)
                break

    return hurricanes_by_mortality


# Test the function
hurricanes_by_mortality = rate_hurricanes_mortality(hurricanes_dict)
for rating, hurricanes in hurricanes_by_mortality.items():
    print(f"Rating {rating}: {len(hurricanes)} hurricanes")
# 8
def most_damaging_hurricane(hurricanes_dict):
    max_damage_hurricane = max(hurricanes_dict.values(), key=lambda x: x['Damage'] if isinstance(x['Damage'], float) else 0)
    max_damage = max_damage_hurricane['Damage']
    hurricane_name = max_damage_hurricane['Name']
    return hurricane_name, max_damage

# Test the function
most_damaging_name, max_damage = most_damaging_hurricane(hurricanes_dict)
print("Most damaging hurricane:", most_damaging_name)
print("Damage caused:", max_damage)

# 9
def rate_hurricanes_by_damage(hurricanes_dict):
    damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
    rated_hurricanes = {rating: [] for rating in damage_scale}

    for hurricane_data in hurricanes_dict.values():
        damage = hurricane_data['Damage']
        if damage == "Damages not recorded":
            rating = 0
        else:
            for rating, upper_bound in damage_scale.items():
                if isinstance(damage, float) and damage <= upper_bound:
                    break
            else:
                rating = max(damage_scale)
        rated_hurricanes[rating].append(hurricane_data)

    return rated_hurricanes


# Test the function
rated_hurricanes_by_damage = rate_hurricanes_by_damage(hurricanes_dict)
print(rated_hurricanes_by_damage)





