try:
	from setuptools import setup
except ImportError:
	from disutils.core import setup

config = {
	'description' : 'Generative Chatbot Spanish',
	'author' : 'Evil-AI',
	'url' : 'www.evil-ai.com',
	'download_url' : 'None',
	'author_email' : 'root.evil.ai@gmail.com',
	'version' : '0.1',
	'install_requires' : ['nose'],
	'packages' : ['NAME'],
	'scripts' : [],
	'name' : 'ParlEs'
}

setup(**config)