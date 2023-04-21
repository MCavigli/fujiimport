#!/usr/bin/env python3
'''Imports and organizes photos from an SD card'''
import os
import shutil


def makeFolder():
    '''Makes the temporary fuji folder if it doesn't
    already exist on the desktop'''
    rootfolder = '/Users/mcavigli/Desktop/fuji'
    jpgfolder = '/Users/mcavigli/Desktop/fuji/JPG'
    rawfolder = '/Users/mcavigli/Desktop/fuji/RAW'

    os.mkdir(rootfolder)
    os.mkdir(jpgfolder)
    os.mkdir(rawfolder)


def moveFiles(sdpath, jpgdest, rawdest):
    '''Moves the files from the source to the destination'''
    for filename in os.listdir(sdpath):
        if os.path.splitext(filename)[1] == ".jpg":
            sourcejpgfile = os.path.join(sdpath, filename)
            destjpgfile = os.path.join(jpgdest, filename)
            shutil.copy(sourcejpgfile, destjpgfile)
        elif os.path.splitext(filename)[1] == ".raf":
            sourcerawfile = os.path.join(sdpath, filename)
            destrawfile = os.path.join(rawdest, filename)
            shutil.copy(sourcerawfile, destrawfile)


def main():
    '''Variables that will be used in the final version'''
    sdpath = '/DCIM'
    destinationpath = '/Users/mcavigli/Desktop/fuji'
    jpgdestinationpath = '/Users/mcavigli/Desktop/fuji/JPG'
    rawdestinationpath = '/Users/mcavigli/Desktop/fuji/RAW'
    '''Variables for testing'''
    jpgdummydest = '/Users/mcavigli/Desktop/dummyfuji/JPG'
    rawdummydest = '/Users/mcavigli/Desktop/dummyfuji/RAW'
    dummydcim = '/Users/mcavigli/Desktop/dummyDCIM'

    '''Checks if the destination folder exists. Makes it if it doesn't'''
    if not os.path.exists(destinationpath):
        makeFolder()

    '''Scans through souce folder to see if there are any
    directories. If its files then it copies the files. If there
    are folders then it'll go through and copy the files in those folders.'''
    for items in os.listdir(dummydcim):
        print(items)
        if os.path.isdir(items):
            '''Still need to work on this part'''
            pass
        else:
            moveFiles(dummydcim, jpgdummydest, rawdummydest)

if __name__ == "__main__":
    main()
