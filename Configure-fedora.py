#!/usr/bin/env python3
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
    quadrapassel gnome-2048 transmission deja-dup tilix dconf-editor \
    remmina util-linux-user git")


def setZshForUser():
    os.system("chsh -s /usr/bin/zsh %s" % user)

def installPapirus():
    os.system('wget -qO- https://raw.githubusercontent.com/PapirusDevelopmentTeam/papirus-icon-theme/master/install-papirus-root.sh | sh')

def dconfNautilus():


def dconfOther():

def syncFromGit():
    os.system("git clone https://github.com/Deminarcis/Admin-Scripts.git")
