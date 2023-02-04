import os, platform

platformFinder = platform.system()

if platformFinder == "Windows":
    CHROME_PROFILE_PATH = r"user-data-dir=C:\Users\<username>\Name\Of\Folder\To\Store\Data"
else:
    CHROME_PROFILE_PATH = r"user-data-dir=/home/<username>/Name/Of/Folder/To/Store/Data"

# Windows 7, 8.1, and 10: C:\Users\<username>\AppData\Local\Google\Chrome\User Data\Default
# Mac OS X El Capitan: Users/<username>/Library/Application Support/Google/Chrome/Default
