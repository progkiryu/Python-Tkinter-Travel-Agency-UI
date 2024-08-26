import tkinter as tk
from FlightsView import FlightsView
from DestinationsView import DestinationsView
from Error import Error

class TripView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.flights_window = FlightsView(self)
        self.destinations_window = DestinationsView(self)

        self.photo = tk.PhotoImage(file = "Images/trip.png")

        photo_label = tk.Label(self, image = self.photo)
        photo_label.image = self.photo
        photo_label.pack()

        self.parent = parent
        username = self.parent.trip_model.agency.loggedInUser.name

        self.label_font = ("Helvetica", 10, "bold")
        self.button_font = ("Arial Narrow", 11, "bold")
        self.label_colour = "#168FC1"

        label_frame = tk.LabelFrame(self, width = 1650, height = 70)
        label_frame.pack_propagate(False)
        label_frame.pack()

        welcome_label = tk.Label(label_frame, text = f"Hi {username}, welcome to the Trip section",
                                 font = self.label_font, fg = self.label_colour)
        welcome_label.pack(expand = True)

        buttons_frame = tk.Frame(self)
        buttons_frame.pack(side = "bottom")

        add_destination_button = tk.Button(buttons_frame, text = "Add Destination", command = lambda:self.destinations_window.modify_destination_menu("addtotrip", "trip"),
                                           font = self.button_font, fg = "white", bg = self.label_colour, width = 30)
        add_destination_button.grid(row = 0, column = 0)

        remove_destination_button = tk.Button(buttons_frame, text = "Remove Destination", command = lambda:self.destinations_window.modify_destination_menu("removetotrip", "normal"),
                                              font = self.button_font, fg = "white", bg = self.label_colour, width = 30)
        remove_destination_button.grid(row = 0, column = 1)

        add_connecting_flights_button = tk.Button(buttons_frame, text = "Add Connecting Flights", command = self.add_connecting_flights,
                                                  font = self.button_font, fg = "white", bg = self.label_colour, width = 30)
        add_connecting_flights_button.grid(row = 0, column = 2)

        view_trip_button = tk.Button(buttons_frame, text = "View Trip", command = self.view_trip_menu,
                                     font = self.button_font, fg = "white", bg = self.label_colour, width = 30)
        view_trip_button.grid(row = 0, column = 3)

        close_button = tk.Button(buttons_frame, text = "Close", command = self.quit_application,
                                 font = self.button_font, fg = "white", bg = self.label_colour, width = 30)
        close_button.grid(row = 0, column = 4)
    
        self.controller = None
    def add_connecting_flights(self):
        if self.controller != None:
            try:
                self.controller.add_connecting_flights()
            except Error as e: e.display()

    def view_trip_menu(self):
        view_trip_window = tk.Toplevel(self.parent)

        photo_label = tk.Label(view_trip_window, image = self.photo)
        photo_label.image = self.photo
        photo_label.pack()

        view_trip_window.title("Display Trip")

        view_trip_label_frame = tk.LabelFrame(view_trip_window, width = 1650, height = 70)
        view_trip_label_frame.pack_propagate(False)
        view_trip_label_frame.pack()

        view_trip_label = tk.Label(view_trip_label_frame, text = "Your Trip",
                                   font = self.label_font, fg = self.label_colour)
        view_trip_label.pack(expand = True)

        listbox_scrollbar_frame = tk.Frame(view_trip_window)
        listbox_scrollbar_frame.pack()

        self.trip_listbox = tk.Listbox(listbox_scrollbar_frame, width = 200, selectmode = "multiple")
        self.trip_listbox.pack(side = "left")

        if (len(self.parent.trip_model.get_itinery()) == 0):
            self.trip_listbox.config(justify = "center")
            self.trip_listbox.insert(tk.END, "Nothing yet.")

        trip_scrollbar = tk.Scrollbar(listbox_scrollbar_frame, orient = "vertical")
        trip_scrollbar.pack(side = "left")

        self.trip_listbox.config(yscrollcommand = trip_scrollbar.set)
        trip_scrollbar.config(command = self.trip_listbox.yview)

        buttons_frame = tk.Frame(view_trip_window)
        buttons_frame.pack(side = "bottom")

        list_individually_button = tk.Button(buttons_frame, text = "View Individual", command = self.list_individually,
                                             font = self.button_font, fg = "white", bg = self.label_colour, width = 80)
        list_individually_button.grid(row = 0, column = 0)

        close_button = tk.Button(buttons_frame, text = "Close", command = view_trip_window.destroy,
                                 font = self.button_font, fg = "white", bg = self.label_colour, width = 80)
        close_button.grid(row = 0, column = 1)

        self.controller.view_itinery(tk.END)
    def list_individually(self):
        selected_tuples = self.trip_listbox.curselection()
        selected_objects = [self.trip_listbox.get(tup) for tup in selected_tuples]
        if self.controller != None and len(selected_objects) > 0:
            try:
                self.controller.list_individually(selected_objects)
            except Error as e: e.display()
            

    def set_controller(self, controller, flights_controller, destinations_controller):
        self.controller = controller
        self.flights_window.set_controller(flights_controller)
        self.destinations_window.set_controller(destinations_controller)
    def quit_application(self):
        self.parent.destroy()