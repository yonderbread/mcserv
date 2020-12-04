# mcserv

Just a little cli module I wrote when I was bored and 
felt like making something useful. This utility will
list vanilla Minecraft versions, give information on
individual versions, and most importantly, install
them.

## Usage:
```
# installation
python -m pip install -U https://github.com/yonderbread/mcserv.git

# listing all versions with and without snapshots included
mcserv list -r
mcserv list -r -s

# getting information about a specific version
mcserv show 1.16.4
mcserv show 1.12.2

# installing a server to a not-yet created path
# in my home folder
mcserv install 1.16.4 /home/me/mc_server
# ... with eula.txt generated
mcserv install 1.16.4 /home/me/mc_server --agree-eula
```