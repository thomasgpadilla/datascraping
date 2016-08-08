from urllib2 import urlopen
from bs4 import BeautifulSoup
import requests

#point to FRUS volumes
html = urlopen("http://digicoll.library.wisc.edu/cgi-bin/FRUS/FRUS-idx?type=browse&scope=FRUS.FRUS1")
soup = BeautifulSoup(html, 'html.parser')

with open("frus_section_title.txt", "w") as file:

#scrape FRUS volume relative URLs 
	for links in soup.find_all("p", {"class":"isshead"}):

#prepend relative URLs with base URL
		for link in links.find_all('a'):
			volumeurl = 'http://digicoll.library.wisc.edu/' + link.get('href')

			volumeurls = requests.get (volumeurl)
			volumesoup=BeautifulSoup(volumeurls.content, 'html.parser')
			
#scrape FRUS volume section relative URLs
			for urls in volumesoup.find_all("p", {"class":"cntsitem"}):

#prepend relative URLs with base URL
				for url in urls.find_all('a'):
					pdfurl = 'http://digicoll.library.wisc.edu/' + url.get('href')

					pdfurls = requests.get (pdfurl)
					pdfsoup=BeautifulSoup(pdfurls.content, 'html.parser')

#visit each FRUS volume section page and scrape the PDF item citation data to a TXT file
					for pdfurls in pdfsoup.find_all("div", {"class":"contentshdr"}):
						for item in pdfurls.find_all('div', {"class":"itemmd"}):
								for title in item.find_all('p'):
									print (title.get_text())
									#file.write((title.get_text())+"\n") - cant get this dang write to work
						

