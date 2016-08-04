# webscraping
Sample scripts for web scraping.
Typically tied to use cases, but generally extensible to other projects.
Scripts help build URL lists to feed to WGET for bulk downloading in a responsible manner (e.g. rate limiting).

**fdr_item_urls**: scrape item URLs matching a type from the Franklin D Roosevelt Master Speech File, write URLs to TXT or CSV file

**frus_singlevolume_pdf_urls**: scrape single volume section URLs from the the University of Wisconsin Madison's Foreign Relations of the United States, proceed to follow each URL to section page and scrape PDF URLs, write PDF URLs to TXT file

**frus_allvolumes**: scrape all volume URLs from the the University of
  Wisconsin Madison's Foreign Relations of the United States, proceed
  to follow each URL to each volume, navigate down to each section of
  each volume and scrape PDF URLs and PDF citations and write each
  list to a separate TXT file.

contact: tgpadillajr@gmail.com
