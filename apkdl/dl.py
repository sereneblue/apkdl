from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import requests

APPS = []

def download(link):
	res = requests.get(link + '/download?from=details', headers={
			'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.5'
		}).text
	soup = BeautifulSoup(res, "html.parser").find('a', {'id':'download_link'})
	if soup['href']:
		r = requests.get(soup['href'], stream=True, headers={
			'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.5'
		})
		with open(link.split('/')[-1] + '.apk', 'wb') as file:
			for chunk in r.iter_content(chunk_size=1024):
				if chunk:
					file.write(chunk)

def search(query):
	res = requests.get('https://apkpure.com/search?q={}&region='.format(quote_plus(query)), headers={
			'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.5'
		}).text
	soup = BeautifulSoup(res, "html.parser")
	for i in soup.find('div', {'id':'search-res'}).findAll('dl', {'class':'search-dl'}):
		app = i.find('p', {'class':'search-title'}).find('a')
		APPS.append((app.text,
					i.findAll('p')[1].find('a').text,
					'https://apkpure.com' + app['href']))