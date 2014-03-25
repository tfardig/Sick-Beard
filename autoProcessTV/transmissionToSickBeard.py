#!usr/bin/python

import os

tvDownloadFolder = '/volume1/downloads/tv/complete'
movieDownloadFolder = '/volume1/downloads/movies/complete'

def isTvDirectory(directory):
    return directory.startswith(tvDownloadFolder)

def isMovieDirectory(directory):
    return directory.startswith(movieDownloadFolder)

def torrent_completed(torrentDir, torrentName):
    if isTvDirectory(torrentDir):
        notify_sickbeard(torrentDir)
    elif notify_couchpotato(torrentDir):
        notify_couchpotato(torrentDir)

def notify_sickbeard(torrentDir):
    print 'Notified sickbeard: ' + torrentDir

def notify_couchpotato(torrentDir):
    print 'Notified couchpotato: ' + torrentDir

if __name__ == '__main__':
    torrentDir = os.getenv('TR_TORRENT_DIR')
    torrentName = os.getenv('TR_TORRENT_NAME')
    
    torrent_completed(torrentDir, torrentName)