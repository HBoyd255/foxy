from modules.is_app_open import is_app_open_on_current_desktop


def main():
    if is_app_open_on_current_desktop("firefox"):
        print("Firefox is open on this virtual desktop.")
    else:
        print("Firefox is not open on this virtual desktop.")


if __name__ == "__main__":
    main()
