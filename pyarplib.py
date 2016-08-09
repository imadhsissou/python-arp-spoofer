#! /usr/bin/env python
import re
  
banner = """  _____ __     __        _____   _____  
 |  __ \\\ \   / / /\    |  __ \ |  __ \  Pyarp Copyright (C) 2016 Imad Hsissou
 | |__) |\ \_/ / /  \   | |__) || |__) | [imad.hsissou@gmail.com]
 |  ___/  \   / / /\ \  |  _  / |  ___/  [https://github.com/7bisso]
 | |       | | / ____ \ | | \ \ | |      {version : beta}
 |_|       |_|/_/    \_\|_|  \_\|_|      

\033[1;91m			[!] Legal disclaimer: 
Usage of Pyarp for attacking targets without prior mutual consent is illegal.\033[1;m

Type "help", "?" or "license" for more information.
Type "man" for full documentation.
"""

regex_net = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/([0-9]|[1-2][0-9]|3[0-2]))$"
regex_ip = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
regex_mac = "^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"

def pyarp_banner():
	return banner

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

