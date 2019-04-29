from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup


def details(movie):
	try:
		soup = BeautifulSoup(urlopen(movie['url']))
		movie['original_title'] = soup.findAll('dl')[0].dd.text
	except:
		pass

def estreias():
	soup = BeautifulSoup(urlopen('http://cinecartaz.publico.pt/Brevemente'))
	info = soup.findAll('section')[1]
	estreias = []
	res = {'title': info.h2.text, 'filmes': estreias }
	for li in info.ul.findAll('li'):
		filme = { 'url': 'http://cinecartaz.publico.pt' + li.a['href'], 'title': li.h3.text }
		estreias.append( filme )
	for movie in res['filmes']:
		details(movie)
	return res
	
