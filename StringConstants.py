"""This module defines long string constants used in tVIM."""

QUIT_QUESTION = "Are you sure you want to quit?"

ABOUT_MESSAGE = "A Text Editor with basic Vim functionality.\n Implemented by \
Titan Ngo."

COMMANDS_MESSAGE = "ESC  -> exit insert mode and enter command mode\n\
---------------------------------------\n\
COMMAND MODE:\n\
gg   -> move cursor to beginning of file\n\
G    -> move cursor to end of file\n\
o    -> create a new line below the cursor and enter insert \t\tmode\n\
O    -> create a new line below the cursor and enter insert \t\tmode\n\
i    -> enter insert mode at the cursor\n\
I    -> enter insert mode at the beginning of this line\n\
A    -> enter insert mode at the end of this line\n\
:w   -> save as\n\
:wq  -> save as and quit\n\
:q   -> quit without saving\n\
?pattern  -> search for the 'pattern' in this file"            

CMD_ERROR = "Command not recognized."

ERROR_TITLE = "Oh no, an error!"

PATTERN_NOT_FOUND = "No patterns in this file match the specified pattern."
