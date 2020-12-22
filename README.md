# ASX Announcements Discord Bot

> :exclamation: If you use this project in anyway, make sure to let me know on Twitter [@NiallGillmor](https://twitter.com/NiallGillmor). Always keen to get involved in anything related to the intersection of programming and the financial markets.

## To-Do

- [ ] Add config file.
- [ ] Parse date.
- [ ] Spice up embed.
- [ ] Seperate announcements for different stocks into different channels.
- [ ] Get company logo for embed.
- [x] Add database and store unqiue.
- [x] Create new table if that company does not already exist.
- [x] Discord bot.

## Personal Project Learnings

- Management of multiple Python installations on personal device and addressing installation conflicts with Homebrew.
- python-discord-webhook module is not async, thus unsuitable for large amounts of Discord webhooks as rate limited.
- Can utilise discord.py to send webhooks without having associated authentication with a bot.
