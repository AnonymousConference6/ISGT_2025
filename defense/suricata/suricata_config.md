## Installation
sudo apt update && sudo apt upgrade -y \
sudo apt install -y software-properties-common \
sudo add-apt-repository -y ppa:oisf/suricata-stable \
sudo apt update \
sudo apt install -y suricata \
suricata --build-info \
sudo suricata-update \
suricata-update update-sources \
sudo ln -s /var/lib/suricata/rules /etc/suricata/rules

## Configuration
Suricate rules can be found under /usr/share/suricata/rules. You can copy them to /etc/suricata.

Edit the following changes on /etc/suricata/suricata.yaml \
Configure HOME_NET variable \
Configure the interface interface and pcap under af-packet. \
Set community-id to true. \
By default, rules for Modbus come with disabled. You need to activate them. \
The rules file in under /var/lib/suricata/rules.

## Test the rule set
To test suricata configuration"\
sudo suricata -T -c /etc/suricata/suricata.yaml -v \
A sample output is "1 rule files processed. 42870 rules successfully loaded, 0 rules failed, 0"

## Run Suricata in console mode
sudo suricata -c /etc/suricata/suricata.yaml -i enp0s8

## Analyze Logs
Logs can be found \
sudo tail -f /var/log/suricata/fast.log
