# 4chan-ripper
[![Python 3.9+](https://upload.wikimedia.org/wikipedia/commons/4/4f/Blue_Python_3.9%2B_Shield_Badge.svg)](https://www.python.org)
[![License: GPL v3](https://upload.wikimedia.org/wikipedia/commons/8/86/GPL_v3_Blue_Badge.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)

Tool for ripping and saving the media files in 4chan threads.

## Usage
```
usage: 4cr [-h] [-b board_id] [-i] [-s] [--out output_directory] [urls ...]

4cr CLI

positional arguments:
  urls                  the urls to process

optional arguments:
  -h, --help            show this help message and exit
  -b board_id           The short id of the board to target. Ignored if the program was not started in interactive mode. Default is hr
  -i                    Causes the archive file to get ignored. Only applicable in interactive mode.
  -s                    Treat the input urls as a photoset to rip
  --out output_directory
                        The output directory. Default is ~/Public
```