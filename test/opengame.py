

import random


BrowserID = random.randint(10000000000, 99999999999)

#somehow this opens up a roblox session 
webbrowser.open(f"roblox-player:1+launchmode:play+gameinfo:{Gamesession}+launchtime:{int(time()*1000)}+placelauncherurl:https%3A%2F%2Fassetgame.roblox.com%2Fgame%2FPlaceLauncher.ashx%3Frequest%3DRequestGame%26browserTrackerId%3D{BrowserID}%26placeId%3D{PlaceId}%26isPlayTogetherGame%3Dfalse+browsertrackerid:{BrowserID}+robloxLocale:en_us+gameLocale:en_us")