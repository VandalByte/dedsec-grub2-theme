# DedSec GRUB2 Theme
![DedSec Logo](/media/logo.jpg)

This theme was created inspired by the awesome fictional hacker group **DedSec** from **Watch Dogs** video game released by **Ubisoft**.

## 🗒️ Getting Started

First clone the repository, then navigate into it.
```shell
git clone https://github.com/vandalsoul/dedsec-grub2-theme.git
cd dedsec-grub2-theme
```
Run the *install.sh*
```shell
chmod +x install.sh
sudo ./install.sh
```

## ⚙️ Manual Installation

Copy the theme directory.
```shell
sudo cp -r dedsec /boot/grub/themes/
```
Make changes to the GRUB config file
```shell
sudo nano /etc/default/grub
```
Find the line `GRUB_THEME=` then change it to `blahhhhhh`
On your keyboard press `Ctrl + O` then press `Enter`, the changes will be saved.

Finally, update the grub.
```shell
sudo update-grub
```
There you go all done.

## 📸 Screenshots

## 📝 License
Made with 💖 and it's released under the **MIT license**.
