
import click
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

@click.command()
@click.option('-u',help='the url you want to parse')
@click.option('-o',help='writing to file')

def main(u,o):

	links = set()
	def urlParser(url, links):
	    html = requests.get(url).text
	    htmlSoup = BeautifulSoup(html, 'html.parser')
	    links.add(url)

	    for link in htmlSoup.find_all("a"):
	        linkUrl = link.get('href')
	        if linkUrl is None:
	            continue
	        fullUrl = urljoin(url, linkUrl)
	        if fullUrl in links:
	            continue
	        leng=len(links)
	       
	        print(leng, fullUrl)
	        urlParser(fullUrl, links)
	urlParser(u, links)

	# writing to file
	def write_file(o, links):
	    with open(str(o), 'wt') as f:
	        for pUrl in links:
	            f.write(pUrl + os.linesep)
	write_file(o, links)

if __name__ == '__main__':
	main()
