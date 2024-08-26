import tkinter as tk
from Error import Error
from FlightsApplication import FlightsApplication
from DestinationsApplication import DestinationsApplication
from TripApplication import TripApplication

class AgencyView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        #Save username for other classes
        self.username = None

        #Fonts and colours
        self.label_font = ("Helvetica", 10, "bold")
        self.button_font = ("Arial Narrow", 11, "bold")
        self.label_colour = "#168FC1"

        #Frame for 'Login' text
        login_text_frame = tk.LabelFrame(self, width = 400, height = 70)
        login_text_frame.pack_propagate(False)
        login_text_frame.pack()

        #Label for 'Login'
        login_label = tk.Label(login_text_frame, text = "Login",
                                    font = self.label_font, foreground = self.label_colour)
        login_label.pack(expand = True)


        #Frame for 'Username' & 'Password' and its respective text-boxes
        entry_frame = tk.Frame(self)
        entry_frame.pack()

        #Label for 'Username' & 'Password'
        self.username_label = tk.Label(entry_frame, text = "Username:",
                                       font = self.label_font, foreground = self.label_colour)
        self.username_label.grid(row = 0, column = 0, pady = 10)
        self.password_label = tk.Label(entry_frame, text = "Password:",
                                       font = self.label_font, foreground = self.label_colour)
        self.password_label.grid(row = 1, column = 0, pady = 10)

        #Text-boxes for 'Username' & 'Password'
        self.username_entry = tk.Entry(entry_frame)
        self.username_entry.grid(row = 0, column = 1, pady = 10)
        self.password_entry = tk.Entry(entry_frame, show = "*")
        self.password_entry.grid(row = 1, column = 1, pady = 10)

        #Frame for 'Login' & 'Exit' buttons
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(side = "bottom")

        #Buttons for 'Login' & 'Exit'
        login_button = tk.Button(buttons_frame, text = "Login", width = 20,
                                      fg = "white", bg = self.label_colour, font = self.button_font,
                                      command = self.check_administrator)
        login_button.grid(row = 0, column = 0)
        exit_button = tk.Button(buttons_frame, text = "Exit", width = 20,
                                     bg = self.label_colour, fg = "white", font = self.button_font,
                                     command = self.quit_application)
        exit_button.grid(row = 0, column = 1)

        self.controller = None

    def set_menu(self):
        menu_window = tk.Toplevel(self.parent)

        icon = tk.PhotoImage(file = "Images/agency_icon.png")
        menu_window.iconphoto(False, icon)

        photo = tk.PhotoImage(file = "Images/agency.png")
        image_label = tk.Label(menu_window, image = photo)
        image_label.image = photo
        image_label.pack()

        label_frame = tk.LabelFrame(menu_window, width = 1650, height = 70)
        label_frame.pack_propagate(False)
        label_frame.pack()

        welcome_message = tk.Label(label_frame, text = (f"Hi {self.username}, welcome to the Prog2 Travel Agency"),
                                   fg = self.label_colour, font = self.label_font)
        welcome_message.pack(expand = True)

        buttons_frame = tk.Frame(menu_window)
        buttons_frame.pack()

        flights_button = tk.Button(buttons_frame, text = "Explore Flights", font = self.button_font, command = self.activate_flights_menu,
                                   fg = "white", bg = self.label_colour, width = 45)
        flights_button.grid(row = 0, column = 0)

        destinations_button = tk.Button(buttons_frame, text = "Explore Destinations", font = self.button_font, command = self.activate_destinations_menu,
                                        fg = "white", bg = self.label_colour, width = 45)
        destinations_button.grid(row = 0, column = 1)

        trip_button = tk.Button(buttons_frame, text = "Book a Trip", font = self.button_font, command = self.activate_trips_menu,
                                fg = "white", bg = self.label_colour, width = 45)
        trip_button.grid(row = 0, column = 2)
        
        exit_button = tk.Button(buttons_frame, text = "Exit", command = menu_window.destroy, font = self.button_font,
                                fg = "white", bg = self.label_colour, width = 45)
        exit_button.grid(row = 0, column = 3)

    def activate_flights_menu(self):
        FlightsApplication(self.parent.model)
    
    def activate_destinations_menu(self):
        DestinationsApplication(self.parent.model)

    def activate_trips_menu(self):
        TripApplication(self.parent.model)

    def set_controller(self, controller):
        self.controller = controller

    def check_administrator(self) -> bool:
        if self.controller != None:
            try:
                if self.controller.check_administrator(self.username_entry.get(), self.password_entry.get()) == True:
                    self.set_menu()
            except Error as e: e.display()
    

    def quit_application(self):
        self.parent.destroy()