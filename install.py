#   ___         _ ___            ___ ___ _   _ ___     _   _
#  |   \ ___ __| / __| ___ __   / __| _ \ | | | _ )___| |_| |_  ___ _ __  ___
#  | |) / -_) _` \__ \/ -_) _| | (_ |   / |_| | _ \___|  _| ' \/ -_) '  \/ -_)
#  |___/\___\__,_|___/\___\__|  \___|_|_\\___/|___/    \__|_||_\___|_|_|_\___|
#
# Version: 3.0
#
# Written by Vandal (vandalsoul)
# Github: https://github.com/vandalsoul/dedsec-grub2-theme/

# imports
import subprocess
import os
import shutil
import re

# functions
def check_root() -> None:
    id = int(subprocess.check_output("id -u", shell=True).decode("utf-8"))
    if id != 0:
        print("(!) Run the script with 'sudo' privileges or as root user !!\n")
        exit()


def change_grub_theme(grub_theme_path: str) -> None:

    output = str(subprocess.check_output("cat /etc/*-release", shell=True).decode("utf-8"))
    id = re.search(".*[a-zA-Z]+=[a-zA-Z]+", output).group(0)
    distro = id.replace("ID=","").lower().strip()

    with open("/etc/default/grub", "r") as grub_file:
        data = grub_file.readlines()
        flag = False
        for i, line in enumerate(data):
            # fedora fix
            if (distro in ["fedora","redhat"]) and (line.startswith("GRUB_TERMINAL_OUTPUT")):
                data.pop(i)
                data.insert(i, f'#{line}\n')
            # adding grub theme path
            elif line.startswith("GRUB_THEME"):
                flag = True
                data.pop(i)  # removing existing line
                data.insert(i, f'GRUB_THEME="{grub_theme_path}"\n')  # adding new line
				
        if not flag:
            data.append(f'GRUB_THEME="{grub_theme_path}"\n')

    with open("/etc/default/grub", "w") as grub_file:
        grub_file.writelines(data)

def prompt(choices) -> str:
    options = list(choices)
    while True:
        print(f"(#) Choose an option [{options[0]}-{options[-1]}] : ", end="")
        choice = input().upper()
        if choice not in options:
            print(f"\nSelect one of the available options !!\n")
            continue
        return choice

# main-script
def main():
    print(
        r"""
    ___         _ ___            ___ ___ _   _ ___     _   _                  
    |   \ ___ __| / __| ___ __   / __| _ \ | | | _ )___| |_| |_  ___ _ __  ___ 
    | |) / -_) _` \__ \/ -_) _| | (_ |   / |_| | _ \___|  _| ' \/ -_) '  \/ -_)
    |___/\___\__,_|___/\___\__|  \___|_|_\\___/|___/    \__|_||_\___|_|_|_\___|

    Written by Vandal (vandalsoul)
    Github: https://github.com/vandalsoul/dedsec-grub2-theme/                                                                   
    """
    )
    print("\n( DEDSEC GRUB-THEME INSTALLER )\n")
    check_root()

    THEME = "dedsec/"  # Theme name

    # debian | arch
    if os.path.exists("/boot/grub/"):

        GRUB_THEMES_DIR = "/boot/grub/themes/"
        GRUB_UPDATE_CMD = "grub-mkconfig -o /boot/grub/grub.cfg"
		
        if not os.path.exists(GRUB_THEMES_DIR):
            os.mkdir(GRUB_THEMES_DIR)
    # fedora | redhat
    elif os.path.exists("/boot/grub2/"):

        GRUB_THEMES_DIR = "/boot/grub2/themes/"
        GRUB_UPDATE_CMD = "grub2-mkconfig -o /boot/grub2/grub.cfg"
		
        if not os.path.exists(GRUB_THEMES_DIR):
            os.mkdir(GRUB_THEMES_DIR)

    else:  # if grub not installed
        print("\n(!) Couldn't find the GRUB directory. Exiting the script ...")
        exit()

    # theme styles
    styles = {
        "A": "Compact",
        "B": "Hype",
        "C": "Legion",
        "D": "Unite",
        "E": "Wrench",
        "F": "Brainwash",
        "G": "Firewall",
        "H": "LoveTrap",
        "I": "RedSkull",
        "J": "Spam",
        "K": "Spyware",
        "L": "Strike",
        "M": "WannaCry",
    }

    print("(#) Choose you Theme-Style :\n")

    style_sheet_menu = f"""
        (A)  Compact theme       (H)  LoveTrap theme 
        (B)  Hype theme          (I)  RedSkull theme 
        (C)  Legion theme        (J)  Spam theme     
        (D)  Unite theme         (K)  Spyware theme  
        (E)  Wrench theme        (L)  Strike theme   
        (F)  Brainwash theme     (M)  WannaCry theme
        (G)  Firewall theme 

    """
    print(style_sheet_menu)
    choice = prompt(styles.keys())

    THEME_DIR = f"{GRUB_THEMES_DIR}{THEME}"

    if os.path.exists(THEME_DIR):  # added due to shutil.copytree fail
        print("\n")
        ask = input("(?) Another version of this theme is already installed,\n    Do you wish to remove it and add the new one (y/n)? [default = n] : ")
        if ask.lower() != "y":
            print("\n(!) No changes were made. Exiting the script ...\n")
            exit()
        else:
            shutil.rmtree(THEME_DIR)
            print("\n($) Removed the previous version ...")

    # copying theme folder
    print("\n($) Copying the theme directory ...")
    shutil.copytree(THEME, THEME_DIR)

    # copying required assets to theme directory
    ICON_THEME = "color"

    BACKGROUND_PATH = f"assets/backgrounds/{styles.get(choice).lower()}.png"
    ICONS_PATH = f"assets/icons/{ICON_THEME}/"

    shutil.copy(BACKGROUND_PATH, f"{THEME_DIR}")
    shutil.copytree(ICONS_PATH, f"{THEME_DIR}/{ICON_THEME}")

    os.rename(f"{THEME_DIR}{styles.get(choice).lower()}.png", f"{THEME_DIR}background.png")
    os.rename(f"{THEME_DIR}{ICON_THEME}/", f"{THEME_DIR}icons/")

    # editing the grub file
    print("\n($) Editing the GRUB file ...")
    THEME_PATH = f"{THEME_DIR}theme.txt"
    change_grub_theme(THEME_PATH)

    # updating grub
    print("\n($) Updating GRUB ...\n")
    subprocess.run(GRUB_UPDATE_CMD, shell=True)

    print("\n($) DedSec GRUB theme was successfully installed !!\n")
    exit()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("\n(!) An unexpected error occured while running the script. Installation was unsuccessful ...\n")
        print(f"(!) ERROR: {e}")
        exit()
