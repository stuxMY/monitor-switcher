# Monitor Switcher

A simple Python 3 script that allows you to select which monitor should be the primary display using `xrandr`.

## Features
- Lists all connected monitors.
- Allows you to select which monitor to set as the primary display.
- Uses `xrandr` to switch the main display seamlessly.

## Prerequisites
- Python 3.x
- `xrandr` (Must be installed on your system)

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/stuxMY/monitor-switcher.git
   cd monitor-switcher

  ```python
python3 monitor.py or chmod +x monitor.py
  mv monitor.py /usr/bin/monitor



# For Ubuntu/Debian-based systems
sudo apt-get install x11-xserver-utils

# For Arch-based systems
sudo pacman -S xorg-xrandr

# For Fedora-based systems
sudo dnf install xrandr


# Example Output 

- Available Monitors:
- 1: HDMI-1
- 2: eDP-1
- 3: DP-1
- Select the monitor number to set as primary: 1
- Set HDMI-1 as the primary display.
