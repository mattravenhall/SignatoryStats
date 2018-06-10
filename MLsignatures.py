import requests
import pandas as pd
from bs4 import BeautifulSoup

#soup = BeautifulSoup(requests.get('https://openaccess.engineering.oregonstate.edu/signatures').content)
soup = BeautifulSoup(open('signatures.html'), 'html.parser')
positions = soup.find_all("div", class_="views-field views-field-field-professional-position")
institutions = soup.find_all("div", class_="views-field views-field-field-institution")
countries = soup.find_all("div", class_="views-field views-field-field-country")

# Rough position counts
print('=Rough Overview of Positions=')
print(pd.Series([x.get_text().strip(' ') for x in positions]).value_counts().head(10))

# Count position types
blank = sum([x.get_text().lower() == '  ' for x in positions])
student = sum([('msc' in x.get_text().lower()) or ('phd' in x.get_text().lower()) or ('student' in x.get_text().lower()) or ('candidate' in x.get_text().lower()) for x in positions])
professor = sum([('professor' in x.get_text().lower()) or ('lecturer' in x.get_text().lower()) for x in positions])
postdoc = sum([('postdoc' in x.get_text().lower()) for x in positions])
datascientist = sum([('data scientist' in x.get_text().lower()) for x in positions])
engineers = sum([('engineer' in x.get_text().lower()) for x in positions])
software = sum([('software' in x.get_text().lower()) for x in positions])
devs = sum([('developer' in x.get_text().lower()) for x in positions])
research = sum([('research' in x.get_text().lower()) for x in positions])

# Specific groups
print('\n=Specific Examples (Total: {:,})='.format(len(positions)))
print('Blank: {}'.format(blank))
print('Students: {}'.format(student))
print('Professors: {}'.format(professor))
print('PostDocs: {}'.format(postdoc))
print('Data Scientists: {}'.format(datascientist))
print('Engineers: {}'.format(engineers))
print('Software: {}'.format(software))
print('Developers: {}'.format(devs))
print('Researchers: {}'.format(research))

# Pull all key words
import re
keywords = [i for j in [re.sub(r'[^\w\s]','', x.get_text().lower().strip(' ')).split(' ') for x in positions] for i in j if i != '']
print('\n=Imperfect Overview of Keywords=')
print(pd.Series(keywords).value_counts().head(10))

# Countries
print('\n=Most Frequent Countries=')
print(pd.Series([x.get_text().strip(' ') for x in countries]).value_counts().head(10))

# Institutions
print('\n=Most Frequent Institution=')
print(pd.Series([x.get_text().strip(' ') for x in institutions]).value_counts().head(10))
print(sum([('oregon' in institution.get_text().lower()) for institution in institutions]))
print([institution.get_text().lower().strip(' ') for institution in institutions if 'oregon' in institution.get_text().lower()])
