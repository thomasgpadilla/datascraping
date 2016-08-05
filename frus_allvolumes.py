from urllib2 import urlopen
from bs4 import BeautifulSoup
import requests

# Adds the relative URL to the WISC digital collections host, then
# soupifies the resulting URL.
#
# @param [String] rellink
# @return [Soup]
def slurp(rellink):
        targetURL = 'http://digicoll.library.wisc.edu/' + rellink
        fetchedURL = requests.get(targetURL)
        return BeautifulSoup(fetchedURL.content, 'html.parser')

# @params [Soup] what
# @return [List]
def drill(what):
        # Find all the p.isshead elements in the soup, then get the
        # href of the first a element within each
        level1 = [x.a.get('href') for x in what.find_all("p", {"class":"isshead"})]
        # Soupify each of the links from level1
        level2 = [slurp(x) for x in level1]
        # Find each of the p.cntsitem elements in each of the level2
        # soups, then smush them together into a flat list as shown in
        # http://stackoverflow.com/a/952952
        level3 = [item for sublist in [x.find_all("p", {"class":"cntsitem"}) for x in level2] for item in sublist]
        # Get the href of the first a element within each of the p elements in level3
        level4 = [x.a.get('href') for x in level3]
        # Soupify each of the links from level4
        return [slurp(x) for x in level4]

def main():
        # point to FRUS volumes
        html = urlopen("http://digicoll.library.wisc.edu/cgi-bin/FRUS/FRUS-idx?type=browse&scope=FRUS.FRUS1")
        soup = BeautifulSoup(html, 'html.parser')
        drilldown = drill(soup)

        with open("fdr_allpdf_urls.txt", "w") as file:
                # Find the first div.itemmd in the soups that result from
                # drill()-ing into the original soup
                itemmds = [x.find_all("div", {"class":"itemmd"})[0] for x in drilldown]
                # Get the href of the first a element from each member of itemmds
                pdfURLs = [x.a.get('href') for x in itemmds]
                for url in pdfURLs:
                        print url
                        file.write(url + "\n")

        with open("fdr_allpdf_citations.txt", "w") as file:
                # Find the first p.biblio in the soups that result from
                # drill()-ing into the original soup
                biblios = [x.find_all("p", {"class":"biblio"})[0] for x in drilldown]
                for item in biblios:
                        print (item.get_text())
                        file.write((item.get_text()) + "\n")

if __name__ == "__main__":
        main()
