from Flights import Flights
from Destinations import Destinations
from Error import Error

class Trip:
    def __init__(self, agency):
        self.agency = agency
        self.flights = Flights(self)
        self.destinations = Destinations(self)
    
    def add_connecting_flights(self):
        if len(self.destinations.destinations) <= 1:
            raise Error("InsufficientLengthException", "Need at least 2 destinations.")
        self.flights.flights.clear()
        current_destination = None
        next_destination = None
        for i in range(len(self.destinations.destinations)):
            current_destination = self.destinations.destinations[i]
            if i == (len(self.destinations.destinations) - 1):
                return
            next_destination = self.destinations.destinations[i + 1]
            if current_destination == next_destination or current_destination.country == next_destination.country:
                raise Error("ExistingItemException", "Destination already exists.")
            for f in self.agency.flights.flights:
                if f.takeoff == current_destination.country and f.landing == next_destination.country:
                    self.flights.add_flight(f)
                    break
    
    def get_itinery(self):
        objects = []
        for i in range(len(self.destinations.destinations)):
            objects.append(self.destinations.destinations[i])
            if i < len(self.flights.flights):
                objects.append(self.flights.flights[i])
        return objects
    
    