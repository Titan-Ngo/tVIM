"""The code below enables events in response to key presses."""

# Import Tkinter objects (GIU package)
import tkinter as tk
import tkinter.scrolledtext as scroll 
from tkinter import messagebox
from tkinter import filedialog 
from tkinter import *

# Import our modules
from my_modules.MainModule import * # Provides main functionality of our program
from my_modules.StringConstants import * # Defines string constants 
  
    
def parse_command(tVIM, event):
    """Parses commands entered inside of cmd_line and checks whether
    they are valid. Provides the functionality for all commands.
        
    Parameters
    ----------
    tVIM: tVIM instance.
    event: A keyboard event.
    """
    
    # Get the str inside cmd_line
    command = tVIM.cmd_line.get('1.0', END)
    # Strip all new line chars from cmd_line.get()
    command = command.replace('\n', '')
        
    # 'o' command - Insert new line below and enter insert
    if command == "o":
        # The line below removes all previous highlighting
        tVIM.scroll_window.tag_remove("highlight", '1.0', END)
        # Moves the cursor to end of this line and inserts a newline char
        tVIM.scroll_window.mark_set(INSERT, INSERT + " lineend")
        tVIM.scroll_window.insert(INSERT, '\n')
        insert_mode(tVIM)
        clear_cmd_line(tVIM)
        
    # 'O' command - Insert new line above and enter insert
    elif command == "O":
        # The line below removes all previous highlighting
        tVIM.scroll_window.tag_remove("highlight", '1.0', END)
        # Moves the cursor to start of this line and inserts a newline char
        tVIM.scroll_window.mark_set(INSERT, INSERT + " linestart")
        tVIM.scroll_window.insert(INSERT, '\n')
        # Moves the cursor one line above the current line
        tVIM.scroll_window.mark_set(INSERT, INSERT + " -1line")
        insert_mode(tVIM)
        clear_cmd_line(tVIM)
        
    # 'gg' command - Move to the beginning of file
    elif command == "gg":
        # The line below removes all previous highlighting
        tVIM.scroll_window.tag_remove("highlight", '1.0', END)
        tVIM.scroll_window.mark_set(INSERT, '1.0')
        tVIM.scroll_window.tag_add("highlight", INSERT, INSERT + " +1c")
        clear_cmd_line(tVIM)
               
    # 'G' command - Move to the end of file
    elif command == "G":
        # The line below removes all previous highlighting
        tVIM.scroll_window.tag_remove("highlight", '1.0', END)
        tVIM.scroll_window.mark_set(INSERT, END)
        tVIM.scroll_window.tag_add("highlight", INSERT + " -1c", INSERT)
        clear_cmd_line(tVIM)
    
    # 'i' command - Return to insert mode at cursor
    elif command == "i":
        insert_mode(tVIM)
        clear_cmd_line(tVIM)
        
    # 'I' command - Return to insert mode at linestart
    elif command == "I":
        tVIM.scroll_window.mark_set(INSERT, INSERT + " linestart")
        insert_mode(tVIM)
        clear_cmd_line(tVIM)
        
    # 'A' command - Return to insert mode at lineend
    elif command == "A":
        tVIM.scroll_window.mark_set(INSERT, INSERT + " lineend")
        insert_mode(tVIM)
        clear_cmd_line(tVIM)
      
    # '?' command - Searches for a given pattern after enter
    elif len(command) > 1 and command[0] == "?":
        
        # After enter key is pressed
        if event.char == '\r':
            
            # Get the pattern from command and search for it
            pattern = command[1:]
            search_pattern(tVIM, pattern)
            clear_cmd_line(tVIM)
            
    # ':' command - Parses commands after enter pressed
    elif len(command) > 1 and command[0] == ":":
        
        # After enter key is pressed
        if event.char == '\r':
            
            # Save as and exit command
            if command[1:] == "wq":
                save_button(tVIM)
                tVIM.root.destroy()
                
            # Exit command, prompt the user
            elif command[1:] == "q":
                exit_button(tVIM)
                clear_cmd_line(tVIM)
                
            # Save as command
            elif command[1:] == "w":
                save_button(tVIM)
                clear_cmd_line(tVIM)
                
            # Command not recognized error 
            else:
                error_popup(CMD_ERROR)
                clear_cmd_line(tVIM)
                

def insert_mode(tVIM):
    """Exits command mode and enters insert mode, moving the
    cursor back to scroll_window.
        
    Parameter
    ---------
    tVIM: tVIM instance.
    """
    
    # Focus back onto scroll_window
    tVIM.scroll_window.focus()
    # Remove all highlighting
    tVIM.scroll_window.tag_remove("highlight", '1.0', END)
    
    
def clear_cmd_line(tVIM):
    """Clears all chars in the command line.
        
    Parameter
    ---------
    tVIM: tVIM instance.
    """
    
    # Clear the command line
    tVIM.cmd_line.delete('1.0', END)
    tVIM.cmd_line.update()
    

def search_pattern(tVIM, pattern):
    """Searches for the specified pattern in this tVIM instance's
    scroll_window. Provides funcitonality for '?pattern' command.
        
    Parameters
    ----------
    tVIM: tVIM instance.
    pattern: the str pattern being searched for.
    """
    
    # Line below removes all previous highlighting
    tVIM.scroll_window.tag_remove("highlight", '1.0', END)
    
    # 'start' specifies where we start scroll_window.search
    start = '1.0'
    pattern_found = False
    
    # Keep calling scroll_window.search until we reach the end
    while (start != END):
        
        # look for the pattern from 'start' and get the position
        pos = tVIM.scroll_window.search(pattern, start, stopindex=END)
        
        # If no occurence of pattern
        if not pos:
            start = END
        
        else:
            # A position was found, highlight that word
            tVIM.scroll_window.tag_add("highlight", pos, pos  
                                    + " +" + str(len(pattern)) + "c")
            # Change start to the end of the found pattern's position
            start = pos + " +" + str(len(pattern)) + "c"
            pattern_found = True
    
    # If the pattern was not found, call an error
    if not pattern_found:
        error_popup(PATTERN_NOT_FOUND)


"""The code below handles a popup window on errors."""


def error_popup(error):
    """Forces a popup window upon a specific error.
    
    Parameter
    ---------
    error: a str, the error that occurred. Gets printed.
    """
    
    popup = messagebox.showerror(title=ERROR_TITLE, message=error)
