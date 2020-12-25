# ASX Announcements Discord Bot

:exclamation: If you find this project helpful in any way, let me know on Twitter [@NiallGillmor](https://twitter.com/NiallGillmor)!

## Description

Lightweight discord webhook intended to be run on schedule to post webhooks to a specific Discord channel alerting new ASX announcements for a set watchlist.

## Installation

1. Download or clone the repo.
2. `pip install` the dependancies/requirements listed below.
3. Add the tickers of the companies you wish to watch to the example.config.ini file as show below.
   <img align="center" src="https://i.imgur.com/7OhZHlO.png">
4. Create a webhook in the Discord channel you wish to post announcements to. Follow [this](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) guide on how to create a webhook.
5. Using the newly created webhook URL, set the id and token in the example.config.ini file. Your ID and token are taken from the webhook URL as follows: `https://discord.com/api/webhooks/`id`/`token.
6. Save your changes to the example.config.ini file and rename the newly saved example.config.ini file to `config.ini`.
7. Run the main.py script.

### Dependencies/Requirements

- requests
- json
- sqlite3
- discord
- configparser
- datetime

## To-Do

- [x] Clean up code.
- [x] Add details of installation and setup to README
- [x] Tool to get company's Xids, https://asx.api.markitdigital.com/asx-research/1.0/search/price?itemsPerPage=1&page=0&searchText=eml, check that symbol item is equal to code, then add it in.
- [x] Add config file.
- [x] Parse date.
- [x] Spice up embed.
- [x] Customise pfp and other elements of bot through code.
- [x] Add database and store unqiue.
- [x] Create new table if that company does not already exist.
- [x] Discord bot.
- [x] Fix dynamic embed colour.
- [x] Add ticker/company identify to message for stacked continuous messages.

## Suggested Features

- [x] On first run, populate database without posting Discord messages for every past announcement.
- [ ] Seperate announcements for different stocks into different channels.

## Personal Project Learnings

- Management of multiple Python installations on personal device and addressing installation conflicts with Homebrew.
- python-discord-webhook module is not async, thus unsuitable for large amounts of Discord webhooks as rate limited.
- Can utilise discord.py to send webhooks without having associated authentication with a bot.
- Using the configparser module.
- Formatting usable READMEs.

## Contact Me

<p align="center"><img align="center" src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/master/svgs/brands/twitter.svg" alt="Twitter" width="20"> <a href="https://twitter.com/NiallGillmor">@NiallGillmor</a></p>
