from setuptools import setup

setup(
    name = "pyarp",
    packages = ["pyarp"],
    entry_points={
          'console_scripts': [
              'pyarp = pyarp.__main__:main'
          ]
      },
    version = '0.1.1',
    license='MIT',
    description = "A user-friendly ARP spoofing tool",
    author = "Imad Hsissou",
    author_email = "imad.hsissou@gmail.com",
    url = "https://github.com/7BISSO/python-arp-spoofer",
    download_url = "https://github.com/7BISSO/python-arp-spoofer/raw/master/dist/pyarp-0.1.1.tar.gz",
    keywords = ['arp', 'scapy'],
    include_package_data=True,
    install_requires=[
	"scapy",
	"netifaces"
    ],
    )
