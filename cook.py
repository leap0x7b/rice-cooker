#!/usr/bin/env python3
###############################################################
#                                                             #
#          .-.          Rice Cooker (Alpha)                   #
#     -------------                                           #
#    /:::::::::::::\    A quick and easy tool for your ricing #
#  (=================)  purposes                              #
#    |%%%%%%%%%%%%%|                                          #
#  <&|%%%% --- %%%%|&>  Author: Leap of Azzam                 #
#  <&|%%%% --- %%%%|&>  GitLab: @LeapofAzzam                  #
#  <&|%%%% --- %%%%|&>  Twitter: @leapofazzam                 #
#    \%%%%%%%%%%%%%/                                          #
#     -------------                                           #
#      v         v                                            #
#                                                             #
###############################################################

## Initialization
# Imports
import os
import sys
import distro

# Variables
windowManagers = ("i3", "Openbox", "bspwm", "Xmonad", "Awesome", "dwm", "SpectrWM", "FluxBox", "HerbstluftWM")
bars = ("Polybar", "Lemonbar")
launchers = ("Rofi", "dmenu")
terminals = ("Suckless Terminal", "Rxvt Unicode", "Cool Retro Term", "Xterm", "Terminology", "Terminator", "Guake", "Tilda", "Alacritty", "Termite", "Xfce Terminal", "MATE Terminal", "GNOME Terminal", "Konsole")
rows, columns = os.popen('stty size', 'r').read().split()

# Functions
def printCenter(text, filler=" ", column=int(columns)):
   print((text.center(column, filler)))

def installPackages(package):
   global runCode
   if (distro.like() == "ubuntu" ) or (distro.like() == "debian" ) or (distro.id() == "debian"):
      packageManager = "apt install -yy " + package
   elif (distro.like() == "archlinux" ) or (distro.like() == "arch" ) or (distro.id() == "arch"):
      packageManager = "pacman --no-confirm --needed -S " + package
   elif (distro.like() == "fedora" ) or (distro.like() == "redhat" ) or (distro.id() == "fedora") or (distro.id() == "rhel") or (distro.id() == "redhat"):
      packageManager = "dnf install -y " + package
   elif (distro.like() == "suse" ) or (distro.like() == "opensuse" ) or (distro.like() == "sles") or (distro.id() == "suse") or (distro.id() == "opensuse") or (distro.id() == "sles"):
      packageManager = "zypper install -n " + package
   elif (distro.like() == "gentoo" ) or (distro.id() == "gentoo"):
      packageManager = "emerge " + package + " --quiet"
      
   elif (distro.like() == "alpine" ) or (distro.id() == "alpine"):
      packageManager = "apk add " + package

   runCode = str(os.system("sudo " + packageManager))

def windowManagerSetup():
   global windowManagerName
   print()
   printCenter("-", "-")
   print()
   print("  Choose window manager:")
   print()
   for value in windowManagers:
      print("  " + str(windowManagers.index(value)+1) + ". " + value)
   print()
   choice = int(input("  [1-" + str(len(windowManagers))  + "] "))
   if (windowManagers[choice-1] != windowManagers[8]):
      windowManagerName = windowManagers[choice-1]
   else:
      print()
      print("  Unknown answer. Aborting..")
      exit(1)

def barSetup():
   global barName
   print()
   printCenter("-", "-")
   print()
   print("  Choose bar:")
   print()
   for value in bars:
      print("  " + str(bars.index(value)+1) + ". " + value)
   print()
   choice = int(input("  [1-" + str(len(bars))  + "] "))
   if (bars[choice-1] != bars[1]):
      barName = bars[choice-1]
   else:
      print()
      print("  Unknown answer. Aborting..")
      exit(1)

def launcherSetup():
   global launcherName
   print()
   printCenter("-", "-")
   print()
   print("  Choose launcher:")
   print()
   for value in launchers:
      print("  " + str(launchers.index(value)+1) + ". " + value)
   print()
   choice = int(input("  [1-" + str(len(launchers))  + "] "))
   launcherName = launchers[choice-1]
   if (launchers[choice-1] != launchers[1]):
      launcherName = launchers[choice-1]
   else:
      print()
      print("  Unknown answer. Aborting..")
      exit(1)

def terminalSetup():
   global terminalName
   global terminalPackageName
   terminalPackage = {
      "Suckless Terminal": "stterm",
      "Rxvt Unicode": "rxvt-unicode-256color",
      "Cool Retro Term": "cool-retro-term",
      "Xterm": "xterm",
      "Terminology": "terminology",
      "Terminator": "terminator",
      "Guake": "guake",
      "Tilda": "tilda",
      "Termite": "termite",
      "Xfce Terminal": "xfce4-terminal",
      "MATE Terminal": "mate-terminal",
      "GNOME Terminal": "gnome-terminal",
      "Konsole": "konsole"
   }
   print()
   printCenter("-", "-")
   print()
   print("  Choose terminal:")
   print()
   for value in terminals:
      print("  " + str(terminals.index(value)+1) + ". " + value)
   print()
   choice = int(input("  [1-" + str(len(terminals))  + "] "))
   if (terminals[choice-1] != terminals[13]):
      terminalName = terminals[choice-1]
      terminalPackageName = terminalPackage.get(terminalName, terminalName.lower())
   else:
      print()
      print("  Unknown answer. Aborting..")
      exit(1)

def setup():
   windowManagerSetup()
   barSetup()
   launcherSetup()
   terminalSetup()
   print()
   printCenter("-", "-")
   print()
   print("  Is this correct?")
   print()
   print("  Window manager:", windowManagerName)
   print("  Bar:", barName)
   print("  Launcher:", launcherName)
   print("  terminal:", terminalName)
   print()
   choice = input("  [Y/n] ")
   print()
   if (choice == "y"):
     installPackages(windowManagerName.lower() + " " + barName.lower() + " " + launcherName.lower() + " " + terminalPackageName.lower())
     if (runCode == "0"):
        print("  Congratulations! 🎉")
        print("  Rice Cooker has been successfully installed tools for your ricing purposes")
        print("  Now you can rice your own distribution whatever you want")
        print()
        exit(0)
     else:
        print()
        print("An error occurred:", file=sys.stderr)
        print("  Package installation canceled with return code: " + runCode, file=sys.stderr)
        #print()
        #print("Aborting..")
   else:
     setup()

## Main setup function
os.system('clear')
printCenter("-", "-")
print()
print("          \x1b[38;5;245m.-.\x1b[0m          Welcome to Rice Cooker")
print("     \x1b[38;5;220m-------------\x1b[0m     v0.2-pre Alpha")
print("    \x1b[38;5;220m/:::::::::::::\\")
print("  \x1b[38;5;245m(=================)\x1b[0m  A quick and easy tool for your ricing")
print("    |%%%%%%%%%%%%%|    purposes")
print("  \x1b[38;5;245m<&\x1b[0m|%%%%\x1b[48;5;238m\x1b[38;5;196m --- \x1b[0m%%%%|\x1b[38;5;245m&>\x1b[0m")
print("  \x1b[38;5;245m<&\x1b[0m|%%%%\x1b[48;5;238m\x1b[38;5;220m --- \x1b[0m%%%%|\x1b[38;5;245m&>\x1b[0m")
print("  \x1b[38;5;245m<&\x1b[0m|%%%%\x1b[48;5;238m --- \x1b[0m%%%%|\x1b[38;5;245m&>\x1b[0m")
print("    \\%%%%%%%%%%%%%/")
print("     -------------")
print("      \x1b[38;5;245mv         v\x1b[0m")
print()
print("  The setup will installing and setting up tools for your ricing purposes.")
choice = input("  Are you sure do you want to continue? [Y/n] ")
if (choice == "y"):
   setup()
else:
   print("  Aborting..")
   exit(1)
