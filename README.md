![logo](/media/logo.png)

<p align="center">
  <b>DedSec theme was created, inspired by the fictional hacker group DedSec from Watch Dogs video game developed by Ubisoft.</b>
</p>
<p align="center">
  <a href="https://raw.githubusercontent.com/vandalsoul/dedsec-grub2-theme/main/LICENSE"><img alt="undefined" src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge&logo=github"></a>
  <a href="https://www.pling.com/p/1569525"><img alt="undefined" src="https://img.shields.io/badge/Download-Here-green?style=for-the-badge&logo=github"></a>
</p>

## ⚙️ Installation

First clone the repository, then navigate into it.
```shell
git clone https://github.com/vandalsoul/dedsec-grub2-theme.git
cd dedsec-grub2-theme
```

### ✅ Using Installation Script
Run the `install.py`
```shell
sudo python3 install.py
```

### ✅ Manual Installation

#### 1️⃣ Copy the theme directory.
```shell
sudo cp -r dedsec /boot/grub/themes/
```
#### 2️⃣ Make changes to the GRUB config file.

*I'm using `nano editor` here, you can use the one of your choice.*
```shell
sudo nano /etc/default/grub
```
Find the line `GRUB_THEME=` then change it to `GRUB_THEME="/boot/grub/themes/dedsec/theme.txt"`

> **Fedora users also need to change the line `GRUB_TERMINAL_OUTPUT=console` to this *(comment it out)* `#GRUB_TERMINAL_OUTPUT=console`**

On your keyboard press `Ctrl + O` then press `Enter`, the changes will be saved and press `Ctrl + X` to exit nano.

#### 3️⃣ Finally, update the grub.

- **Debian | Ubuntu | Arch**
```shell
sudo grub-mkconfig -o /boot/grub/grub.cfg
```
- **Fedora | Redhat**
```shell
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```
There you go all done.

## 💰 Donate

**Hey everyone 🙋‍♂️ if you wanna support me on my theme making campaign then feel free to buy me a cup of coffee ☕ anytime you wish...**
 
<a href="https://www.buymeacoffee.com/vandalsoul" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

## 📸 Preview
![Screenshot](/media/screenshot.png)

## 📝 License
Made with 💖 and it's released under the **MIT** license.
