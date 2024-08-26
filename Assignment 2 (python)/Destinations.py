from Destination import Destination
from Utils import Utils
from Error import Error

class Destinations:
    def __init__(self, agency):
        self.utils = Utils()
        self.agency = agency
        self.destinations = []
    
    def add_destination(self, destination: Destination, type):
        if self.has_destination(destination.name, destination.country):
            raise Error("ExistingItemException", "Destination already exists.")
        self.destinations.append(destination)
        if type != "trip":
            self.utils.add_flights_for_destination(destination, self.agency)
    
    def remove_destination(self, name, country):
        if self.has_destination(name, country) == False:
            raise Error("ItemNotFoundException", "Destination does not exist.")
        destination = self.get_destination(name, country)
        self.destinations.remove(destination)
    
    def has_destination(self, name, country):
        for d in self.destinations:
            if d.name == name and d.country == country:
                return True
        return False
    
    def get_destination(self, name, country):
        if self.has_destination(name, country) == False:
            #throw error
            pass
        for d in self.destinations:
            if d.name == name and d.country == country:
                return d
        return None
    
    def insert_dummy_data(self):
        self.destinations.append(Destination("Eiffel Tower", "France"))
        self.destinations.append(Destination("Opera House", "Australia"))
        self.destinations.append(Destination("Uluru", "Australia"))
        self.destinations.append(Destination("Machu Picchu", "Peru"))
        self.destinations.append(Destination("Great Pyramids", "Egypt"))
        self.destinations.append(Destination("Niagara Falls", "Canada"))
        for d in self.destinations:
            self.utils.add_flights_for_destination(d, self.agency)
    
    def get_filtered_destinations(self, country):
        filtered = []
        for d in self.destinations:
            if country.lower() in d.country.lower(): filtered.append(d)
        return filtered


    
    
