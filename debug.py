# This file contains all debug functions
debug = False


# Debug out function for displaying a value
def out(prefix, value):
    if debug:
        print(f"DEBUG: {prefix} = {str(value)}")


# Debug info for displaying the flow of code
def info(information):
    if debug:
        print(f"DEBUG: {information}")


# Used for displaying to the console an error and if it was fatal exiting the program
def error(message, fatal):
    if debug:
        if fatal:
            exit(f"Fatal Error: {message}")
        else:
            print(f"ERROR: {message}")
