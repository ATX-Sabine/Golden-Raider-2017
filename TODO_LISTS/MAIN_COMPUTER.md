# Setup

- [ ] Flash Firmware to MicroSD Card (Raspbian Stretch)
- [ ] boot w/HDMI cable setup and USB hub to keyboard
- [ ] Change user pi password
- [ ] Connect to WiFi
- [ ] `sudo raspi-config`
  - [ ] set keyboard layout
  - [ ] set locale
  - [ ] enable SSH, I2C
  - [ ] change network name (golden-raider-mk2.local)
- [ ] `sudo apt-get update && sudo apt-get upgrade`
- [ ] reboot headless, ssh in
- [ ] add necessary users and privileges
  - [ ] Sabine_ATX
  - [ ] autopilot
  - [ ] Visitor
- [ ] Remove default `pi` user
- [ ] install necessary dependencies
  - [ ] python3, pip3, wiringpi