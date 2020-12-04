import requests
import os
import tqdm

VERSION_INDEX_URL = 'https://launchermeta.mojang.com/mc/game/version_manifest.json'


class ServerVersionDownload:
    def __init__(self, version_id: str, downloads: dict):
        if not downloads:
            raise FileNotFoundError('Unable to request version data.')

        self.version_id = version_id
        self.url = None
        self.hash = None
        self.size = None

        if 'server' in downloads:
            server_dl = downloads['server']
            for k, v in server_dl.items():
                if k == 'size':
                    self.size = v
                if k == 'sha1':
                    self.hash = v
                if k == 'url':
                    self.url = v


class Version:
    def __init__(self, version_id: str, version_type: str, version_url: str):
        self.id = version_id
        self.type = version_type
        self.url = version_url

    def get_download(self):
        with requests.get(self.url) as req:
            req.raise_for_status()
            data = req.json()
            return ServerVersionDownload(self.id, data.get('downloads'))


def get_all_versions(include_releases=True, include_snapshots=True, _ignore=('old_alpha', 'old_beta')):
    entries = []
    with requests.get(VERSION_INDEX_URL) as req:
        req.raise_for_status()
        data = req.json()
        versions = data['versions']
        for version in versions:
            if not include_snapshots and version['type'] == 'snapshot':
                continue
            if not include_releases and version['type'] == 'release':
                continue
            if version['type'] in _ignore:
                continue
            entries.append(Version(version['id'], version['type'], version['url']))
    return entries


def get_version(version_id: str):
    entries = get_all_versions()
    for version in entries:
        if version.id == version_id:
            return version


def install(download: ServerVersionDownload, dirpath: str, agree_eula: bool = False, filename: str = None, _ch_size: int = 1024):
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

    filename = download.version_id + '.jar' if filename is None else filename
    path = os.path.join(dirpath, filename)
    url = download.url
    filesize = download.size

    if agree_eula:
        print('By creating a Minecraft server you agree to Mojang\'s End User License Agreement,')
        print('which can be found here: https://account.mojang.com/documents/minecraft_eula')

        eulapath = os.path.join(dirpath, 'eula.txt')
        with open(eulapath, 'w') as f:
            f.write('eula=true')
            f.close()

    progbar = tqdm.tqdm(total=filesize, unit_divisor=1000000)
    with open(path, 'wb') as f:
        with requests.get(url, stream=True) as req:
            for chunk in req.iter_content(chunk_size=_ch_size):
                progbar.update(len(chunk))
        f.close()

    print('Done! (Downloaded ' + str(filesize / 1000000) + ' mb)')
    print('Server location: ' + path)
