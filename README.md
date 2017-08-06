# shaynman
[Shaynman](http://t.me/ShaynmanBot) : SNU + Feynman, 서울대 물리학과 공지/강의게시판 알리미.

## Requirements
`requests`, `python-telegram-bot`, `schedule` module.
```bash
sudo pip3 install requests python-telegram-bot schedule
```

## Setup
- Create a telegram bot with [BotFather](http://t.me/BotFather), and get your bot's token.
- Get your server on Central Europe. [More on appropriate server location](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Performance-Optimizations#server-location)

```bash
git clone https://github.com/seungwonpark/shaynman
cd shaynman
nano token.txt
(YOUR_BOT_TOKEN)
^X - Y - ENTER
python3 initialize.py
screen
python3 shaynman.py
^A D
screen
python3 parser.py
^A D
```

## License
MIT
