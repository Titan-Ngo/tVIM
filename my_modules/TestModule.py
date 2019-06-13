"""This module writes a test for our program."""

# Import Tkinter objects (GIU package)
import tkinter as tk
import tkinter.scrolledtext as scroll 
from tkinter import messagebox
from tkinter import filedialog 
from tkinter import *

# Import our modules
from my_modules.MainModule import * # Provides main functionality of our program
from my_modules.ParseCommands import * # Provides functionaltiy for commands
from my_modules.StringConstants import * # Defines string constants 


def test_tVIM():
    """Tests tVIM class."""

    this_tVIM = tVIM()

    print("tVIM opened and closed.")
