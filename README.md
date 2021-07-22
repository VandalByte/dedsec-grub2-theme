![Logo](/media/logo.png)

This theme was created inspired by the awesome fictional hacker group **DedSec** from **Watch Dogs** video game developed by **Ubisoft**.

## 📸 Screenshots
![Screenshot](/media/screenshot.png)

## ✨ Getting Started

First clone the repository, then navigate into it.
```shell
git clone https://github.com/vandalsoul/dedsec-grub-theme.git
cd dedsec-grub-theme
```
**[ NOTE ] :** *The install.py script is only compatible with **Debian** based linux distributions so far.For others you should stick with the **Maual Installation**.*

Run the *install.py*
```shell
sudo python3 install.py
```

## ⚙️ Manual Installation

Copy the theme directory.
```shell
sudo cp -r dedsec /boot/grub/themes/
```
Make changes to the GRUB config file

*I'm using nano editor here, you can use the one of your choice.*
```shell
sudo nano /etc/default/grub
```
Find the line `GRUB_THEME=` then change it to `GRUB_THEME="/boot/grub/themes/dedsec/theme.txt"`

On your keyboard press `Ctrl + O` then press `Enter`, the changes will be saved.

Finally, update the grub.
```shell
sudo update-grub
```
There you go all done.

## 📝 License
Made with 💖 and it's released under the **GNU General Public License v3.0**.
