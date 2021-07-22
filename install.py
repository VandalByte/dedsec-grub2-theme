# ______         _ _____             _____ ______ _   _______   _   _                         
# |  _  \       | /  ___|           |  __ \| ___ \ | | | ___ \ | | | |                        
# | | | |___  __| \ `--.  ___  ___  | |  \/| |_/ / | | | |_/ / | |_| |__   ___ _ __ ___   ___ 
# | | | / _ \/ _` |`--. \/ _ \/ __| | | __ |    /| | | | ___ \ | __| '_ \ / _ \ '_ ` _ \ / _ \
# | |/ /  __/ (_| /\__/ /  __/ (__  | |_\ \| |\ \| |_| | |_/ / | |_| | | |  __/ | | | | |  __/
# |___/ \___|\__,_\____/ \___|\___|  \____/\_| \_|\___/\____/   \__|_| |_|\___|_| |_| |_|\___|
# 
# Written by : Vandal (vandalsoul)
# Github : https://github.com/vandalsoul/dedsec-grub-theme/
#
                                                                                            
# imports
import subprocess

# functions
def check_root() -> None:
    id = int(subprocess.check_output("id -u", shell=True).decode("utf-8"))
    if id != 0:
        print("(!) Run the script with 'sudo' privileges or as root user !!")
        exit()


def get_os_release() -> str:
    with open("/etc/os-release", "r") as os_release_file:
        data = os_release_file.read().splitlines()
        for i in data:
            if i.startswith("ID"):
                os_release = i.split("=")[-1].strip()
                return os_release.lower()
    return ""


def change_grub_theme(grub_theme_path: str) -> None:
    with open("/etc/default/grub", "r") as grub_file:
        data = grub_file.readlines()
        for i, line in enumerate(data):
            if line.startswith("GRUB_THEME"):
                data.pop(i)  # removing existing line
                data.insert(i, f'GRUB_THEME="{grub_theme_path}"\n')  # adding new line

    with open("/etc/default/grub", "w") as grub_file:
        grub_file.writelines(data)


# main-script
check_root()

THEME_DIR = "dedsec/"
OS_RELEASE = get_os_release()  # getting os release id

if not OS_RELEASE:  # exits if cant find
    print("(!) Couldn't find the OS release version. Exiting the script...")
    exit()

if OS_RELEASE in ["debian", "ubuntu"]:  # for Debian based
    GRUB_THEMES_DIR = "/boot/grub/themes/"
    GRUB_UPDATE_CMD = "update-grub"
else:
    print("(!) Couldn't find the OS release version. Exiting the script...")
    exit()

# copying theme folder
print("Copying the theme directory...\n")
subprocess.run(f"cp -r {THEME_DIR} {GRUB_THEMES_DIR}", shell=True)

# editing the grub file
THEME_PATH = f"{GRUB_THEMES_DIR}{THEME_DIR}theme.txt"
change_grub_theme(THEME_PATH)

# updating grub
subprocess.run(GRUB_UPDATE_CMD, shell=True)
