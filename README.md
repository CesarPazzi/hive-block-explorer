# hive-block-explorer
Block Explorer for the Hive Blockchain written in Python

For now, it just displays the contens of a post as if you would see it in the HiveBlocks website minus the replies, votes and other stuff.

# Installation
On Windows you could install Git to run the following command or download as Zip from the Github page and extract it.
If you are on Linux the following command is recommended.

In a Command Prompt or Terminal window type:

`git clone https://github.com/CesarPazzi/hive-block-explorer`

This will download and extract the files in a folder called hive-block-explorer.

## Installation
You will need Python 3 (most Linux distros already come with Python preinstalled) to begin.
Hive Block Explorer uses 2 Python libraries for working properly:

* jsonrpc_requests
* PySide6

You can setup a Virtual Environment or run `setup.cmd` to install the libraries in your local Python installation. Basically this `setup.cmd` will call `pip install -r requirements.txt` command and install the required libraries with the proper versions.

## Uninstallation
If you set a Virtual Environment, you can simply delete the folder you cloned with `git` command.
If you will not use the libraries mentioned above, you can uninstall them running the command `pip uninstall -r requirements.txt` it will only uninstall the libraries and not the dependencies if any.