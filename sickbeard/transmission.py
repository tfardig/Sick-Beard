import sickbeard

from sickbeard import logger

import json
import urllib2

def sendTorrent(torrent):
    data = {
        arguments: {
            "download-dir": sickbeard.TRANSMISSION_DOWNLOAD_DIR,
            "filename": torrent.url
        },
        method: "torrent-add"
    }

    data = json.dumps(data)
    url = sickbeard.TRANSMISSION_HOST + '/transmission/rpc'

    req = urllib2.Request(url, data, {'Content-Type: application/json'})
    f = urllib2.urlopen(req)
    response = f.read()
    f.close()