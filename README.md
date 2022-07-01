<p align="center">
  <img width=90% src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/update-4.0/media/banner.png" alt="banner" />
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

## ⚙️ Installation

### ✅ Using Installation Script

#### 1️⃣ Clone the repository
```shell
git clone --depth 1 https://github.com/VandalByte/dedsec-grub2-theme.git
cd dedsec-grub2-theme
```

#### 2️⃣ Run `install.py`
```shell
sudo python3 install.py
```

### ✅ Manual Installation
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

<p align="center">
  <b>If you liked 💕 my project please give it a star ⭐ this will inspire me lot and show me that you guys actually like and support my work...</b>
  <b>So ummm... that's all 😅 have an awesome day 🤗</b>
</p>

<p align="center">
  <b>Also follow me on 💬 <a href="https://github.com/VandalByte">Github</a> or on 💬 <a href="https://twitter.com/VandalByte">Twitter</a>  to keep in touch with all the updates...</b>
</p>

## 📸 Preview

<p align="center">
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-compact.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-hackerden.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-unite.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-wrench.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-sitedown.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-mashup.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-fuckery.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-tremor.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-stalker.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-reaper.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-brainwash.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-lovetrap.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-spam.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-spyware.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-redskull.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-firewall.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-strike.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-wannacry.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/dedsec-grub2-theme/main/media/previews/preview-legion.png" />
</p>
