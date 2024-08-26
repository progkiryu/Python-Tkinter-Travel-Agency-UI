import tkinter as tk
from Agency import Agency
from FlightsView import FlightsView
from FlightsController import FlightsController

class FlightsApplication(tk.Toplevel):
    def __init__(self, agency:Agency):
        super().__init__()

        self.title("Explore Flights")

        icon = tk.PhotoImage(file = "Images/flights_icon.png")
        self.iconphoto(True, icon)

        self.agency_model = agency
        
        view = FlightsView(self)
        view.main_menu()
        view.pack()

        controller = FlightsController(self.agency_model, view)

        view.set_controller(controller)

