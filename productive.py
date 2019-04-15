#!/usr/local/bin/python3.7

# from site_blocker import block_sites
import subprocess

quit_apps = [
    "Discord",
    "Steam",
    "Firefox Developer Edition"
]

for app in quit_apps:
    subprocess.call(['osascript', '-e', 'tell application "{}" to quit'.format(app)]) #AppleScript quit app call


subprocess.call(['osascript', '-e', """
                                    tell application "Swipes" to launch
                                    tell application \"Firefox Developer Edition\"
                                       activate
                                       open location "https://drive.google.com"
                                    end tell
                                    """])

if __name__ == "__main__":
    pass