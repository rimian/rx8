# RX8

This is for repurposing the RX8 satelite navigation to run engine parameters on a Raspberry PI.

This is a huge job. Make yourself a coffee!

## What you need to do

You'll need the following equipment:

* An OBDII bluebooth adapter
* A Raspberry PI
* A 7 inch screen.

## Required packages

```
sudo apt-get install netcat-openbsd
```

## Installation

* SSH into your Raspberry PI.
* In the home directory checkout this repo.
* Add the auto start section of wayfire.ini to your config

## Pulling things apart

In my case, my RX8 did not have a satelite navigation system installed so, I bought an entire using off eBay. I recommend using a second hand screen and swapping it out later. There's a lot of stuff to pull apart and it will take you a long time. If you have a spare, you can work on it and then swap it out of your car later. If not, go right ahead and pull out your centre console.

Here's some instructions I found on doing that: https://newscrewdriver.com/2023/08/06/removing-navigation-lcd-assembly-from-2004-mazda-rx-8/

## Booting up the Rasberry PI in Kiosk Mode

The easiest example I found so far: https://core-electronics.com.au/guides/raspberry-pi-kiosk-mode-setup/#V1Y5SSB using Wayland config.

To get the display to be full screen, you need to boot the app in kiosk mode. I got this working with wayland. Add this to wayfire.ini

```
[autostart]
screensaver = false
dpms = false
kiosk = /home/pi/rx8/run_kiosk.sh
```
## Fitting a new screen

I've seen some other guides recommend hot gluing a tablet or screen in place of the old one. I don't think hot glue will hold through the extreme heat cycles inside a car, the vibrations and pushing on it with your finger.

The best way to fit a replacement screen is to reuse the metal brackets that mount the old screen. Thankfully, the old screen seems to be a standard 16:9 and a new screen (without a cover) should be an easy fit.

## Connecting

```sudo rfcomm```

