from menu import display_menu
from wildlife import get_species_list, display_species, get_surveys_by_species, display_sightings
from utilities import filter_venomous, sort_sightings_by_date

def main():
    display_menu()
    while True:
        command = input("wildlife> ").strip().lower()
        if command == "help":
            display_menu()
        elif command == "exit":
            break
        elif command.startswith("species "):
            parts = command.split()
            city = parts[1]
            if len(parts) == 3 and parts[2] == "venomous":
                species_list = get_species_list(city)
                if species_list:
                    venomous_species = filter_venomous(species_list)
                    display_species(venomous_species)
                else:
                    print(f"No species found for city: {city}")
            else:
                species_list = get_species_list(city)
                if species_list:
                    display_species(species_list)
                else:
                    print(f"No species found for city: {city}")
        elif command.startswith("sightings "):
            parts = command.split()
            if len(parts) == 3:
                city = parts[1]
                taxonid = parts[2]
                surveys = get_surveys_by_species(taxonid, city)
                if surveys:
                    sorted_surveys = sort_sightings_by_date(surveys)
                    display_sightings(sorted_surveys)
                else:
                    print(f"Could not fetch surveys for taxonid {taxonid} in {city}")
            else:
                print("Invalid command format for sightings. Use: sightings <city> <taxonid>")
        else:
            print("Invalid command. Type 'help' for the list of commands.")

if __name__ == "__main__":
    main()
