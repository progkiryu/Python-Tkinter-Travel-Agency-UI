import tkinter as tk
from Error import Error

class FlightsView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label_font = ("Helvetica", 10, "bold")
        self.button_font = ("Arial Narrow", 11, "bold")
        self.label_colour = "#168FC1"
        
        self.photo = tk.PhotoImage(file = "Images/flight.png")

        self.parent = parent
        self.controller = None

        self.airlines_listbox = tk.Listbox(self, width = 20)
        self.flight_no_listbox = tk.Listbox(self, width = 20)
        self.takeoff_listbox = tk.Listbox(self, width = 20)
        self.landing_listbox = tk.Listbox(self, width = 20)
        self.cost_listbox = tk.Listbox(self, width = 20)
        
    def main_menu(self):
        username = self.parent.agency_model.loggedInUser.name

        photo_label = tk.Label(self, image = self.photo)
        photo_label.image = self.photo
        photo_label.pack()

        label_frame = tk.LabelFrame(self, width = 1650, height = 70)
        label_frame.pack_propagate(False)
        label_frame.pack()

        welcome_label = tk.Label(label_frame, text = f"Hi {username}, welcome to the Flights section",
                                 font = self.label_font, fg = self.label_colour)
        welcome_label.pack(expand = True)

        buttons_frame = tk.Frame(self)
        buttons_frame.pack(side = "bottom")

        view_all_flights_button = tk.Button(buttons_frame, text = "View All Flights", command = lambda:self.view_all_flights_menu("all"),
                                            font = self.button_font, fg = "white", bg = self.label_colour, width = 30)
        view_all_flights_button.grid(row = 0, column = 0)

        view_by_country_button = tk.Button(buttons_frame, text = "View Flights By Country", command = lambda:self.view_all_flights_menu("filtered"),
                                           font = self.button_font, fg = "white", bg = self.label_colour, width = 30)
        view_by_country_button.grid(row = 0, column = 1)

        add_flight_button = tk.Button(buttons_frame, text = "Add Flight", command = self.add_flight_menu,
                                      font = self.button_font, fg = "white", bg = self.label_colour, width = 30)
        add_flight_button.grid(row = 0, column = 2)

        remove_flight_button = tk.Button(buttons_frame, text = "Remove Flight", command = self.remove_flight_menu,
                                         font = self.button_font, fg = "white", bg = self.label_colour, width = 30)
        remove_flight_button.grid(row = 0, column = 3)

        close_button = tk.Button(buttons_frame, text = "Close", command = self.quit_application,
                                 font = self.button_font, fg = "white", bg = self.label_colour, width = 30)
        close_button.grid(row = 0, column = 4)
        
    def view_all_flights_menu(self, type:str):
        self.view_flights_window = tk.Toplevel(self.parent)

        photo_label = tk.Label(self.view_flights_window, image = self.photo)
        photo_label.image = self.photo
        photo_label.pack()

        label_frame = tk.LabelFrame(self.view_flights_window, width = 1650, height = 70)
        label_frame.pack_propagate(False)
        label_frame.pack()

        flights_label = tk.Label(label_frame, font = self.label_font, fg = self.label_colour)

        if type == "filtered":
            flights_label.config(text = "Filtered Flights")
            self.view_flights_window.title("Display Flights Filtered")
            country_label = tk.Label(self.view_flights_window, text = "Country",
                                     font = self.label_font, fg = self.label_colour)
            country_label.pack()

            self.country_entry = tk.Entry(self.view_flights_window, width = 125)
            self.country_entry.pack()

            self.country_entry.bind("<KeyRelease>", self.filter)
        else:
            flights_label.config(text = "Flights")
            self.view_flights_window.title("Display Flights")

        flights_label.pack(expand = True)

        list_scroll_bar_frame = tk.Frame(self.view_flights_window)
        list_scroll_bar_frame.pack(pady = 10)

        list_frame = tk.Frame(list_scroll_bar_frame)
        list_frame.pack(side = "left")

        scroll_bar_frame = tk.Frame(list_scroll_bar_frame)
        scroll_bar_frame.pack(side = "left")
        scroll_bar = tk.Scrollbar(scroll_bar_frame, orient = "vertical")
        scroll_bar.pack()
        
        airlines_label = tk.Label(list_frame, text = "Airline", font = self.label_font, fg = self.label_colour)
        airlines_label.grid(row = 0, column = 0)

        self.airlines_listbox = tk.Listbox(list_frame, width = 55, yscrollcommand = scroll_bar.set)
        self.airlines_listbox.grid(row = 1, column = 0)

        flight_no_label = tk.Label(list_frame, text = "Flight Number", font = self.label_font, fg = self.label_colour)
        flight_no_label.grid(row = 0, column = 1)

        self.flight_no_listbox = tk.Listbox(list_frame, width = 55, yscrollcommand = scroll_bar.set)
        self.flight_no_listbox.grid(row = 1, column = 1)

        takeoff_label = tk.Label(list_frame, text = "Takeoff Country", font = self.label_font, fg = self.label_colour)
        takeoff_label.grid(row = 0, column = 2)

        self.takeoff_listbox = tk.Listbox(list_frame, width = 55, yscrollcommand = scroll_bar.set)
        self.takeoff_listbox.grid(row = 1, column = 2)

        landing_label = tk.Label(list_frame, text = "Landing Country", font = self.label_font, fg = self.label_colour)
        landing_label.grid(row = 0, column = 3)

        self.landing_listbox = tk.Listbox(list_frame, width = 55, yscrollcommand = scroll_bar.set)
        self.landing_listbox.grid(row = 1, column = 3)

        cost_label = tk.Label(list_frame, text = "Cost", font = self.label_font, fg = self.label_colour)
        cost_label.grid(row = 0, column = 4)

        self.cost_listbox = tk.Listbox(list_frame, width = 55, yscrollcommand = scroll_bar.set)
        self.cost_listbox.grid(row = 1, column = 4)

        scroll_bar.config(command = self.multiple_scroll)

        self.controller.set_flights(tk.END)

        close_button = tk.Button(self.view_flights_window, text = "Close", width = 165, command = self.quit_view_flights,
                                 font = self.button_font, fg = "white", bg = self.label_colour)
        close_button.pack(side = "bottom")

    def add_flight_menu(self):
        self.add_flight_window = tk.Toplevel(self.parent)
        self.add_flight_window.title("Add Flight")

        photo_label = tk.Label(self.add_flight_window, image = self.photo)
        photo_label.image = self.photo
        photo_label.pack()
        

        add_flight_label_frame = tk.LabelFrame(self.add_flight_window, width = 1650, height = 70)
        add_flight_label_frame.pack_propagate(False)
        add_flight_label_frame.pack()

        add_flight_label = tk.Label(add_flight_label_frame, text = "Add a Flight",
                                    font = self.label_font, fg = self.label_colour)
        add_flight_label.pack(expand = True)

        entries_frame = tk.Frame(self.add_flight_window)
        entries_frame.pack()

        airline_label = tk.Label(entries_frame, text = "Airline:", 
                                 font = self.label_font, fg = self.label_colour)
        airline_label.grid(row = 0, column = 0, pady = 10)

        flight_no_label = tk.Label(entries_frame, text = "Flight Number:",
                                   font = self.label_font, fg = self.label_colour)
        flight_no_label.grid(row = 1, column = 0, pady = 10)

        takeoff_label = tk.Label(entries_frame, text = "Takeoff:",
                                 font = self.label_font, fg = self.label_colour)
        takeoff_label.grid(row = 2, column = 0, pady = 10)

        landing_label = tk.Label(entries_frame, text = "Landing:",
                                 font = self.label_font, fg = self.label_colour)
        landing_label.grid(row = 3, column = 0, pady = 10)
        
        cost_label = tk.Label(entries_frame, text = "Cost:",
                              font = self.label_font, fg = self.label_colour)
        cost_label.grid(row = 4, column = 0, pady = 10)


        self.airlines_entry = tk.Entry(entries_frame)
        self.airlines_entry.grid(row = 0, column = 1, pady = 10)
        self.airlines_entry.bind("<KeyRelease>", self.add_detect)

        self.flight_no_entry = tk.Entry(entries_frame)
        self.flight_no_entry.grid(row = 1, column = 1, pady = 10)
        self.flight_no_entry.bind("<KeyRelease>", self.add_detect)

        self.takeoff_entry = tk.Entry(entries_frame)
        self.takeoff_entry.grid(row = 2, column = 1, pady = 10)
        self.takeoff_entry.bind("<KeyRelease>", self.add_detect)

        self.landing_entry = tk.Entry(entries_frame)
        self.landing_entry.grid(row = 3, column = 1, pady = 10)
        self.landing_entry.bind("<KeyRelease>", self.add_detect)

        self.cost_entry = tk.Entry(entries_frame)
        self.cost_entry.grid(row = 4, column = 1, pady = 10)
        self.cost_entry.bind("<KeyRelease>", self.add_detect)

        buttons_frame = tk.Frame(self.add_flight_window)
        buttons_frame.pack(side = "bottom")

        self.add_flight_button = tk.Button(buttons_frame, text = "Add Flight", font = self.button_font, width = 80,
                                           command = self.add_flight, state = "disabled")
        self.add_flight_button.grid(row = 0, column = 0)

        close_button = tk.Button(buttons_frame, text = "Close", command = self.add_flight_window.destroy, width = 80,
                                 font = self.button_font, fg = "white", bg = self.label_colour)
        close_button.grid(row = 0, column = 1)

    def remove_flight_menu(self):
        self.remove_flight_window = tk.Toplevel(self.parent)
        self.remove_flight_window.title("Remove Flight")

        photo_label = tk.Label(self.remove_flight_window, image = self.photo)
        photo_label.image = self.photo
        photo_label.pack()

        remove_flight_label_frame = tk.LabelFrame(self.remove_flight_window, width = 1650, height = 70)
        remove_flight_label_frame.pack_propagate(False)
        remove_flight_label_frame.pack()

        remove_flight_label = tk.Label(remove_flight_label_frame, text = "Remove a Flight", font = self.label_font,
                                       fg = self.label_colour)
        remove_flight_label.pack(expand = True)

        entries_frame = tk.Frame(self.remove_flight_window)
        entries_frame.pack()

        takeoff_label = tk.Label(entries_frame, text = "Takeoff:", font = self.label_font,
                                 fg = self.label_colour)
        takeoff_label.grid(row = 0, column = 0, pady = 10)

        self.country_1_entry = tk.Entry(entries_frame)
        self.country_1_entry.grid(row = 0, column = 1, pady = 10)
        self.country_1_entry.bind("<KeyRelease>", self.remove_detect)

        landing_label = tk.Label(entries_frame, text = "Landing:", font = self.label_font,
                                 fg = self.label_colour)
        landing_label.grid(row = 1, column = 0, pady = 10)

        self.country_2_entry = tk.Entry(entries_frame)
        self.country_2_entry.grid(row = 1, column = 1, pady = 10)
        self.country_2_entry.bind("<KeyRelease>", self.remove_detect)

        buttons_frame = tk.Frame(self.remove_flight_window)
        buttons_frame.pack()

        self.remove_flight_button = tk.Button(buttons_frame, text = "Remove Flight", font = self.button_font,
                                              command = self.remove_flight, state = "disabled", width = 80)
        self.remove_flight_button.grid(row = 0, column = 0)

        close_button = tk.Button(buttons_frame, text = "Close", command = self.remove_flight_window.destroy,
                                 font = self.button_font, fg = "white", bg = self.label_colour, width = 80)
        close_button.grid(row = 0, column = 1)

    def multiple_scroll(self, *args):
        self.airlines_listbox.yview(*args)
        self.flight_no_listbox.yview(*args)
        self.takeoff_listbox.yview(*args)
        self.landing_listbox.yview(*args)
        self.cost_listbox.yview(*args)

    def filter(self, e):
        if self.controller != None:
            input = self.country_entry.get()
            self.airlines_listbox.delete(0, tk.END)
            self.flight_no_listbox.delete(0, tk.END)
            self.takeoff_listbox.delete(0, tk.END)
            self.landing_listbox.delete(0, tk.END)
            self.cost_listbox.delete(0, tk.END)
            self.controller.filtered(input, tk.END)
    
    def add_detect(self, e):
        airlines_input = self.airlines_entry.get()
        flight_no_input = self.flight_no_entry.get()
        takeoff_input = self.takeoff_entry.get()
        landing_input = self.landing_entry.get()
        cost_input = self.cost_entry.get()

        if (len(airlines_input) > 0 and len(flight_no_input) > 0 and len(takeoff_input) > 0 and len(landing_input) > 0 and len(cost_input) > 0):
            self.add_flight_button.config(state = "active", activeforeground = "white", activebackground = self.label_colour,
                                          bg = self.label_colour, fg = "white")
        else:
            self.add_flight_button.config(state = "disabled", disabledforeground = "black", bg = "white", fg = "white")
    
    def add_flight(self):
        if self.controller != None:
            try:
                self.controller.add_flight(self.airlines_entry.get(), self.takeoff_entry.get(), self.landing_entry.get())
                self.controller.set_flights(tk.END)
                self.add_flight_window.destroy()
            except Error as e: e.display()
            
    def remove_detect(self, e):
        takeoff_input = self.country_1_entry.get()
        landing_input = self.country_2_entry.get()

        if (len(takeoff_input) > 0 and len(landing_input) > 0):
            self.remove_flight_button.config(state = "active", activeforeground = "white", activebackground = self.label_colour,
                                             bg = self.label_colour, fg ="white")
        else:
            self.remove_flight_button.config(state = "disabled", disabledforeground = "black", bg = "white", fg = "white")

    def remove_flight(self):
        if self.controller != None:
            try:
                self.controller.remove_flight(self.country_1_entry.get(), self.country_2_entry.get())
                self.controller.set_flights(tk.END)
                self.remove_flight_window.destroy()
            except Error as e: e.display()

    def quit_view_flights(self):
        self.view_flights_window.destroy()
        self.airlines_listbox = tk.Listbox(width = 20)
        self.flight_no_listbox = tk.Listbox(width = 20)
        self.takeoff_listbox = tk.Listbox(width = 20)
        self.landing_listbox = tk.Listbox(width = 20)
        self.cost_listbox = tk.Listbox(width = 20)

    def set_controller(self, controller):
        self.controller = controller

    def quit_application(self):
        self.parent.destroy()

