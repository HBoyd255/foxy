from pyvda import get_apps_by_z_order
import win32process
import psutil


def is_app_open_on_current_desktop(app_name: str) -> bool:
    """Checks if an app is open on the current virtual desktop.

    Args:
        app_name (str): The name of the app to check for.

    Returns:
        bool: whether the app is open on the current virtual desktop.
    """

    open_windows = get_apps_by_z_order()

    # Iterates through each open window.
    for window in open_windows:

        # Get the handle of the window.
        window_handle = window.hwnd

        # Get the process id of the window handle.
        process_id = win32process.GetWindowThreadProcessId(window_handle)[1]

        # Gets the process associated with the process id.
        process = psutil.Process(process_id)

        # Get the name of the process.
        process_name = process.name()

        # If the app name is found in the process name, return True.
        if app_name in process_name:
            return True

    # If the app name was not found, return False.
    return False
