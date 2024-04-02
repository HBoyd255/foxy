from modules.is_app_open import is_app_open_on_current_desktop

import os
import sys
import subprocess

FIREFOX_DIRECTORY = "C:\\Program Files\\Mozilla Firefox"


def main():

    # Change the current directory to the location of firefox.
    os.chdir(FIREFOX_DIRECTORY)

    input_args = sys.argv[1:]

    if len(input_args) == 0:
        input_args.append("about:newtab")

    # If firefox is not open on the current desktop, open a new window.
    if not is_app_open_on_current_desktop("firefox"):
        tab_or_window = "--new-window"
    else:
        # If firefox is open on the current desktop, open a new tab.
        tab_or_window = "--new-tab"

    firefox_args = ["firefox.exe"]
    firefox_args.append(tab_or_window)
    for i in input_args:
        firefox_args.append(i)

    # Open firefox with the arguments.
    subprocess.Popen(firefox_args)


if __name__ == "__main__":
    main()
