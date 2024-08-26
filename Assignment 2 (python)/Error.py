import tkinter as tk

class Error(Exception):
    def __init__(self, type, message):
        self.type = type
        self.message = message
    def display(self):

        label_font = ("Helvetica", 10, "bold")
        button_font = ("Arial Narrow", 11, "bold")
        label_colour = "#168FC1"

        error_window = tk.Toplevel()
        error_window.title("Error")

        icon = tk.PhotoImage(file = "Images/error_icon.png")
        error_window.iconphoto(False, icon)

        photo = tk.PhotoImage(file = "Images/error.png")
        photo_label = tk.Label(error_window, image = photo)
        photo_label.image = photo
        photo_label.pack()

        error_label_frame = tk.LabelFrame(error_window, width = 1650, height = 70)
        error_label_frame.pack_propagate(False)
        error_label_frame.pack()

        error_label = tk.Label(error_label_frame, text = "Error", font = label_font, fg = label_colour)
        error_label.pack(expand = True)

        error_type = tk.Label(error_window, text = self.type, font = label_font, fg = label_colour)
        error_type.pack()

        error_message = tk.Label(error_window, text = self.message, font = label_font, fg = "red")
        error_message.pack(expand = True)

        close_button = tk.Button(error_window, text = "Close", command = error_window.destroy, font = button_font,
                                  fg = "white", bg = label_colour, width = 160)
        close_button.pack(side = "bottom")
