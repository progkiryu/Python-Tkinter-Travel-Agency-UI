import tkinter as tk
from AgencyView import AgencyView
from AgencyController import AgencyController
from Agency import Agency

class AgencyApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Prog2 Travel Agency")

        icon = tk.PhotoImage(file = "Images/agency_icon.png")
        self.iconphoto(False, icon)

        self.model = Agency()
        view = AgencyView(self)
        view.pack_propagate(True)
        view.pack()

        controller = AgencyController(self.model, view)

        view.set_controller(controller)

if __name__ == "__main__":
    agency_app = AgencyApplication()  
    agency_app.mainloop()

