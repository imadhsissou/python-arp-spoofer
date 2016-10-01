import re
  
banner = """  _____ __     __        _____   _____  
 |  __ \\\ \   / / /\    |  __ \ |  __ \  [Author : Imad Hsissou]
 | |__) |\ \_/ / /  \   | |__) || |__) | [Author email : imad.hsissou@gmail.com]
 |  ___/  \   / / /\ \  |  _  / |  ___/  [https://github.com/7bisso]
 | |       | | / ____ \ | | \ \ | |      [version 0.1.1]
 |_|       |_|/_/    \_\|_|  \_\|_|      

\"Usage of Pyarp for attacking targets without prior mutual consent is illegal.\"

Type "help", "?" or "license" for more information.
Type "man" for full documentation.
"""

license = """
MIT License

Copyright (c) 2016 Imad Hsissou

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

manual="""			   _____MAN PAGE_____

NAME
	pyarp  - a friendly command-line spoofing tool wrriten in python.

COMMANDS

	iface - 
			iface <interface name>
			Manually set your network interface
			'eth0' is set as default.

	inet  - 
			inet [option]
			options :
				AF_INET : IP information
				AF_LINK : MAC information
				Type "inet" for both.

	getmac - 
			getmac <host ip address>
			Get host MAC address.

	scan - 
			scan <network>, eg {scan 192.168.1.0/24}
			Map your network.

	spoof - 
			spoof <target> <target>
			Launch MITM/ARP spoofing attack.
			press Ctrl+C to stop.

	help  - 
			help [command]
			display information about a command.

	clear - clear screen

	exit  - close pyarp, press Ctrl+D for clean exit
			press Ctrl+C for forced exit.

NOTICE

	IPv6 is not supported Yet.
"""

regex_net = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/([0-9]|[1-2][0-9]|3[0-2]))$"
regex_ip = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
regex_mac = "^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"

def pyarp_banner():
	return banner

def pyarp_license():
	return license

def pyarp_manual():
	return manual

def regex(exp,regexp):
	if regexp == 'net':
		check = re.compile(regex_net)
		match = check.match(exp)
		return match

	elif regexp == 'ip':
		check = re.compile(regex_ip)
		match = check.match(exp)
		return match

	elif regexp == 'mac':
		check = re.compile(regex_mac)
		match = check.match(exp)
		return match

	else:
		return False


