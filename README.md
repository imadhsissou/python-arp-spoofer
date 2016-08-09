# Pyarp

[![pyarp | beta](https://img.shields.io/badge/pyarp-beta-brightgreen.svg)](https://github.com/7BISSO/Pyarp) [![python](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/download/releases/2.7/)
[![scapy](https://img.shields.io/badge/scapy-2.x-blue.svg)](https://github.com/secdev/scapy/)
[![linux](https://img.shields.io/badge/os-linux-orange.svg)](https://www.linux.com/)
[![MIT](https://img.shields.io/badge/licence-MIT-red.svg)](https://github.com/7BISSO/Pyarp/blob/master/LICENSE)

Pyarp is a simple pen testing tool wrriten in python, it intercepts packets on a switched LAN by forging ARP replies, it comes with a line-oriented command interpreter, autocomplete feature and commands history.


![Imgur](http://i.imgur.com/PxiEcZ4.png)


## Dependencies  

* [python 2.7](https://www.python.org/download/releases/2.7/)
* [scapy 2.x](http://www.secdev.org/projects/scapy/doc/installation.html)
* [netifaces](https://bitbucket.org/al45tair/netifaces)  

The fastest way to install `netifaces` is to use `easy_install` module :

```
$ apt-get install python-setuptools
$ easy_install netifaces
```

## Documentation  

Type `help [command]` to display information about a command, or check the [man page](https://github.com/7BISSO/Pyarp/blob/master/man-page) for full documentation.

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
Launch MITM attack (Ctrl + C to stop)
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

The contents of this repository is licensed under [MIT License](https://github.com/7BISSO/Pyarp/blob/master/LICENSE).
