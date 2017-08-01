# shaynman
[Shaynman](http://t.me/ShaynmanBot) : SNU + Feynman, 서울대 물리학과 공지/강의게시판 알리미.

## Requirements
`requests`, `python-telegram-bot` module.
```bash
sudo pip3 install requests python-telegram-bot
```

## Setup
- Create a telegram bot with [BotFather](http://t.me/BotFather), and get your bot's token.
- Get your server on Central Europe. [More on appropriate server location](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Performance-Optimizations#server-location)

```bash
git clone https://github.com/seungwonpark/shaynman
cd shaynman
python3 initialize.py
nohup `python3 shaynman.py` & # Should be operating on background
sudo crontab -e
*/10 * * * * /usr/bin/python3 parser.py # Parse boards and send messages for every 10 minutes.
```

## License
MIT
