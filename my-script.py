'''
Author : Shreyak Upadhyay
Email : shreyakupadhyay07@gmail.com
Subject : getting data from internshala .
Description:
Getting data from internshala website. 
'''
import requests
from bs4 import BeautifulSoup
import sys

salary = []
pages = int(sys.argv[1])


s = requests.session()

# for i in range(0, pages):
#    soup = s.get('')
#for i in range(1, pages):
    #try:
soup = s.get("http://internshala.com/internships/computer%20science-internship").text
#soup = s.get('http://internshala.com/internships/page-' + str(i)).text
html = BeautifulSoup(soup,'lxml')

jobs = html.findAll('div', {'class': 'container-fluid individual_internship'})
#print jobs[0]
#print jobs
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

    print "GOT+++++++++++++++++++++++++++++++++"
