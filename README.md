# four-chan-ripper
[![Python 3.11+](https://upload.wikimedia.org/wikipedia/commons/6/62/Blue_Python_3.11%2B_Shield_Badge.svg)](https://www.python.org)
[![License: GPL v3](https://upload.wikimedia.org/wikipedia/commons/8/86/GPL_v3_Blue_Badge.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)

Tool for ripping and saving the media files in 4chan threads.

## Installation
```bash
pip install four-chan-ripper
```

## Usage
```
usage: __main__.py [-h] [-b board_id] [-i] [-s] [-o output_directory] [urls ...]

4chan ripper CLI

positional arguments:
  urls                 the urls to process

options:
  -h, --help           show this help message and exit
  -b board_id          The short id of the board to target. Ignored if the program was not started in interactive mode. Default is hr
  -i                   Causes the archive file to get ignored. Only applicable in interactive mode.
  -s                   Treat the input urls as a photoset to rip
  -o output_directory  The output directory. Defaults to the current working directory.
```
Also installs a CLI alias called `4cr` which can be used to invoke the program directly