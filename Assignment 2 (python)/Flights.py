from Flight import Flight
from Error import Error

class Flights:
    def __init__(self, agency):
        self.agency = agency
        self.flights = []
    
    def add_flight(self, flight):
        if self.has_flight(flight.takeoff, flight.landing):
            raise Error("ExistingItemException", "Flight exists.")
        self.flights.append(flight)
    
    def remove_flight(self, takeoff, landing):
        if self.has_flight(takeoff, landing) == False:
            raise Error("ItemNotFoundException", "Flight does not exist.")
        flight = self.get_flight(takeoff, landing)
        self.flights.remove(flight)
    
    def has_flight(self, takeoff, landing):
        for f in self.flights:
            if f.takeoff == takeoff and f.landing == landing:
                return True
        return False
    
    def get_flight(self, takeoff, landing):
        for f in self.flights:
            if f.takeoff == takeoff and f.landing == landing:
                return f
        return None
    
    def get_filtered_flights(self, country):
        filtered = []
        for f in self.flights:
            if country.lower() in f.takeoff.lower() or country.lower() in f.landing.lower():
                filtered.append(f)
        return filtered
    
    def get_total_cost(self):
        cost = 0.0
        for f in self.flights:
            cost = cost + f.cost
        return cost