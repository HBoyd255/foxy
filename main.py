from modules.is_app_open import is_app_open_on_current_desktop

import os
import sys

FIREFOX_DIRECTORY = "C:\\Program Files\\Mozilla Firefox"

def main():

    # Change the current directory to the location of firefox.
    os.chdir(FIREFOX_DIRECTORY)

    # Combine the arguments received  by this script into one string.
    arguments = " ".join(sys.argv[1:])

    # If firefox is not open on the current desktop, add the new-window flag.
    if not is_app_open_on_current_desktop("firefox"):
        arguments += " --new-window"

    # Open firefox with the arguments.
    os.system(f"firefox.exe {arguments}")


if __name__ == "__main__":
    main()
