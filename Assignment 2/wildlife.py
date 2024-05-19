import requests
from nominatim import get_coordinates_from_nominatim

def get_species_list(city_name):
    coords = get_coordinates_from_nominatim(city_name)
    if not coords:
        return None
    url = f"https://api.example.com/wildlife/species?lat={coords['lat']}&lon={coords['lon']}"
    response = requests.get(url)
    return response.json()

def display_species(species_list):
    for species in species_list:
        print(f"Species: {species['Species']['AcceptedCommonName']}, Status: {species['Species']['PestStatus']}")

def get_surveys_by_species(taxonid, city_name):
    coords = get_coordinates_from_nominatim(city_name)
    if not coords:
        return None
    url = f"https://api.example.com/wildlife/surveys?taxonid={taxonid}&lat={coords['lat']}&lon={coords['lon']}"
    response = requests.get(url)
    return response.json()

def display_sightings(sightings):
    for sighting in sightings:
        print(f"Sighting: {sighting['properties']['LocalityDetails']} on {sighting['properties']['StartDate']}")
