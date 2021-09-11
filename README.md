![logo](/media/logo.png)

![GitHub](https://img.shields.io/github/license/vandalsoul/dedsec-grub2-theme?style=for-the-badge)

This theme was created, inspired by the fictional hacker group **DedSec** from **Watch Dogs** video game developed by **Ubisoft**.

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

On your keyboard press `Ctrl + O` then press `Enter`, the changes will be saved and press `Ctrl + X` to exit nano.

#### 3️⃣ Finally, update the grub.

- **Debian | Ubuntu | Arch**
```shell
sudo grub-mkconfig -o /boot/grub/grub.cfg
```
- **Fedora | Redhat**
```shell
sudo grub2-mkconfig -o /etc/grub2.cfg
```
There you go all done.

## 💰 Donate
If you like my work please consider donating, and it would really help me a lot, thanks 😇

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/vandalsoul)

## 📸 Preview
![Screenshot](/media/screenshot.png)

## 💡 Fix-it Tips
*Click to view...*

<details>
  <summary><b>( Q ] GRUB theme doesn't show up after installing the theme?</b></summary>
  <br>
  
 *It is mainly because of your grub config file ( **located at /etc/default/grub** ).*
  
 *Default grub config will be different for every linux distro. So inorder for this to work you will have to make some tweaks in your grub config file.*

 *This is the [GRUB config](/media/mx-linux-grub-config-file.txt) file for MX Linux 19.4*

 **[ WARNING ] : This is only for referance and not for copy-pasting since it is a Debian-based distro, yours might be different and can mess up the boot if copy-pasted.**
  
</details>

## 📝 License
Made with 💖 and it's released under the **MIT** license.
