# mcserv

Just a little cli module I wrote when I was bored and 
felt like making something useful. This utility will
list vanilla Minecraft server versions, give information on
individual versions, and most importantly, install
them.

## Usage:
```
# ~ INSTALLATION ~
git clone https://github.com/yonderbread/mcserv.git
cd mcserv
python -m pip install -r requirements.txt # installing dependencies
python setup.py install # install mcserv package to local repo
cd ..
rm -rf mcserv # optional; delete git repo since it's not needed anymore

# ~ LIST AVAILABLE VERSIONS ~
mcserv list -r # releases only
mcserv list -r -s # snapshots included

# ~ VIEW VERSION INFO ~
mcserv show 1.16.4
mcserv show 1.12.2

# ~ SET UP SERVER FOLDER ~
mcserv install 1.16.4 /home/me/mc_server # create 1.16.4 server folder in home directory
# ... with eula.txt generated
mcserv install 1.16.4 /home/me/mc_server --agree-eula # automatically changes eula=false to eula=true in eula.txt file
```
