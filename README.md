<p align="center">
  <img width=90% src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/banner.png" alt="banner" />
</p>

<p align="center">
  <a href="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/LICENSE">
    <img src="https://img.shields.io/badge/License%20GPL--3.0-008a8a?style=for-the-badge&logo=github&logoColor=000000" alt="license" />
  </a>
  <a href="https://www.pling.com/p/1569525">
    <img src="https://img.shields.io/badge/Download-green?style=for-the-badge&logo=github&logoColor=000000" alt="license" />
  </a>
  <a href="https://www.pling.com/p/1569525">
    <img src="https://img.shields.io/badge/Version--4.0-ff173f?style=for-the-badge&logo=github&logoColor=000000" alt="license" />
  </a>
</p>

**📣 NOTE : I haven't tested the 2K version of the theme because I don't have a 2K display, so if someone could test it out and let me know how it works, that would be fantastic.**

### ✔️ Installation

```shell
git clone --depth 1 https://github.com/VandalByte/dedsec-grub2-theme.git && cd dedsec-grub2-theme
sudo python3 dedsec-theme.py --install
```

### ✔️ Manual Installation
*Click to view...*
<details>
 <summary><b>Debian 💀 Ubuntu 💀 Arch</b></summary>
 
  #### 1️⃣ Download your favourite version of the theme from [**Pling**](https://www.pling.com/p/1569525/).

  Now extract your downloaded .zip file.

  Either manually extract it or use the command below. ( *Here I'm using 'brainwash' version of my theme as an example* )
  ```shell
  unzip dedsec-brainwash.zip
  ```
  *The rest of the commands are the same for all the theme styles.*

  #### 2️⃣ Copy the theme directory.
  ```shell
  sudo cp -r dedsec /boot/grub/themes/
  ```
  #### 3️⃣ Make changes to the GRUB config file.

  ```shell
  sudo nano /etc/default/grub
  ```
  Find the line `GRUB_THEME=` then change it to `GRUB_THEME="/boot/grub/themes/dedsec/theme.txt"`

  Then save the file.

  #### 4️⃣ Finally, update the grub.
  ```shell
  sudo grub-mkconfig -o /boot/grub/grub.cfg
  ```
  Now the theme should be installed successfully, enjoy !!
</details>

<details>
 <summary><b>Fedora 💀 Redhat</b></summary>
 
  #### 1️⃣ Download your favourite version of the theme from [**Pling**](https://www.pling.com/p/1569525).

  Now extract your downloaded .zip file.

  Either manually extract it or use the command below. ( *Here I'm using 'brainwash' version of my theme as an example* )
  ```shell
  unzip dedsec-brainwash.zip
  ```
  *The rest of the commands are the same for all the theme styles.*

  #### 2️⃣ Copy the theme directory.
  ```shell
  sudo cp -r dedsec /boot/grub2/themes/
  ```
  #### 3️⃣ Make changes to the GRUB config file.

  ```shell
  sudo nano /etc/default/grub
  ```
  Find the line `GRUB_THEME=` then change it to `GRUB_THEME="/boot/grub2/themes/dedsec/theme.txt"`
 
  Change the line `GRUB_TERMINAL_OUTPUT=console` to this *(comment it out)* `#GRUB_TERMINAL_OUTPUT=console`

  Then save the file.

  #### 4️⃣ Finally, update the grub.
  ```shell
  sudo grub2-mkconfig -o /boot/grub2/grub.cfg
  ```
  Now restart your computer the grub theme should be installed successfully, enjoy !!
</details>

### ❌ Uninstallation
```shell
sudo python3 dedsec-theme.py --uninstall
```
**With a little effort the theme's text colours, progress bar colours, progress bar text, and so on can all be customised in `theme.txt` to your liking 💕**
<p align="center">
  <b>Please consider 🤗 giving this project a star ⭐ if you liked it</b>
</p>

<p align="center">
  <b>Follow me on 💬 <a href="https://github.com/VandalByte">Github</a> or 💬 <a href="https://twitter.com/VandalByte">Twitter</a>  to stay up to date on all future updates ...</b>
</p>

## 📸 Preview

<p align="center">
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-compact.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-hackerden.png" />
  <br>
  <b>💀 Compactㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ💀 HackerDen</b>
</p>

<p align="center">
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-unite.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-wrench.png" />
  <br>
  <b>💀 Uniteㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ 💀 Wrench</b>
</p>

<p align="center">
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-sitedown.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-comments.png" />
  <br>
  <b>💀 SiteDownㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ💀 Comments</b>
</p>

<p align="center">
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-trolls.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-mashup.png" />
  <br>
  <b>💀 Trollsㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ💀 Mashup</b>
</p>

<p align="center">
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-fuckery.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-tremor.png" />
  <br>
  <b>💀 Fuckeryㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ💀 Tremor</b>
</p>

<p align="center">
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-reaper.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-stalker.png" />
  <br>
  <b>💀 Reaperㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ💀 Stalker</b>
</p>

<p align="center">
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-brainwash.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-lovetrap.png" />
  <br>
  <b>💀 Brainwashㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ💀 LoveTrap</b>
</p>

<p align="center">
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-spyware.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-spam.png" />
  <br>
  <b>💀 Spywareㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ💀 Spam</b>
</p>

<p align="center">
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-redskull.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-strike.png" />
  <br>
  <b>💀 RedSkullㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ💀 Strike</b>
</p>

<p align="center">
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-firewall.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-wannacry.png" />
  <br>
  <b>💀 Firewallㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ💀 WannaCry</b>
</p>

<p align="center">
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-legion.png" />
  <br>
  <b>💀 Legion</b>
</p>

|    |    |    |
|:-------:|:-------:|:---------:|
|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|
|[**Linux Mind**](https://www.pling.com/p/1397139/)|[**Descent**](https://www.pling.com/p/1000083/)|[**Steam Big Picture**](https://github.com/LegendaryBibo/Steam-Big-Picture-Grub-Theme)|
|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|
|[**Virtuaverse (Alt Backgrounds in lower comment)**](https://www.reddit.com/r/unixporn/comments/m5522z/grub2_had_some_fun_with_grub/gqy61xm/)|[**YoRHa**](https://github.com/OliveThePuffin/yorha-grub-theme)|[**CRT-Amber**](https://www.pling.com/p/1727268/)|
|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|
|[**Matter (Customizable)**](https://www.pling.com/p/1400298/)|[**DedSec**](https://www.pling.com/p/1569525/)|[**Sekiro**](https://github.com/semimqmo/sekiro_grub_theme)|
|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|
|[**BigSur**](https://www.pling.com/p/1443844/)|[**Fallout**](https://www.pling.com/p/1230882/)|[**Graphite**](https://www.pling.com/p/1676418/)|
|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|
|[**Cyberpunk 2077**](https://www.pling.com/p/1515662/)|[**CyberRe**](https://www.pling.com/p/1420727/)|[**Cyberpunk**](https://www.pling.com/p/1429443/)|
|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|
|[**Grau**](https://www.pling.com/p/1111514/)|[**Untitled**](https://github.com/samoht9277/dotfiles/tree/master/grub/themes/self)|[**Breeze**](https://www.linux-apps.com/p/1000111/)|
|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|
|[**Plasma-Dark**](https://www.pling.com/p/1195799/)|[**Deadora**](https://www.pling.com/p/1111550/)|[**Plasma-Light**](https://www.pling.com/p/1197062/)|
|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|
|[**Sleek (Set)**](https://www.pling.com/p/1414997/)|[**Atomic**](https://www.pling.com/p/1200710/)|[**Aero**](https://www.pling.com/p/1112066/)|
|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|
|[**Standby**](https://www.pling.com/p/1172610/)|[**Axiom**](https://www.pling.com/p/1111735/)|[**Solarized-Dark**](https://www.pling.com/p/1177401/)|
|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|
|[**Retro GRUB**](https://www.pling.com/p/1568741/)|[**CyberXero**](https://www.pling.com/p/1502415/)|[**Distro Themes (set)**](https://www.pling.com/p/1482847/)|
|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|
|[**Poly Light**](https://www.pling.com/p/1176413/)|[**Solstice**](https://www.pling.com/p/1111874/)|[**Poly Dark**](https://www.pling.com/p/1230780/)|
|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|
|[**Dark Matter (Set)**](https://www.pling.com/p/1603282/)|[**Virtual Future**](https://www.pling.com/p/1529571/)|[**Grubby Terminal**](https://gitlab.com/perthshiretim/grubby-terminal)|
|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|![placeholder](/Images/Placeholderr.png)|
|[**Monochrome Dark**](https://www.pling.com/p/1111868/)|[**Billy's Agent**](https://gitlab.com/Drorago/billys-agent-grub2-theme)|[**Monochrome Light**](https://www.pling.com/p/1111486/)|

