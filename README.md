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

### ✔️ Installation

```fish
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
  ```fish
  unzip dedsec-brainwash.zip
  ```
  *The rest of the commands are the same for all the theme styles.*

  #### 2️⃣ Copy the theme directory.
  ```fish
  sudo cp -r dedsec /boot/grub/themes/
  ```
  #### 3️⃣ Make changes to the GRUB config file.

  ```fish
  sudo nano /etc/default/grub
  ```
  Find the line `GRUB_THEME=` then change it to `GRUB_THEME="/boot/grub/themes/dedsec/theme.txt"`

  Then save the file.

  #### 4️⃣ Finally, update the grub.
  ```fish
  sudo grub-mkconfig -o /boot/grub/grub.cfg
  ```
  Now the theme should be installed successfully, enjoy !!
</details>

<details>
 <summary><b>Fedora 💀 Redhat</b></summary>
 
  #### 1️⃣ Download your favourite version of the theme from [**Pling**](https://www.pling.com/p/1569525).

  Now extract your downloaded .zip file.

  Either manually extract it or use the command below. ( *Here I'm using 'brainwash' version of my theme as an example* )
  ```fish
  unzip dedsec-brainwash.zip
  ```
  *The rest of the commands are the same for all the theme styles.*

  #### 2️⃣ Copy the theme directory.
  ```fish
  sudo cp -r dedsec /boot/grub2/themes/
  ```
  #### 3️⃣ Make changes to the GRUB config file.

  ```fish
  sudo nano /etc/default/grub
  ```
  Find the line `GRUB_THEME=` then change it to `GRUB_THEME="/boot/grub2/themes/dedsec/theme.txt"`
 
  Change the line `GRUB_TERMINAL_OUTPUT=console` to this *(comment it out)* `#GRUB_TERMINAL_OUTPUT=console`

  Then save the file.

  #### 4️⃣ Finally, update the grub.
  ```fish
  sudo grub2-mkconfig -o /boot/grub2/grub.cfg
  ```
  Now restart your computer the grub theme should be installed successfully, enjoy !!
</details>

### ❌ Uninstallation
```fish
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

|    |    |    |
|:-------:|:-------:|:---------:|
|![Compact](https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-compact.png)|![HackerDen](https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-hackerden.png)|![Legion](https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-legion.png)|
|**💀 Compact**|**💀 HackerDen**|**💀 Legion**|
|![Wrench](https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-wrench.png)|![Unite](https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-unite.png)|![Mashup](https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-mashup.png)|
|**💀 Wrench**|**💀 Unite**|**💀 Mashup**|
|![SiteDown](https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-sitedown.png)|![Trolls](https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-trolls.png)|![Comments](https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-comments.png)|
|**💀 SiteDown**|**💀 Trolls**|**💀 Comments**|
|![Fuckery](https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-fuckery.png)|![Tremor](https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-tremor.png)|![Reaper](https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-reaper.png)|
|**💀 Fuckery**|**💀 Tremor**|**💀 Reaper**|
|![Stalker](https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-stalker.png)|![Brainwash](https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-brainwash.png)|![LoveTrap](https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-lovetrap.png)|
|**💀 Stalker**|**💀 Brainwash**|**💀 LoveTrap**|
|![Spyware](https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-spyware.png)|![Spam](https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-spam.png)|![RedSkull](https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-redskull.png)|
|**💀 Spyware**|**💀 Spam**|**💀 RedSkull**|
|![Strike](https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-strike.png)|![Firewall](https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-firewall.png)|![WannaCry](https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-wannacry.png)|
|**💀 Strike**|**💀 Firewall**|**💀 WannaCry**|
