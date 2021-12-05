# hive-block-explorer
Block Explorer for the Hive Blockchain written in Python

For now, it just displays the contens of a post as if you would see it in the HiveBlocks website minus the replies, votes and other stuff.

# Installation
On Windows you could install Git to run the following command or download as Zip from the Github page and extract it.
If you are on Linux the following command is recommended.

In a Command Prompt or Terminal window type:

`git clone https://github.com/CesarPazzi/hive-block-explorer`

This will download and extract the files in a folder called hive-block-explorer.

## Python 3
You have to install Python 3 and PIP (on Windows, PIP comes with Python installation, and on Linux, in mosts distros, Python 3 and PIP comes preinstalled). And have to install the following Python Libraries using PIP:

* jsonrpc_requests
* PyQt5

## PIP
There's a requirements.txt file included in this repository to ease the installation of the required Python Libraries.
On Windows, you could run `setup.cmd` to install the libraries using PIP or if it fails or don't want to run the file, you could type the following command on a Command Prompt window or a Terminal window on Linux.

`pip install -r requirements.txt`

# Uninstallation
Once you are done, and want to remove it from your computer, you only have to delete the folder that generate the `git` command or where you extract the Zip file.