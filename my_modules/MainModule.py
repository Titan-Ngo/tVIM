"""This module provides the main functionality for the program and its GUI.

Note, the capitalization of the class defintion and title of this program are 
based on a play off of "gVIM".
"""

# Import Tkinter objects (GIU package)
import tkinter as tk
import tkinter.scrolledtext as scroll 
from tkinter import messagebox
from tkinter import filedialog 
from tkinter import *

# Import our modules
from my_modules.ParseCommands import * # Provides main functionality of our program
from my_modules.StringConstants import * # Defines string constants 


class tVIM():
    """The tVIM class defines a window in which the text editting is done. 
    Essentially, each instance of tVIM is an instance of the program itself.
    
    Instance vars
    -------------
    root: The Tkinter instance (the text editting window)
    scroll_window: The main Tkinter Text object in which the user writes in.
                   The user can scroll in this text box.
    cmd_line: The Tkinter Text object in which the user calls commands in.
    
    font: The font of chars in scroll_window.
    font_size: The size of chars in scroll_window.
    font_type: Specifies whether chars in scroll_window are bold/italic.
    """
    
    def __init__(self, contents=None):
        """Initializes a tVIM instance using the inputted parameter, if any.
        
        Parameters
        ----------
        self: tVIM instance.
        contents: a str that fills the tVIM window, defaults to None.
        """
        
        # Initializes the default font, font size, and font type
        self.font = "Courier"
        self.font_size = 10
        self.font_type = ""
        
        # Sets up the main window and adjusts its size
        self.root = tk.Tk(className="tVIM")
        self.root.resizable(False, False)
        self.root.geometry("780x460") # widthxheight
        # The main window has 1 column and 2 rows, 
        # the upper row for scroll_window and bottom for cmd_line
        self.root.rowconfigure(2)
        self.root.columnconfigure(1)  

        # Sets up scroll_window
        self.scroll_window = scroll.ScrolledText(self.root, width=95, height=23)
        self.scroll_window.bind("<Key>", self.scroll_window_events)
        self.scroll_window.grid(sticky=W)
        self.scroll_window.config(font=(self.font, self.font_size, self.font_type))
        # Sets up highlighting in the scroll_window
        self.scroll_window.tag_configure("highlight", background="yellow")
        self.scroll_window.tag_configure("search", background="blue")

        # Insert the contents str param into scroll_window
        if contents != None:
            self.scroll_window.insert('1.0', contents)   
        
        # Set up the frame to maintain the size of cmd_line
        cmd_frame = tk.Frame(self.root, width=50, height=3)
        cmd_frame.grid(row=1, column=0, sticky=S)
        # Set up cmd_line
        self.cmd_line = Text(cmd_frame, width=50, height=1)
        self.cmd_line.bind("<Key>", self.cmd_line_events)
        self.cmd_line.grid(sticky=S)

        # Creates the menu at the top of tVIM's window
        create_menu(self)

        # Runs the program loop
        self.root.mainloop()
        
    def save_file(self, filename):
        """Saves this file as a specified filename.
        
        Parameters
        ----------
        self: tVIM instance.
        filename: a str that is the name of the file.
        """
        
        # Get the contents currently in this window
        contents = self.scroll_window.get('1.0', END)
        
        # Write the contents into the file with filename
        filename.write(contents)
        filename.close()
        
    def scroll_window_events(tVIM, event):
        """Takes in all keyboard events while inside scroll_window.
        
        Parameters
        ----------
        self: tVIM instance.
        event: A keyboard event.
        """
    
        # Move cursor to cmd_line if esc 
        if event.char == '\x1b':
            tVIM.cmd_line.focus()

    def cmd_line_events(tVIM, event):
        """Takes in all keyboard events while inside cmd_line.
        
        Parameters
        ----------
        self: tVIM instance.
        event: A keyboard event.
        """
    
        # Move cursor back to scroll_window if enter
        parse_command(tVIM, event)



"""The code below sets up the dropdown menus at the top of the window.

The code in create_menu(), open_button(), save_button(), exit_button(),
and about_button() is inspired by, but not directly taken from, code from the 
following site: https://knowpapa.com/text-editor/
"""


def create_menu(tVIM):
    """Builds the GUI for the menu bar at the top of the tVIM window.
        
    Parameter
    ---------
    tVIM: tVIM instance.
    """

    # Creates the general menu bar for the tVIM's root window
    menu = Menu(tVIM.root)
    tVIM.root.config(menu=menu)
    
    # Creates the 'File' dropdown menu
    file_menu = Menu(menu)
    menu.add_cascade(label="File", menu=file_menu) 
    file_menu.add_command(label="New Window", command=lambda: tVIM())
    file_menu.add_command(label="Open", command=open_button)
    file_menu.add_command(label="Save", command=lambda: save_button(tVIM))
    file_menu.add_command(label="Exit", command=lambda: exit_button(tVIM))

    # Creates the 'Help' dropdown menu
    help_menu = Menu(menu)
    menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=about_button)
    help_menu.add_command(label="Commands", command=command_button)
    
    # Creates the 'Themes' dropdown menu
    themes_menu = Menu(menu)
    menu.add_cascade(label="Themes", menu=themes_menu)
    themes_menu.add_command(label="Normal", command=lambda: normal_button(tVIM))
    themes_menu.add_command(label="Dark Mode", command=lambda: dark_button(tVIM))
    themes_menu.add_command(label="Gray", command=lambda: gray_button(tVIM))
    themes_menu.add_command(label="Sky", command=lambda: day_button(tVIM))
    themes_menu.add_command(label="Evening", command=lambda: evening_button(tVIM))
    themes_menu.add_command(label="Beach", command=lambda: beach_button(tVIM))
    themes_menu.add_command(label="UCSD", command=lambda: UCSD_button(tVIM))
    themes_menu.add_command(label="McDonald's", command=lambda: mcdonalds_button(tVIM))
    
    # Creates the 'Fonts' dropdown menu
    fonts_menu = Menu(menu)
    menu.add_cascade(label="Fonts", menu=fonts_menu)
    fonts_menu.add_command(label="Courier", command=lambda: courier_button(tVIM))
    fonts_menu.add_command(label="Times", command=lambda: times_button(tVIM))
    fonts_menu.add_command(label="Helvetica", command=lambda: helv_button(tVIM))
    fonts_menu.add_command(label="Comic Sans", command=lambda: comicsans_button(tVIM))
    fonts_menu.add_command(label="????", command=lambda: mystery_button(tVIM))
    fonts_menu.add_separator()
    fonts_menu.add_command(label="Bold", command=lambda: bold_button(tVIM))
    fonts_menu.add_command(label="Italic", command=lambda: italic_button(tVIM))
    fonts_menu.add_command(label="Bold Italic", command=lambda: both_button(tVIM))
    fonts_menu.add_command(label="None", command=lambda: none_button(tVIM))


# The functions below provide functionality to menu items under 'File' and 'Help'


def open_button():
    """Opens a file that the user specifies into a new tVIM instance."""
    
    filename = filedialog.askopenfilename()

    if filename != None:
        file = open(filename, "rt")
        contents = file.read()
        # Load the contents from the chosen file into a new window
        tVIM(contents)
        file.close()
        
        
def save_button(tVIM):
    """Saves the text inside of this tVIM's scroll_window into a specified filename.
        
    Parameter
    ---------
    tVIM: tVIM instance.
    """
    
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    
    if filename != None:
        tVIM.save_file(filename)
        
        
def exit_button(tVIM):
    """Prompts the user to exit the tVIM instance without saving.
        
    Parameter
    ---------
    tVIM: tVIM instance.
    """
    
    if messagebox.askyesno("Quit", QUIT_QUESTION):
        tVIM.root.destroy()

        
def about_button():
    """Opens the 'About' information popup."""
    
    about = messagebox.showinfo(title="About", message=ABOUT_MESSAGE)
    
    
def command_button():
    """Opens the 'Commands' information popup."""
    
    commands = messagebox.showinfo(title="Commands", message=COMMANDS_MESSAGE)


# The below functions provide functionality to menu items under 'Font'


def courier_button(tVIM):
    """Changes the font inside scroll_window to Courier.
        
    Parameter
    ---------
    tVIM: tVIM instance.
    """
    
    tVIM.font = "Courier"
    tVIM.scroll_window.config(font=(tVIM.font, tVIM.font_size, tVIM.font_type))

    
def times_button(tVIM):
    """Changes the font inside scroll_window to Times.
        
    Parameter
    ---------
    tVIM: tVIM instance.
    """
    
    tVIM.font = "Times"
    tVIM.scroll_window.config(font=(tVIM.font, tVIM.font_size, tVIM.font_type))


def helv_button(tVIM):
    """Changes the font inside scroll_window to Helvetica.
        
    Parameter
    ---------
    tVIM: tVIM instance.
    """
    
    tVIM.font = "Helvetica"
    tVIM.scroll_window.config(font=(tVIM.font, tVIM.font_size, tVIM.font_type))


def comicsans_button(tVIM):
    """Changes the font inside scroll_window to Comic Sans MS.
        
    Parameter
    ---------
    tVIM: tVIM instance.
    """
    
    tVIM.font = "Comic Sans MS"
    tVIM.scroll_window.config(font=(tVIM.font, tVIM.font_size, tVIM.font_type))


def mystery_button(tVIM):
    """Changes the font inside scroll_window to Symbol.
        
    Parameter
    ---------
    tVIM: tVIM instance.
    """
    
    tVIM.font = "Symbol"
    tVIM.scroll_window.config(font=(tVIM.font, tVIM.font_size, tVIM.font_type))


def bold_button(tVIM):
    """Changes the font type inside scroll_window to Bold.
        
    Parameter
    ---------
    tVIM: tVIM instance.
    """
    
    tVIM.font_type = "bold"
    tVIM.scroll_window.config(font=(tVIM.font, tVIM.font_size, tVIM.font_type))

    
def italic_button(tVIM):
    """Changes the font type inside scroll_window to Italic.
        
    Parameter
    ---------
    tVIM: tVIM instance.
    """
    
    tVIM.font_type = "italic"
    tVIM.scroll_window.config(font=(tVIM.font, tVIM.font_size, tVIM.font_type))
    
    
def both_button(tVIM):
    """Changes the font type inside scroll_window to Bold Italic.
        
    Parameter
    ---------
    tVIM: tVIM instance.
    """
    
    tVIM.font_type = "bold italic"
    tVIM.scroll_window.config(font=(tVIM.font, tVIM.font_size, tVIM.font_type))
    
    
def none_button(tVIM):
    """Changes the font type inside scroll_window back to normal, not bold/italic.
        
    Parameter
    ---------
    tVIM: tVIM instance.
    """
    
    tVIM.font_type = ""
    tVIM.scroll_window.config(font=(tVIM.font, tVIM.font_size, tVIM.font_type))
    
    
# The below functions provide functionality to menu items under 'Themes'
    

def normal_button(tVIM):
    """Changes the theme back to default.
        
    Parameter
    ---------
    tVIM: tVIM instance.
    """
    
    tVIM.scroll_window.config(background="white", foreground="black")
    
    
def dark_button(tVIM):
    """Changes the theme to 'dark mode'.
        
    Parameter
    ---------
    tVIM: tVIM instance.
    """
    
    tVIM.scroll_window.config(background="gray17", foreground="white")

        
def gray_button(tVIM):
    """Changes the theme to 'gray'.
        
    Parameter
    ---------
    tVIM: tVIM instance.
    """
    
    tVIM.scroll_window.config(background="gray", foreground="white")
    
    
def day_button(tVIM):
    """Changes the theme to 'day'.
        
    Parameter
    ---------
    tVIM: tVIM instance.
    """
    
    tVIM.scroll_window.config(background="steel blue", foreground="white")
    
    
def evening_button(tVIM):
    """Changes the theme to 'evening'.
        
    Parameter
    ---------
    tVIM: tVIM instance.
    """
    
    tVIM.scroll_window.config(background="midnight blue", foreground="white")
    
    
def beach_button(tVIM):
    """Changes the theme to 'beach'.
        
    Parameter
    ---------
    tVIM: tVIM instance.
    """
    
    tVIM.scroll_window.config(background="papaya whip", foreground="light sea green")
    
    
def UCSD_button(tVIM):
    """Changes the theme to 'UCSD'.
        
    Parameter
    ---------
    tVIM: tVIM instance.
    """
    
    tVIM.scroll_window.config(background="dodger blue", foreground="gold")
    

def mcdonalds_button(tVIM):
    """Changes the theme to 'mcdonalds'.
        
    Parameter
    ---------
    tVIM: tVIM instance.
    """
    
    tVIM.scroll_window.config(background="red4", foreground="gold")

