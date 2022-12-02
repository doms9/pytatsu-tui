## What is this?

A way to save/manage \*OS blobs using [pytatsu](https://github.com/Cryptiiiic/Tatsu)

## Prerequisites

- Windows/Linux/macOS
- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads/) (**>= 3.10**)
  - [Python's Pip Package Manager](https://pip.pypa.io/en/stable/installation/)
  - [Tkinter](https://tkdocs.com/tutorial/install.html#installlinux) (If running on Linux)
- An iPod, iPhone, iPad, or Apple TV

## Usage

- Clone the repository

  ```sh
  git clone https://github.com/doms9/Tatsu-Manager --depth=1

  cd ./Tatsu-Manager
  ```

- Create a virtual environment (recommended), install requirements, and run

  - Windows (Command Prompt)

  ```cmd
  curl -sSO https://bootstrap.pypa.io/virtualenv.pyz

  py virtualenv.pyz -q venv && .\venv\Scripts\activate

  python -m pip install -r requirements.txt

  python tui.py
  ```

  - Unix OS (Bash/Z Shell)

  ```sh
  curl -sSO https://bootstrap.pypa.io/virtualenv.pyz

  python3 virtualenv.pyz -q venv && . ./venv/bin/activate

  python3 -m pip install -r requirements.txt

  python3 tui.py
  ```

For every device you have, you'll be asked to provide the following information:

- [Device Model and Board Configuration](./apple_devices.md)
- [Exclusive Chip Identification](https://www.theiphonewiki.com/wiki/ECID#Getting_the_ECID) (Decimal and Hex formats supported)
- [ApNonce](https://gist.github.com/m1stadev/5464ea557c2b999cb9324639c777cd09#getting-a-generator-apnonce-pair-jailbroken) (Required for A12+)
  - This script **DOES NOT** freeze your ApNonce if your device isn't jailbroken, do that beforehand.
- [Generator](https://www.idownloadblog.com/2021/03/08/futurerestore-guide-1-generator/) (Required for A12+)
  - (Eg. 0x1111111111111111 for [unc0ver](https://unc0ver.dev/), 0xbd34a880be0b53f3 for [Electra](https://coolstar.org/electra/)/[Chimera](https://chimera.coolstar.org/)/[Odyssey](https://theodyssey.dev/)/[Taurine](https://taurine.app/)/[Cheyote](https://www.cheyote.io/))

---

###### [API used for Apple's Stable Firmwares](https://ipswdownloads.docs.apiary.io/#)

###### [API used for Apple's Beta Firmwares](https://github.com/m1stadev/ios-beta-api)

###### [Cryptiiiic's Pytatsu](https://github.com/Cryptiiiic/Tatsu)
