import os
import platform
import errno
import sys

user = os.getlogin()
uid = os.getuid()

if os.getuid() != 0:
    exit("You are not logged in as root. This script contains commands that must be run as root, please restart using sudo or run this script as root")

def updates():
    os.system("dnf upgrade --refresh -y")

def install-fedy():
    os.system("sudo sh -c 'curl https://www.folkswithhats.org/installer | bash'")

def system-tools():
    os.system
