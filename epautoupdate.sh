#!/bin/bash
cd ~/Projects/virtenvs/discordpodupdate/bin
.  ./activate
cd ../../../PodcastEpUpdater
python3 episodeupdate.py --web $discord_url
deactivate