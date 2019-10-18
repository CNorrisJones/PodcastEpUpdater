#!/bin/bash
echo $discord_url
cd /mnt/c/Users/Chris\ Norris-Jones/Desktop/Projects/virtenv/discordpodupdate/bin
.  ./activate
cd ../../../PodcastEpUpdater
python3 episodeupdate.py --web $discord_url
deactivate