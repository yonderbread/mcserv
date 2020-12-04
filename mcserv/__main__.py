import os

from .fetch import get_all_versions, get_version, install
from .term import list_versions, show_download
import sys

if __name__ == '__main__':
    try:
        args = sys.argv[1:]
        action = args[0].lower()
        flags = args[1:]

        snapshots = False
        releases = False

        eula_agree = False

        if '-s' in flags:
            snapshots = True
        if '-r' in flags:
            releases = True

        if '--agree-eula' in flags:
            eula_agree = True

        if action == 'list':
            versions = get_all_versions(releases, snapshots)
            print(list_versions(versions))

        elif action == 'show':
            version = get_version(flags[0])
            if not version:
                print(flags[0] + ' is not a valid version.')
                print('Try `mcserv list -r -s` for a list of available versions.')
                sys.exit()

            print(show_download(version.get_download()))

        elif action == 'install':
            version = get_version(flags[0])
            path = ' '.join(i for i in flags[1:] if i not in ('-s', '-r', '--agree-eula'))
            if not version:
                print(flags[0] + ' is not a valid version.')
                print('Try `mcserv list -r -s` for a list of available versions.')
                sys.exit()

            print('Installing Minecraft server version ' + version.id)

            install(version.get_download(), path, agree_eula=eula_agree)

    except IndexError:
        print('Invalid syntax.')
