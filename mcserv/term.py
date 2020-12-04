from .fetch import get_version, get_all_versions, Version, ServerVersionDownload
from typing import List
from tabulate import tabulate


def list_versions(versions: List[Version]):
    rows = []
    for version in versions:
        rows.append((version.id, version.type, version.url))

    return tabulate(rows, headers=('Version', 'Type', 'Download URL'), tablefmt="fancy_grid")


def show_download(download: ServerVersionDownload):
    rows = [('Version', download.version_id), ('Download URL', download.url), ('SHA1 Hash', download.hash),
            ('Size (MB)', round(download.size / 1000000, 2))]
    return tabulate(rows, tablefmt="fancy_grid")
