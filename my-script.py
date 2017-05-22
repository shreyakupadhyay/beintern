'''
Author : Shreyak Upadhyay
Email : shreyakupadhyay07@gmail.com
Subject : getting data from internshala .
Description:
Getting data from internshala website. 
'''
import requests, sys
from bs4 import BeautifulSoup


salary = []
pages = int(sys.argv[1])


s = requests.session()

def getInternship():
	response = s.get("http://internshala.com/internships/computer%20science-internship").text
	soup = BeautifulSoup(response,'lxml')
	jobs = soup.findAll('div', {'class': 'container-fluid individual_internship'})

	for val in jobs:
	    """
	    This part is for "individual_internship_header" 
	    """
	    #internship title
	    print (val.findChildren()[0]).find('h4').get('title')
	    #print (val.findChildren()[0]).find('h4').getText()
	    print " ".join((val.findChildren()[0]).find('h4').getText().split())  # removing extra spaces from the string
	    print (val.findChildren()[0]).find('h4').findNextSibling('h4').findChildren()[0]['href']
	    print (val.findChildren()[0]).find('h4').findNextSibling('h4').findChildren()[0]['title']
	    """
	    This part is for "individual_internship_details"
	    """ 
	    #Duration , Stipend , Posted On , Apply By
	    for giv in val.findAll('td'):
	        print " ".join(giv.getText().split())

getInternship()   
