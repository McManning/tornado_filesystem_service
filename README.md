tornado_filesystem_service
==========================

## What is this, even?

This is a simple weekend project to implement a lightweight web interface for some basic file management utilities.
This performs the following functions:
* Displaying user configurable virtual root directories mapped to any number of drives and subfolders on the actual machine
* Listing files and folders in a directory
* Renaming files within a directory
* Moving files between directories
* Providing user configurable suggestions for target directories when moving files (eg: Suggesting video files move to a media drive)

## Dependencies
* [Tornado Web Service](http://www.tornadoweb.org/)
* Python 2.7+ (3.0 Support untested, but probably doesn't work)
* [Twitter Bootstrap](http://twitter.github.com/bootstrap/index.html) - But it's just pulling files directly from their github, so don't worry about that one for now :P

## Installation
* Have Tornado in Python's path
* Run service.py
* Check http://localhost:50006/browse/ 
* That's it!

This has been tested under Windows 7, and a random Debian VPS.

## Configuration
Edit *filesystem.ini* to your liking, it should be relatively straight forward.

## License
The "Do whatever you want with it, I don't care" one.

## Todo
* Implement the actual rename/move requests after the user has selected a target
* Ability to rename folders

