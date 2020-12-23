# ASX Announcements Discord Bot

> :exclamation: If you use this project in anyway, make sure to let me know on Twitter [@NiallGillmor](https://twitter.com/NiallGillmor). Always keen to get involved in anything related to the intersection of programming and the financial markets.

## To-Do

- [x] Tool to get company's Xids, https://asx.api.markitdigital.com/asx-research/1.0/search/price?itemsPerPage=1&page=0&searchText=eml, check that symbol item is equal to code, then add it in.
- [x] Add config file.
- [ ] Clean up code structure.
- [ ] Parse date.
- [ ] Spice up embed.
- [ ] Seperate announcements for different stocks into different channels.
- [ ] Get company logo for embed.
- [ ] Add details of installation and setup to README
- [ ] Customise pfp and other elements of bot through code.
- [x] Add database and store unqiue.
- [x] Create new table if that company does not already exist.
- [x] Discord bot.

## Personal Project Learnings

- Management of multiple Python installations on personal device and addressing installation conflicts with Homebrew.
- python-discord-webhook module is not async, thus unsuitable for large amounts of Discord webhooks as rate limited.
- Can utilise discord.py to send webhooks without having associated authentication with a bot.
- Using the configparser module.
