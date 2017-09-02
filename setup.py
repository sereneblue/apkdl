from setuptools import setup, find_packages
from apkdl import __version__
import os

setup(
	name ='apkdl',
	version = __version__,
	description = 'Search and download APKs from the command line',
	url = 'https://github.com/sereneblue/apkdl',
	author = 'sereneblue',
	license = "MIT",
	packages = find_packages(),
	classifiers = [
		'Intended Audience :: Developers',
		'Environment :: Console',
		'Topic :: Utilities',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
	],
	keywords = ['android', 'apk', 'cli'],
	install_requires = ['requests', 'beautifulsoup4'],
	entry_points = {
		'console_scripts':[
			'apkdl=apkdl.__main__:main'
		],
	}
)
