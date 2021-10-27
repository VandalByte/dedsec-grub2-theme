![logo](/media/logo.png)

<p align="center">
  <a href="https://raw.githubusercontent.com/vandalsoul/dedsec-grub2-theme/main/LICENSE"><img alt="undefined" src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge&logo=github"></a>
  <a href="https://www.gnome-look.org/p/1569525"><img alt="undefined" src="https://img.shields.io/badge/Download-Here-green?style=for-the-badge&logo=github"></a>
</p>

<b>DedSec theme was created, inspired by the fictional hacker group DedSec from Watch Dogs video game developed by Ubisoft.</b>

**📢 Upcoming UPDATE : New theme variants will be added**

## 📙 Table of Contents
- [Getting Started](https://github.com/vandalsoul/dedsec-grub2-theme#-getting-started)
- [Installation](https://github.com/vandalsoul/dedsec-grub2-theme#%EF%B8%8F-installation)
- [Donate](https://github.com/vandalsoul/dedsec-grub2-theme#-donate)
- [Preview](https://github.com/vandalsoul/dedsec-grub2-theme#-preview)
- [Fix-it Tips](https://github.com/vandalsoul/dedsec-grub2-theme#-fix-it-tips)
- [License](https://github.com/vandalsoul/dedsec-grub2-theme#-license)

## ✨ Getting Started

First clone the repository, then navigate into it.
```shell
git clone https://github.com/vandalsoul/dedsec-grub2-theme.git
cd dedsec-grub2-theme
```

## ⚙️ Installation

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
**Hey guys 🙋‍♂️ If you like my projects feel free to buy me a coffee ☕ anytime to show your loving 💗 support !!**

<a href="https://www.buymeacoffee.com/vandalsoul" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

## 📸 Preview
![Screenshot](/media/screenshot.png)

## 💡 Fix-it Tips
*Click to view...*

<details>
  <summary><b>(❓) GRUB theme doesn't show up after installing the theme? [ Fedora ]</b></summary>
  <br>
  
 *It is mainly because of your grub config file ( **located at /etc/default/grub** ).*
  
 *Default grub config will be different for every linux distro. So inorder for this to work you will have to make some tweaks in your grub config file.*
  
  *To fix this, open the file `/etc/default/grub`*
  ```
  sudo nano /etc/default/grub
  ```
  *Change the line `GRUB_TERMINAL_OUTPUT=console` to this (comment it out) `#GRUB_TERMINAL_OUTPUT=console`*
  
  *And save the file*
  
  *Then run the following command*
  ```
  sudo grub2-mkconfig -o /boot/grub2/grub.cfg
  ```
  *Now restart your computer the grub theme will show up...*
  
</details>

## 📝 License
Made with 💖 and it's released under the **MIT** license.
