# personal computer setup script for those who work with aws
# woks on ubuntu

import os


# system programs
apk_to_install = []
bash_command = "sudo apt install "

apk_to_install.append("python3-pip")
apk_to_install.append("ipython3")
apk_to_install.append("awscli")
apk_to_install.append("git")
apk_to_install.append("openssh-client")


for apk in apk_to_install:
    print("commence installing an apk -----------------------")
    os.system(bash_command + apk)
    print("--------------------------------------------------")


# programs require pip
apk_on_pip = []
command_pip = "pip3 install "

apk_on_pip.append("boto3")
apk_on_pip.append("tqdm")

for apk in apk_on_pip:
    print("commence installing an apk -----------------------")
    os.system(command_pip + apk)
    print("--------------------------------------------------")


# programs require snap
apk_on_snap = []
command_snap = "snap install"

apk_on_snap.append("vlc")
apk_on_snap.append("pycharm-professional --classic")

for apk in apk_on_snap:
    print("commence installing an apk -----------------------")
    os.system(command_snap + apk)
    print("--------------------------------------------------")


print("complete installing multiple programs")

