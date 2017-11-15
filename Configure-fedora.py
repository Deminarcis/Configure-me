import os
import platform
import errno
import sys

user = os.getlogin()
uid = os.getuid()

if os.getuid() != 0:
    exit("This script contains commands that must be run as root, please restart using sudo or run this script as root")


def updates():
    os.system("dnf upgrade --refresh -y")


def installFedy():
    os.system("sudo sh -c 'curl https://www.folkswithhats.org/installer | bash'")


def systemTools():
    os.system("dnf install -y samba-common eiciel zsh easytag gimp pavucontrol \
    quadrapassel gnome-2048 trasnmission deja-dup tilix filezilla dconf-editor \
    remmina")


def setZshForUser():
    setZsh = raw_input("Would you like to set Zsh as your default shell?: ")
    if setZsh == "Y" or "y":
        os.system("chsh -s /usr/bin/zsh %s" % uid)
