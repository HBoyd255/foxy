from modules.is_app_open import is_app_open_on_current_desktop

import os
import sys

FIREFOX_DIRECTORY = "C:\\Program Files\\Mozilla Firefox"


def main():

    # Change the current directory to the location of firefox.
    os.chdir(FIREFOX_DIRECTORY)

    # Combine the arguments received  by this script into one string.
    arguments = " ".join(sys.argv[1:])

    if arguments == "":
        arguments = "about:newtab"

    # By default, open a new tab.
    tab_or_window = "--new-tab"

    # If firefox is not open on the current desktop, open a new window.
    if not is_app_open_on_current_desktop("firefox"):
        tab_or_window = "--new-window"

    # Open firefox with the arguments.
    os.system(f"firefox.exe {tab_or_window} {arguments}")


if __name__ == "__main__":
    main()
