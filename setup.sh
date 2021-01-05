#!/usr/bin/env bash
#######################################################
#         ,-,         Rice Cooker (Alpha)
#     -----------     
#    /...........\    A quick and easy tool for your
#   /.............\   ricing purposes
# (=================) 
#   |+++++++++++++|   Author: Leap of Azzam
# <&|++++ --- ++++|&> Gitlab: @LeapofAzzam
#   |++++ --- ++++|   Twitter: @LeapofAzzam
#   |++++ --- ++++|
#   \+++++++++++++/
#    -------------
#     v         v
#######################################################

set -e

function print_centered {
     [[ $# == 0 ]] && return 1

     declare -i TERM_COLS="$(tput cols)"
     declare -i str_len="${#1}"
     [[ $str_len -ge $TERM_COLS ]] && {
          echo "$1";
          return 0;
     }

     declare -i filler_len="$(( (TERM_COLS - str_len) / 2 ))"
     [[ $# -ge 2 ]] && ch="${2:0:1}" || ch=" "
     filler=""
     for (( i = 0; i < filler_len; i++ )); do
          filler="${filler}${ch}"
     done

     printf "%s$1%s" "$filler"  "$filler"
     [[ $(( (TERM_COLS - str_len) % 2 )) -ne 0 ]] && printf "%s" "${ch}"
     printf "\n"

     return 0
}

function choice_centered {
     [[ $# == 0 ]] && return 1

     declare -i TERM_COLS="$(tput cols)"
     declare -i str_len="${#1}"
     [[ $str_len -ge $TERM_COLS ]] && {
          echo "$1";
          return 0;
     }

     declare -i filler_len="$(( (TERM_COLS - str_len) / 2 ))"
     [[ $# -ge 2 ]] && ch="${2:0:1}" || ch=" "
     filler=""
     for (( i = 0; i < filler_len; i++ )); do
          filler="${filler}${ch}"
     done

     printf "%s%s" "$filler" "$1"
     [[ $(( (TERM_COLS - str_len) % 2 )) -ne 0 ]] && printf "%s" "${ch}"
     #printf "\n"
     read choice

     return 0
}

function setup_wm {
     echo
     print_centered "-" "-"
     echo
     print_centered "Choose one of these WM"
     echo
     #print_centered "1. i3-gaps           " # i3-gaps installation still in development
     print_centered "1. i3                "
     print_centered "2. Openbox           "
     print_centered "3. bspwm             "
     print_centered "4. Xmonad            "
     print_centered "5. Awesome           "
     print_centered "6. dwm               "
     print_centered "7. SpectrWM          "
     print_centered "8. FluxBox           "
     print_centered "9. HerbstluftWM      "
     echo
     choice_centered "Choose WM:"
     echo
     case $choice in
          #1)
          #echo "i3-gaps installation still in development"
          #;;
          1)
          sudo apt install i3 
          ;;
          2)
          sudo apt install openbox obconf
          ;;
          3)
          sudo apt install bspwm
          ;;
          4)
          sudo apt install xmonad
          echo "making a simple xmonad configuration"
          mkdir -p ~/.xmonad 
          touch ~/.xmonad/xmonad.hs
          cat >> ~/.xmonad/xmonad.hs << EOM
import XMonad

main = xmonad def
    { terminal    = "urxvt"
    , modMask     = mod4Mask
    , borderWidth = 3
    }
EOM
          ;;
          5)
          sudo apt install awesome
          ;;
          6)
          sudo apt install dwm
          ;;
          7)
          sudo apt install spectrwm
          ;;
          8)
          sudo apt install fluxbox
          ;;
          9)
          sudo apt install herbstluftwm
          ;;
          *)
          echo "Wrong answer. Aborting.."
          exit 1
          ;;
     esac
}

function setup_bar {
     echo
     print_centered "-" "-"
     echo
     print_centered "Choose one of these bar"
     echo
     print_centered "1. Polybar            "
     print_centered "2. Lemonbar           "
     echo
     choice_centered "Choose bar:"
     echo
     case $choice in
          1)
          sudo apt install polybar
          ;;
          2)
          sudo apt install lemonbar
          ;;
          *)
          echo "Wrong answer. Aborting.."
          exit 1
          ;;
     esac
}

function setup_launcher {
     echo
     print_centered "-" "-"
     echo
     print_centered "Choose one of these launcher"
     echo
     print_centered "1. Rofi                    "
     print_centered "2. Dmenu                   "
     echo
     choice_centered "Choose launcher:"
     echo
     case $choice in
          1)
          sudo apt install rofi
          ;;
          2)
          sudo apt install dmenu
          ;;
          *)
          echo "Wrong answer. Aborting.."
          exit 1
          ;;
     esac
}

function setup {
     setup_wm
     setup_bar
     setup_launcher
     echo
     print_centered "-" "-"
     print_centered "The setup has been successfully set up all of your ricing"
     print_centered "purposes"
     echo
     choice_centered "Press the Enter key to exit. "
     exit 0
}

clear
print_centered "-" "-"
echo
print_centered ",-,"
print_centered "-----------"
print_centered "/...........\\" 
print_centered "/.............\\" 
print_centered "(=================)"
print_centered "|+++++++++++++|" 
print_centered "<&|++++ --- ++++|&>" 
print_centered "|++++ --- ++++|" 
print_centered "|++++ --- ++++|" 
print_centered "\\+++++++++++++/" 
print_centered "-------------" 
print_centered "v         v" 
echo
print_centered "Welcome to Rice Cooker (Alpha)"
print_centered "A quick and easy tool for your ricing purposes"
echo
print_centered "-" "-"
echo
print_centered "The setup will setting up all of your ricing purposes."
print_centered "Are you sure do you want to continue?"
choice_centered "[Y/n]"

if [[ $(echo ${choice} | tr '[:upper:]' '[:lower:]') == "y" ]]; then
setup
else echo "Aborting.."
exit 1
fi
