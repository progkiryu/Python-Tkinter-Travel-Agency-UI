from Destination import Destination
from Flight import Flight
from Error import Error


class TripController():
    def __init__(self, model, view):
        self.model = model
        self.flights = model.flights
        self.destinations = model.destinations
        self.view = view
    def add_connecting_flights(self):
        self.model.add_connecting_flights()
    def view_itinery(self, end):
        objects = self.model.get_itinery()
        for o in objects:
            self.view.trip_listbox.insert(end, o.to_string())
    def list_individually(self, array):
        objects = self.model.get_itinery()
        selected_objects = array
        result_list = []
        for o in objects:
            if o.to_string() in selected_objects: result_list.append(o)
        data_type = type(result_list[0])
        for o in result_list:
            if type(o) is not data_type: raise Error("InputMismatchException", "Cannot show both Flights and Destinations.")
        if data_type is Flight: 
            self.view.flights_window.view_all_flights_menu("all")
        elif data_type is Destination: 
            self.view.destinations_window.view_destinations("all")
