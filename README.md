# AnsiBot

AnsiBot is a simple, fast, expandable open-source Python IRC Bot!

## Getting AnsiBot

There are currently only one brance for this repository:
 - **master** *(stable)*: This branch contains stable, tested code. This is the branch you should be using if you just want to run your own AnsiBot! [![Build Status](https://travis-ci.org/infrascloudy/AnsiBot.svg?branch=master)](https://travis-ci.org/infrascloudy/AnsiBot)
 
New releases will be pushed to **master** whenever we have a stable version to release. This should happen on a fairly regular basis, so you'll never be too far behind the latest improvements.

## Installing AnsiBot

Firstly, AnsiBot will only run on **Python 3.4 or higher**. Because we use the asyncio module, you will not be able to use any other versions of Python.

To install AnsiBot on *nix (linux, etc), see [here](https://github.com/infrascloudy/AnsiBot/wiki/Installing-on-*nix)

### Running AnsiBot

Before you run the bot, rename `config.default.json` to `config.json` and edit it with your preferred settings. You can check if your JSON is valid using [jsonlint.com](http://jsonlint.com/)!

Once you have installed the required dependencies and renamed the config file, you can run the bot! Make sure you are in the correct folder and run the following command:

```
python3 -m cloudbot
```

Note that you can also run the `cloudbot/__main__.py` file directly, which will work from any directory.
```
python3 CloudBot/cloudbot/__main__.py
```
Specify the path as /path/to/repository/cloudbot/__main__.py, where `cloudbot` is inside the repository directory.

## Running with supervisor in a virtual environment

If you have a virtual environment setup (suggested you use this method)
```
cat /etc/supervisor/supervisord.conf
[program:ansibot]
directory=/srv/ansibot/public
command=/srv/ansibot/private/ansibot/bin/python3 -m cloudbot
environment=PATH="/srv/ansibot/private/ansibot/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
autostart=true
autorestart=true
```

### Documentation

The AnsiBot documentation is currently somewhat non existing. If you need any help, please log an issue here, and we will be happy to assist you.

### Support

If you think you have found a bug/have an idea/suggestion, please **open an issue** here on Github.

AnsiBot is **licensed** under the **GPL v3** license. The terms are as follows.

![GPL V3](https://www.gnu.org/graphics/gplv3-127x51.png)
    
    AnsiBot

    Copyright © 2011-2017 Allan Swanepoel / InfrasCloudy

    AnsiBot is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    AnsiBot is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with AnsiBot.  If not, see <http://www.gnu.org/licenses/>.
