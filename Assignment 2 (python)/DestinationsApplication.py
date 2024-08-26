import tkinter as tk
from Agency import Agency
from DestinationsController import DestinationsController
from DestinationsView import DestinationsView

class DestinationsApplication(tk.Toplevel):
    def __init__(self, agency:Agency):
        super().__init__()

        self.title("Explore Destinations")

        icon = tk.PhotoImage(file = "Images/destinations_icon.png")
        self.iconphoto(True, icon)

        self.agency_model = agency

        view = DestinationsView(self)
        view.main_menu()
        view.pack()

        controller = DestinationsController(self.agency_model, view)

        view.set_controller(controller)