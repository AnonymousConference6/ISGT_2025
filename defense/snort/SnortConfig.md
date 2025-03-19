## Update Your System (Linux Ubuntu)
sudo apt update && sudo apt upgrade -y

## Install Dependencies
sudo apt install -y build-essential libpcap-dev libpcre3-dev libdnet-dev zlib1g-dev luajit libluajit-5.1-dev libssl-dev bison flex libdaq-dev libdaq2

## Install Snort
sudo apt-get install snort -y

## Verify Installation
snort -V \
snort --version

## Snort Configuration
First, make sure your Virtual Box promiscuous mode setting is "Allow All" \
sudo ip link set <network_interface> promisc on \
The snort config file is under /etc/snort \
Arguably, the most important file is /etc/snort/snort.conf \
Copy of this file: cp /etc/snort/snort.conf /etc/snort/snort.conf.bak 

set your home network \
ipvar HOME_NET \<your_subnet\> \
Example: ipvar HOME_NET 192.168.1.0/24

By default, the rule path is /etc/snort/rules \
You can manually put your local signatures to /etc/snort/rules/local.rules 

## Run Snort
The below command verifies that the Snort configuration that is about to be used is valid and won't fail at run time. \
sudo snort -T -c /etc/snort/snort.conf -i <network_interface>

To start Snort \
sudo snort -A console -q -u snort -g snort -c /etc/snort/snort.conf -i <network_interface>
