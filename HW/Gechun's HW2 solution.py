from bs4 import BeautifulSoup
import urllib
import csv
import os

# Set WD
os.chdir('/Users/lingechun/Documents/GitHub/python_summer2020/HW')

with open('HW2_gechun.csv', 'w') as f:
	w = csv.DictWriter(f, fieldnames = ("Title", "Published date", "Issues", "Number of signatures"))
	w.writeheader()
	# We want to scrap first two pages of petitions so the range should be (1,3)
	petition_link = []
    for i in range(1, 3):
    	# Open the website page
	    web_address = 'https://petitions.whitehouse.gov/petitions?page=' + str(i)
	    web_page = urllib.request.urlopen(web_address)
	    # Parse it
	    soup = BeautifulSoup(web_page.read())
        # Find all peptions links on page one/two
	    this_petition_link = soup.find_all('h3')
	    # The first three links are not related to the petitions so get rid of them
	    this_petition_link = this_petition_link[3: len(this_petition_link)]
	    # Add all the links together for later use 
	    petition_link = petition_link + this_petition_link


	# Loop over petition_link
	for i in petition_link[0:len(petition_link)]:
	# Title
        petition = {}
        petition['Title'] = i.text
    # Open each petition's website
        try:
		    petition_page = urllib.request.urlopen("https://petitions.whitehouse.gov" + i.find('a')['href'])	
		# Parse it
		    soup = BeautifulSoup(petition_page.read())
	    except urllib.error.URLError:
		    continue
    # Published date
        try:
		    petition['Published date'] = soup.find('h4', class_ = 'petition-attribution').text
	    except AttributeError:
		    petition['Published date'] = 'NA'

	# Issues
        try:
		    petition['Issues'] = soup.find('div', class_ = 'content').find_all('h6')
	    except AttributeError:
		    petition['Issues'] = 'NA'

	# Number of signatures
	    try:
		    petition['Number of signatures'] = soup.find('span', class_ = 'signatures-number').text
	    except AttributeError:
		    petition['Number of signatures'] = 'NA'

	    w.writerow(petition)


# Modify the csv file
import pandas as pd
# open the cvs file
file = pd.read_csv("/Users/lingechun/Documents/GitHub/python_summer2020/HW/HW2_gechun.csv")
# clean the Issues
# issues2 = [re.sub('[^a-zA-Z0-9\\\/ #]|_', '', \     issues[i]) for i in range(0, len(issues))] 
issues = []
for i in range(0, len(file['Issues'])):
	this_issue = file['Issues'][i].replace('<h6>', '')
	this_issue = this_issue.replace('</h6>', '')
	this_issue = this_issue.replace('&amp;', '&')
	this_issue = this_issue.replace('[', '')
	this_issue = this_issue.replace(']', '')
	issues.append(this_issue)
file['Issues'] = issues

# clean the Published date
dates = []
for i in range(0, len(file['Published date'])):
	this_date = file['Published date'][i].split()
	this_date = this_date[-3:]
	this_date = ' '.join(this_date)
	dates.append(this_date)
file['Published date'] = dates
# store the modification back to a new csv file
file.to_csv(r'/Users/lingechun/Documents/GitHub/python_summer2020/HW/HW2_gechun_clean.csv', index = False)


