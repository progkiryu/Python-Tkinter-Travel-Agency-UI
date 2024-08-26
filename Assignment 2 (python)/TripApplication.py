import tkinter as tk
from Trip import Trip
from TripView import TripView
from TripController import TripController
from FlightsController import FlightsController
from DestinationsController import DestinationsController

class TripApplication(tk.Toplevel):
    def __init__(self, agency):
        super().__init__()

        self.title("Book a Trip")

        icon = tk.PhotoImage(file = "Images/trip_icon.png")
        self.iconphoto(True, icon)

        self.agency_model = agency
        self.trip_model = Trip(self.agency_model)

        view = TripView(self)
        view.pack()

        controller = TripController(self.trip_model, view)
        flights_controller = FlightsController(self.trip_model, view.flights_window)
        destinations_controller = DestinationsController(self.trip_model, view.destinations_window)

        view.set_controller(controller, flights_controller, destinations_controller)
