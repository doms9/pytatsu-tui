## What is this?

A way to save/manage \*OS blobs using [pytatsu](https://github.com/Cryptiiiic/pytatsu)

## Prerequisites

- Windows/Linux/macOS
- [Python](https://www.python.org/downloads/) (**>= 3.10**)
  - [Tkinter](https://tkdocs.com/tutorial/install.html)

## Usage

```sh
$ python3 -m pip install pytatsu-tui --upgrade

$ tatsu-tui

$ tatsu-tui -u/--unset # Unset the saved config directory
```

For every device you have, you'll be asked to provide the following information:

- [Device Model and Board Configuration](https://github.com/doms9/pytatsu-tui/blob/default/apple_devices.md)
- [Exclusive Chip Identification](https://www.theiphonewiki.com/wiki/ECID#Getting_the_ECID) (Decimal and Hex formats supported)
- [ApNonce](https://gist.github.com/m1stadev/5464ea557c2b999cb9324639c777cd09#getting-a-generator-apnonce-pair-jailbroken) (Required for A12+)
  - This **<ins>DOES NOT</ins>** freeze your ApNonce if your device isn't jailbroken, do that beforehand.
- [Generator](https://www.idownloadblog.com/2021/03/08/futurerestore-guide-1-generator/) (Required for A12+)
  - (Eg. 0x1111111111111111 for [unc0ver](https://unc0ver.dev/), 0xbd34a880be0b53f3 for [Electra](https://coolstar.org/electra/)/[Chimera](https://chimera.coolstar.org/)/[Odyssey](https://theodyssey.dev/)/[Taurine](https://taurine.app/)/[Cheyote](https://www.cheyote.io/))

## Preview

![](https://github.com/doms9/pytatsu-tui/blob/default/preview.gif)

---

###### [API used for Apple's Stable Firmwares](https://ipswdownloads.docs.apiary.io/#)

###### [API used for Apple's Beta Firmwares](https://github.com/m1stadev/ios-beta-api)

###### [Cryptiiiic's Pytatsu](https://github.com/Cryptiiiic/pytatsu)
