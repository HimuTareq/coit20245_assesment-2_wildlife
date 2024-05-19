def filter_venomous(species_list):
    return [species for species in species_list if species['Species']['PestStatus'] == 'Venomous']

def sort_sightings_by_date(sightings):
    return sorted(sightings, key=lambda x: x["properties"]["StartDate"])
