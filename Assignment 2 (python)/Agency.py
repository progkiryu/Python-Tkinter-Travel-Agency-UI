from Administrators import Administrators
from Administrator import Administrator
from Destinations import Destinations
from Flights import Flights

class Agency:
    def __init__(self):
        self.admins = Administrators()
        self.destinations = Destinations(self)
        self.flights = Flights(self)
        self.admins.insert_dummy_data()
        self.destinations.insert_dummy_data()
        self.loggedInUser = None
    
