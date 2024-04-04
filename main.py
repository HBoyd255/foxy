from modules.is_app_open import is_app_open_on_current_desktop

import os
import sys
import subprocess

FIREFOX_DIRECTORY = "C:\\Program Files\\Mozilla Firefox"


def main():

    # Change the current directory to the location of Firefox.
    os.chdir(FIREFOX_DIRECTORY)

    # Get the arguments provided to the script.
    input_args = sys.argv[1:]

    # If no arguments are provided, open a new tab.
    if len(input_args) == 0:
        input_args.append("about:newtab")

    # Join the input arguments into a single string.
    joined_input_args = " ".join(input_args)

    # If Firefox is not open on the current desktop, open a new window.
    if not is_app_open_on_current_desktop("firefox"):
        tab_or_window = "--new-window"
    else:
        # If Firefox is open on the current desktop, open a new tab.
        tab_or_window = "--new-tab"

    # Open Firefox with the arguments.
    subprocess.Popen(["firefox.exe", tab_or_window, joined_input_args])


if __name__ == "__main__":
    main()
