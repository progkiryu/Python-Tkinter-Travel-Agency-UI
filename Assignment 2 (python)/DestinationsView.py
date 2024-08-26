import tkinter as tk
from Error import Error

class DestinationsView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label_font = ("Helvetica", 10, "bold")
        self.button_font = ("Arial Narrow", 11, "bold")
        self.label_colour = "#168FC1"
        self.photo = tk.PhotoImage(file = "Images/destination.png")

        self.parent = parent
        self.controller = None

        self.destination_list = tk.Listbox(self, width = 60)

        self.country_list = tk.Listbox(self, width = 60)

    def main_menu(self):
        username = self.parent.agency_model.loggedInUser.name

        photo_label = tk.Label(self, image = self.photo)
        photo_label.image = self.photo
        photo_label.pack()

        label_frame = tk.LabelFrame(self, width = 1650, height = 70)
        label_frame.pack_propagate(False)
        label_frame.pack()

        welcome_label = tk.Label(label_frame, text = f"Hi {username}, welcome to the Destinations section",
                                 font = self.label_font, fg = self.label_colour)
        welcome_label.pack(expand = True)

        buttons_frame = tk.Frame(self)
        buttons_frame.pack(side = "bottom")

        view_all_destinations_button = tk.Button(buttons_frame, text = "View All Destinations", command = lambda:self.view_destinations("all"),
                                                 font = self.button_font, fg = "white", bg = self.label_colour, width = 30)
        view_all_destinations_button.grid(row = 0, column = 0)

        view_by_country_button = tk.Button(buttons_frame, text = "View Filtered Destinations", command = lambda:self.view_destinations("filtered"),
                                           font = self.button_font, fg = "white", bg = self.label_colour, width = 30)
        view_by_country_button.grid(row = 0, column = 1)

        add_destination = tk.Button(buttons_frame, text = "Add Destination", command = lambda:self.modify_destination_menu("add", "normal"),
                                    font = self.button_font, fg = "white", bg = self.label_colour, width = 30)
        add_destination.grid(row = 0, column = 2)

        remove_destination = tk.Button(buttons_frame, text = "Remove Destination", command = lambda:self.modify_destination_menu("remove", "normal"),
                                       font = self.button_font, fg = "white", bg = self.label_colour, width = 30)
        remove_destination.grid(row = 0, column = 3)

        exit_button = tk.Button(buttons_frame, text = "Exit", command = self.quit_application,
                                font = self.button_font, fg = "white", bg = self.label_colour, width = 30)
        exit_button.grid(row = 0, column = 4)

    def view_destinations(self, type):
        self.view_destinations_window = tk.Toplevel(self.parent)

        photo_label = tk.Label(self.view_destinations_window, image = self.photo)
        photo_label.image = self.photo
        photo_label.pack()

        destinations_label_frame = tk.LabelFrame(self.view_destinations_window, width = 1650, height = 70)
        destinations_label_frame.pack_propagate(False)
        destinations_label_frame.pack()

        destinations_label = tk.Label(destinations_label_frame, font = self.label_font, fg = self.label_colour)

        if type == "filtered":
            self.view_destinations_window.title("Display Filtered Destinations")
            destinations_label.config(text = "Filtered Destinations")
            country_label = tk.Label(self.view_destinations_window, text = "Country",
                                     font = self.label_font, fg = self.label_colour)
            country_label.pack()
            self.country_search_entry = tk.Entry(self.view_destinations_window, width = 125)
            self.country_search_entry.pack()
            self.country_search_entry.bind("<KeyRelease>", self.filter)
        else:
            self.view_destinations_window.title("Display Destinations")
            destinations_label.config(text = "Destinations")
        
        destinations_label.pack(expand = True)

        list_scroll_bar_frame = tk.Frame(self.view_destinations_window)
        list_scroll_bar_frame.pack(pady = 10)

        listbox_frame = tk.Frame(list_scroll_bar_frame)
        listbox_frame.pack(side = "left")

        scroll_bar_frame = tk.Frame(list_scroll_bar_frame)
        scroll_bar_frame.pack(side = "left")
        scroll_bar = tk.Scrollbar(scroll_bar_frame, orient = "vertical")
        scroll_bar.pack()

        destination_name_label = tk.Label(listbox_frame, text = "Name",
                                               font = self.label_font, fg = self.label_colour)
        destination_name_label.grid(row = 0, column = 0)
        
        self.destination_list = tk.Listbox(listbox_frame, width = 100, yscrollcommand = scroll_bar.set)
        self.destination_list.grid(row = 1, column = 0)

        country_list_label = tk.Label(listbox_frame, text = "Country",
                                      font = self.label_font, fg = self.label_colour)
        country_list_label.grid(row = 0, column = 1)

        self.country_list = tk.Listbox(listbox_frame, width = 100, yscrollcommand = scroll_bar.set)
        self.country_list.grid(row = 1, column = 1)

        scroll_bar.config(command = self.multiple_scroll)

        self.controller.set_destinations(tk.END)

        close_button = tk.Button(self.view_destinations_window, text = "Close", width = 165, command = self.quit_view_destinations,
                                 font = self.button_font, fg = "white", bg = self.label_colour)
        close_button.pack(side = "bottom")


    def modify_destination_menu(self, type, version):
        self.modify_destination_window = tk.Toplevel(self.parent)

        photo_label = tk.Label(self.modify_destination_window, image = self.photo)
        photo_label.image = self.photo
        photo_label.pack()


        modify_label_frame = tk.LabelFrame(self.modify_destination_window, width = 1650, height = 70)
        modify_label_frame.pack_propagate(False)
        modify_label_frame.pack()

        modify_label = tk.Label(modify_label_frame, font = self.label_font, fg = self.label_colour)
        
        buttons_frame = tk.Frame(self.modify_destination_window)
        buttons_frame.pack(side = "bottom")

        self.modify_button = tk.Button(buttons_frame, state = "disabled", font = self.button_font, width = 80)
    
        if "add" in type:
            if "totrip" in type:
                self.modify_destination_window.title("Add Destination To Trip")
            else: self.modify_destination_window.title("Add Destination")
            modify_label.config(text = "Add a Destination")
            self.modify_button.config(text = "Add Destination", command = lambda:self.add_destination(version))
        elif "remove" in type:
            if "totrip" in type:
                self.modify_destination_window.title("Remove Destination From Trip")
            else: self.modify_destination_window.title("Remove Destination")
            modify_label.config(text = "Remove a Destination")
            self.modify_button.config(text = "Remove Destination", command = self.remove_destination)
        
        entries_frame = tk.Frame(self.modify_destination_window)
        entries_frame.pack()

        name_label = tk.Label(entries_frame, text = "Name:",
                              font = self.label_font, fg = self.label_colour)
        name_label.grid(row = 0, column = 0, pady = 10, padx = 20)

        self.name_entry = tk.Entry(entries_frame)
        self.name_entry.grid(row = 0, column = 1, pady = 10, padx = 20)
        self.name_entry.bind("<KeyRelease>", self.detect)

        country_label = tk.Label(entries_frame, text = "Country:",
                                 font = self.label_font, fg = self.label_colour)
        country_label.grid(row = 1, column = 0, pady = 10, padx = 20)

        self.country_entry = tk.Entry(entries_frame)
        self.country_entry.grid(row = 1, column = 1, pady = 10, padx = 20)
        self.country_entry.bind("<KeyRelease>", self.detect)

        modify_label.pack(expand = True)
        
        self.modify_button.grid(row = 0, column = 0)

        close_button = tk.Button(buttons_frame, text = "Close", command = self.modify_destination_window.destroy,
                                 font = self.button_font, fg = "white", bg = self.label_colour, width = 80)
        close_button.grid(row = 0, column = 1)


    def multiple_scroll(self, *args):
        self.destination_list.yview(*args)
        self.country_list.yview(*args)

    def filter(self, e):
        if self.controller != None:
            country = self.country_search_entry.get()
            self.destination_list.delete(0, tk.END)
            self.country_list.delete(0, tk.END)
            self.controller.filter_destinations(country, tk.END)

    def detect(self, e):
        name_input = self.name_entry.get()
        country_input = self.country_entry.get()

        if len(name_input) > 0 and len(country_input) > 0: self.modify_button.config(state = "active", activebackground = self.label_colour,
                                                        activeforeground = "white", bg = self.label_colour, fg = "white")
        else: self.modify_button.config(state = "disabled", disabledforeground = "black", bg = "white", fg = "black")

    def add_destination(self, version):
        if self.controller != None:
            try:
                self.controller.add_destination(self.name_entry.get(), self.country_entry.get(), version)
                self.controller.set_destinations(tk.END)
                self.modify_destination_window.destroy()
            except Error as e: e.display()
        

    def remove_destination(self):
        if self.controller != None:
            try:
                self.controller.remove_destination(self.name_entry.get(), self.country_entry.get())
                self.controller.set_destinations(tk.END)
                self.modify_destination_window.destroy()
            except Error as e: e.display()
    
    def set_controller(self, controller):
        self.controller = controller

    def quit_view_destinations(self):
        self.view_destinations_window.destroy()
        self.destination_list = tk.Listbox(width = 60)
        self.country_list = tk.Listbox(width = 60)

    def quit_application(self):
        self.parent.destroy()