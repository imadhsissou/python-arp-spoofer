# Pyarp

Pyarp is a simple pen testing tool, written in python. It intercepts packets on a switched LAN by forging ARP replies. It comes with a line-oriented command interpreter, with autocomplete feature and commands history.

## Dependencies  

```
# apt-get install python-dev
# apt-get install setuptools
# apt-get install python-pip
```

## Installation
```
# pip install pyarp
```

## Documentation  

Type `help [command]` to display the information about a command, or check the [Manual](https://github.com/7BISSO/python-arp-spoofer/blob/master/pyarp/data/MANUAL.txt) for full documentation.

<b>Notice : the beta version doesn't support IPv6 yet.</b>


## Usage example  

Set your network interface (press \<tab\> to list all network interfaces)
```
pyarp>> iface wlan0
pyarp>>
```
Scan for connected hosts on LAN
```
pyarp>> scan 192.168.1.0/24
Begin emission:
**Finished to send 256 packets.
...
Received 5 packets, got 2 answers, remaining 254 packets

inet 192.168.1.0/24
iface wlan0

Host 1: MAC a4:7e:39:ab:fb:e0  IP 192.168.1.1
Host 2: MAC 00:0c:6e:da:49:ab  IP 192.168.1.4
pyarp>>
```
Launch MITM attack (Ctrl + C to terminate)
```
pyarp>> spoof 192.168.1.1 192.168.1.4

[+] Attack Launched.

.
Sent 1 packets.
.
Sent 1 packets.
^C
[+] Attack stopped, successful recover.

pyarp>>
```

## License  

The contents of this repository is licensed under [MIT License] (https://github.com/7BISSO/python-arp-spoofer/blob/master/LICENSE).
