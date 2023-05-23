from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://forms.office.com/Pages/ResponsePage.aspx?id=BTnzL-h5_kGxNuXPSTHur5MRzWm6IZ1DmCDtRDz55atUMU9NWEZERFZDN1c2RjBXVVBUUzFXUjRISy4u"
html = urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup.get_text())