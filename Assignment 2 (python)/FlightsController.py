from Error import Error
from Flight import Flight

class FlightsController():
    def __init__(self, model, view):
        self.model = model
        self.view = view
    def set_flights(self, end):
        self.view.airlines_listbox.delete(0, end)
        self.view.flight_no_listbox.delete(0, end)
        self.view.takeoff_listbox.delete(0, end)
        self.view.landing_listbox.delete(0, end)
        self.view.cost_listbox.delete(0, end)
        flights = self.model.flights.flights
        for f in flights:
            self.view.airlines_listbox.insert(end, f.airline)
            self.view.flight_no_listbox.insert(end, str(f.flight_no))
            self.view.takeoff_listbox.insert(end, f.takeoff)
            self.view.landing_listbox.insert(end, f.landing)
            self.view.cost_listbox.insert(end, "{:.2f}".format(float(f.cost)))
    def filtered(self, country, end):
        self.view.airlines_listbox.delete(0, end)
        self.view.flight_no_listbox.delete(0, end)
        self.view.takeoff_listbox.delete(0, end)
        self.view.landing_listbox.delete(0, end)
        self.view.cost_listbox.delete(0, end)
        filtered_flights = self.model.flights.get_filtered_flights(country)
        for f in filtered_flights:
            self.view.airlines_listbox.insert(end , f.airline)
            self.view.flight_no_listbox.insert(end, str(f.flight_no))
            self.view.takeoff_listbox.insert(end, f.takeoff)
            self.view.landing_listbox.insert(end, f.landing)
            self.view.cost_listbox.insert(end, "{:.2f}".format(float(f.cost)))
    def add_flight(self, airline, takeoff, landing):
        try:
            flight_no = int(self.view.flight_no_entry.get())
            cost = float(self.view.cost_entry.get())
        except ValueError as e: raise Error("NumberFormatException", "Enter a number.")
        self.model.flights.add_flight(Flight(airline, flight_no, takeoff, landing, cost))
    def remove_flight(self, takeoff, landing):
        self.model.flights.remove_flight(takeoff, landing)
            
