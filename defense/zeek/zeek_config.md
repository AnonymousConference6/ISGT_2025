## Installation
sudo apt install -y cmake make gcc g++ flex bison libpcap-dev libssl-dev python3 python3-dev python3-pip zlib1g-dev libmaxminddb-dev liblzma-dev libsqlite3-dev libjemalloc-dev curl \
echo 'deb http://download.opensuse.org/repositories/security:/zeek/xUbuntu_22.04/ /' | sudo tee /etc/apt/sources.list.d/security:zeek.list \
curl -fsSL https://download.opensuse.org/repositories/security:zeek/xUbuntu_22.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/security_zeek.gpg > /dev/null \
sudo apt update \
sudo apt install zeek

Zeek is installed at /opt/zeek\
echo 'export PATH=/opt/zeek/bin:$PATH' >> ~/.bashrc \
source ~/.bashrc \
zeek --version

cat /opt/zeek/etc/node.cfg

## Configuration
Change the interface at /opt/zeek/etc/node.cfg
In my case, it is enp0s8 \

## Start and Restart Commands
sudo /opt/zeek/bin/zeekctl deploy \
sudo /opt/zeek/bin/zeekctl status \
sudo /opt/zeek/bin/zeekctl restart

## Log Analysis
Logs are found under /opt/zeek/logs/current

## Enable Modbus Related Rules
sudo nano /opt/zeek/share/zeek/site/local.zeek \
@load protocols/modbus/track-memmap.zeek \
Then, run this again: sudo /opt/zeek/bin/zeekctl deploy
