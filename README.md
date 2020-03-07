# RDB
discord bot for setting up 5v5 csgo scrims

1. Set up bot account for the discord you want it on through the
   discord developer portal

2. Add your bots api key to your environment variables as DISCORDAPI (using
   your .bashrc file or other shell config file)
   for bash:
      add ```export DISCORDAPI=<your_token>``` to .bashrc file
   for fish:
      add ```set -gx DISCORDAPI <your_token>``` to config.fish file, usually in
      your .config/fish/ directory

3. you will need python3 and pip3, using pip3 install discord.py and bs4 as
   well as any other libraries you dont have.

4. after cloning you should now be able to run ```python3 rdb.py```
