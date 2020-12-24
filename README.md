# ASX Announcements Discord Bot

> :exclamation: If you use this project helpful in any way, let me know on Twitter [@NiallGillmor](https://twitter.com/NiallGillmor)!

## Description

Lightweight discord webhook intended to be run on schedule to post webhooks to a specific Discord channel alerting new ASX announcements for a set watchlist.

## To-Do

- [ ] Clean up code.
- [ ] Add details of installation and setup to README
- [x] Tool to get company's Xids, https://asx.api.markitdigital.com/asx-research/1.0/search/price?itemsPerPage=1&page=0&searchText=eml, check that symbol item is equal to code, then add it in.
- [x] Add config file.
- [x] Parse date.
- [x] Spice up embed.
- [x] Customise pfp and other elements of bot through code.
- [x] Add database and store unqiue.
- [x] Create new table if that company does not already exist.
- [x] Discord bot.

## Suggested Features

- [ ] Seperate announcements for different stocks into different channels.

## Personal Project Learnings

- Management of multiple Python installations on personal device and addressing installation conflicts with Homebrew.
- python-discord-webhook module is not async, thus unsuitable for large amounts of Discord webhooks as rate limited.
- Can utilise discord.py to send webhooks without having associated authentication with a bot.
- Using the configparser module.
- Requirements file.

## Contact Me

<p align="center"><img align="center" src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/master/svgs/brands/twitter.svg" alt="Twitter" width="20"> <a href="https://twitter.com/NiallGillmor">@NiallGillmor</a></p>
