# Description: This script scrapes the website for the data we need. TO USE INSTEAD OF SCRIPT IF WE CAN'T GET THE API TO WORK.

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')