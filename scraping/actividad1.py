import requests
from bs4 import BeautifulSoup
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

text_to_search = "engineer"

job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title", string=lambda x: text_to_search.lower() in x.lower())
    if not title_element:
       continue
    
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    if (title_element):
      print(title_element.get_text().strip())

    if (company_element):
      print(company_element.get_text().strip())

    if (location_element):
      print(location_element.get_text().strip())

    link_element = job_element.find("a", string=lambda x: x == "Apply")
    if (link_element):
      print(link_element['href'])

    print("---------")
