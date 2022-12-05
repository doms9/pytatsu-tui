import platform
import shutil
import subprocess
from configparser import ConfigParser
from distutils.util import strtobool
from pathlib import Path
from tkinter import Tk, filedialog
from typing import NoReturn

from send2trash import send2trash
from termcolor import colored

config_prsr = ConfigParser()

ERROR = colored("ERROR:", "red", attrs=["bold"])

SUCCESS = colored("Successfully", "green")


def clear_terminal() -> int:
    """
    Clear the terminal
    """

    return subprocess.call(
        "cls" if platform.system() == "Windows" else "clear",
        shell=True,
    )


def wait_to_cont(*args, clear: bool = False) -> None:
    """
    Print a message then wait for user input to continue

    `clear` is to optionally clear the terminal beforehand
    """

    if clear:
        clear_terminal()

    if args:
        print(*args)

    input("\nEnter any key to continue\n\n: ")


def wait_to_exit(*args, clear: bool = False) -> NoReturn:
    """
    Print a message then wait for user input to exit

    `clear` is to optionally clear the terminal beforehand
    """

    if clear:
        clear_terminal()

    if args:
        print(*args)

    input("\nEnter any key to exit\n\n: ")

    raise SystemExit


def config_dir() -> Path:
    """
    Path to where the config file, blobs, and buildmanifests are saved
    """

    config_dir_text = Path("./path.txt").resolve()

    if not config_dir_text.exists():
        clear_terminal()

        print("Please select a directory to save your blobs\n")

        Tk().withdraw()

        input_directory = filedialog.askdirectory(
            initialdir=Path.cwd(),
            title="Choose a directory for your blobs",
        )

        try:

            directory = Path(input_directory)

            config_dir_text.write_text(f"{directory}", encoding="utf-8")

            (directory / "permissionchecking12345").mkdir()

            (directory / "permissionchecking12345").rmdir()

        except PermissionError:
            config_dir_text.unlink()

            wait_to_exit(
                "Please select a directory where you have read and write permissions.",
                clear=True,
            )

        except TypeError:
            wait_to_exit(
                "Please re-run and select a directory to save your config file and blobs.",
                clear=True,
            )

        return directory.resolve()

    try:
        directory = Path(config_dir_text.read_text(encoding="utf-8").strip())

        (directory / "permissionchecking12345").mkdir()

        (directory / "permissionchecking12345").rmdir()

    except PermissionError:
        config_dir_text.unlink()

        wait_to_exit(
            "Please select a new directory where you have read and write permissions.",
            clear=True,
        )

    except FileNotFoundError:
        config_dir_text.unlink()

        wait_to_exit(
            "Please select a new directory to save your config file and blobs.",
            clear=True,
        )

    return directory.resolve()


def config_file() -> Path:
    """
    Path to the config file
    """

    return config_dir() / "tatsu.ini"


def bm_dir() -> Path:
    """
    Path to the buildmanifests' directory
    """

    return config_dir() / "BuildManifests"


def blob_dir(device_number: int) -> Path:
    """
    Path to the directory where blobs are saved for the given device
    """

    return config_dir() / f"DEVICE {device_number}"


def create_config() -> None:
    """
    Create a config file if it doesn't exist
    """

    while not config_file().is_file():
        clear_terminal()

        print("Config not found, creating a new one...\n")

        amount_of_devices = input("How many devices would you like to add?\n\n: ")

        try:
            devices = int(amount_of_devices)
        except ValueError:
            if amount_of_devices == "":
                raise SystemExit

            wait_to_cont(
                "Please enter the number of devices as an integer, not a string/float.",
                clear=True,
            )
            continue

        for new in range(1, devices + 1):
            clear_terminal()

            print(
                "ENTERING INFORMATION FOR",
                f"{colored(f'DEVICE {new}', attrs=['underline'])}",
            )

            config_prsr[f"DEVICE {new}"] = {}

            config_prsr[f"DEVICE {new}"]["model"] = input("\nDevice Identifier?\n\n: ")

            config_prsr[f"DEVICE {new}"]["board"] = input(
                "\nBoard Configuration?\n\n: "
            )

            config_prsr[f"DEVICE {new}"]["ecid"] = input(
                "\nExclusive Chip Identification (ECID)?\n\n: "
            )

            config_prsr[f"DEVICE {new}"]["generator"] = input(
                "\nGenerator? (Required for A12+)\n\n: "
            )

            config_prsr[f"DEVICE {new}"]["apnonce"] = input(
                "\nApNonce? (Required for A12+)\n\n: "
            )

        with config_file().open("w", encoding="utf-8") as a:
            config_prsr.write(a)

        wait_to_cont(
            f"{SUCCESS} added {devices} device(s) to the config!",
            clear=True,
        )
        break


def num_of_devices() -> list[int]:
    """
    Return the numbers of devices in the config
    """

    config_prsr.read(config_file())

    return [devices[0] for devices in enumerate(config_prsr.sections(), start=1)]


def add_device() -> None:
    """
    Add device(s) to the config
    """

    clear_terminal()

    existing = num_of_devices()[-1]

    amount_of_devices = input("How many new devices would you like to add?\n\n: ")

    try:
        devices = int(amount_of_devices)
    except ValueError:
        if amount_of_devices == "":
            return

        wait_to_cont(
            "Please enter the number of new devices as an integer.",
            clear=True,
        )
        return

    for i in range(1, devices + 1):
        new = existing + i

        clear_terminal()

        print(
            "ENTERING INFORMATION FOR",
            f"{colored(f'DEVICE {new}', attrs=['underline'])}",
        )

        config_prsr[f"DEVICE {new}"] = {}

        config_prsr[f"DEVICE {new}"]["model"] = input("\nDevice Identifier?\n\n: ")

        config_prsr[f"DEVICE {new}"]["board"] = input("\nBoard Configuration?\n\n: ")

        config_prsr[f"DEVICE {new}"]["ecid"] = input(
            "\nExclusive Chip Identification (ECID)\n\n: "
        )

        config_prsr[f"DEVICE {new}"]["generator"] = input(
            "\nGenerator? (Required for A12+)\n\n: "
        )

        config_prsr[f"DEVICE {new}"]["apnonce"] = input(
            "\nApNonce? (Required for A12+)\n\n: "
        )

    with config_file().open("w", encoding="utf-8") as b:
        config_prsr.write(b)

    wait_to_cont(
        f"{SUCCESS} added {devices} device(s) to the config!",
        clear=True,
    )
    return


def rm_device() -> bool:
    """
    Remove device(s) from the config

    Returns `1 (True)` if a device was removed

    Returns `0 (False)` otherwise
    """

    clear_terminal()

    confirm = 0

    print("Which device would you like to remove?\n")

    for num in num_of_devices():
        model = config_prsr[f"DEVICE {num}"]["model"]
        print(f"{num}) DEVICE {num} ({colored(model, 'cyan')})")

    selected_device = input("\n: ")

    try:
        device = int(selected_device)
    except ValueError:
        if selected_device == "":
            return confirm

        wait_to_cont(
            "Please enter an integer from the list of devices.",
            clear=True,
        )
        return confirm

    if device in num_of_devices():
        print(
            f"\nBy proceeding, all saved blobs for DEVICE {device}",
            f"will be {colored('deleted', 'red', attrs=['underline'])}\n",
        )

    else:
        wait_to_cont(
            f"DEVICE {colored(device, 'red')} does not exist.",
            clear=True,
        )
        return confirm

    try:
        confirm = strtobool(
            input("Are you sure you want to continue?\n\n[Y/N]: ").strip()
        )
    except ValueError:
        confirm = 0

    if confirm:
        delete_blob_dirs(device)

        wait_to_cont(
            f"{SUCCESS} deleted DEVICE {device}!",
            clear=True,
        )

    else:
        wait_to_cont(
            "Aborting...",
            clear=True,
        )

    return confirm


def delete_blob_dirs(device: int) -> None:
    """
    Delete the blob directory for the given device
    """

    if len(num_of_devices()) == device == 1:
        send2trash(config_file())

        if blob_dir(1).exists():
            send2trash(blob_dir(1))

        return

    if blob_dir(device).exists():
        send2trash(blob_dir(device))

    if device == 1:
        for existing in num_of_devices()[1:]:
            if (blob_dir(existing)).is_dir():
                shutil.move(
                    blob_dir(existing),
                    blob_dir(existing - 1),
                )
    else:
        for existing in num_of_devices()[device - 1 :]:  # noqa
            if (blob_dir(existing)).is_dir():
                shutil.move(
                    blob_dir(existing),
                    blob_dir(existing - 1),
                )

    update_config(device, num_of_devices()[-1])


def update_config(
    selected_device: int,
    total_devices: int,
) -> None:

    """
    Update the config after removing a device
    """

    config_prsr.read(config_file())

    config_prsr.remove_section(f"DEVICE {selected_device}")

    if selected_device != total_devices:
        for device in range(selected_device, total_devices + 1):
            if device != selected_device:
                items = config_prsr.items(f"DEVICE {device}")

                config_prsr.remove_section(f"DEVICE {device}")

                config_prsr.add_section(f"DEVICE {device - 1}")

                for key, val in items:
                    config_prsr.set(f"DEVICE {device - 1}", key, val)

    with config_file().open("w", encoding="utf-8") as a:
        config_prsr.write(a)
