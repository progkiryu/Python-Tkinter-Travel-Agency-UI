import random
from Destination import Destination
from Flight import Flight

class Utils:
    #Using @staticmethod did not work on my version of VSCode and I basically removed it and just imported this method.
    def add_flights_for_destination(self, destination:Destination, agency):
        country = destination.country
        airlines = ["American Airlines", "QANTAS", "JetStar", "Tiger Airways", "United Airlines", "Egypt Air", "Etihad", "Singapore Airlines", "British Air", "Cathay Dragon"]
        flight_min = 11
        flight_max = 999

        cost_min = 49.99
        cost_max = 999.99

        countries = []
        for d in agency.destinations.destinations:
            countries.append(d.country)
        
        for s in countries:
            try:
                agency.flights.add_flight(Flight(airlines[random.randint(0, (len(airlines) - 1))], random.randint(flight_min, flight_max), country, s, random.uniform(cost_min, cost_max)))
                agency.flights.add_flight(Flight(airlines[random.randint(0, (len(airlines) - 1))], random.randint(flight_min, flight_max), s, country, random.uniform(cost_min, cost_max)))
            except:
                continue
