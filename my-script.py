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
html = BeautifulSoup(soup)

jobs = html.findAll('div', {'class': 'container-fluid individual_internship'})
#print jobs[0]
#print jobs
for val in jobs:
    """
    This part is for "individual_internship_header" 
    """
    print (val.findChildren()[0]).find('h4').get('title')
    print (val.findChildren()[0]).find('h4').getText()
    print (val.findChildren()[0]).find('h4').findNextSibling('h4').findChildren()[0]['href']
    print (val.findChildren()[0]).find('h4').findNextSibling('h4').findChildren()[0]['title']
    """
    This part is for "individual_internship_details"
    """
    for child in val.findChildren():
        print child
        print "========="
        print "========="
        print "========="
        print "========="
    print val

    #for child in children:
        #print child
    #print val.children.string
    #print val.next_sibling
    #stipend = val.td.findNextSibling('td').findNextSibling('td')
    #posted_on = val.td.findNextSibling('td').findNextSibling('td').findNextSibling('td').text
    #company_name = val.h4.findNextSibling('h4')
    #url = val.findAll('a')[2]['href']
    #print stipend
    break



"""
            if(stipend.text[0] == 'R'):
                pstipend = stipend.text.split()[0].split('-')
                if(len(pstipend) > 1):
                    salary.append((int(pstipend[1]), i, posted_on, company_name.text, url))
                else:
                    salary.append(
    				(int(pstipend[0].split('.')[1]), i, posted_on, company_name.text, url))
    except:
        print "Exception occured"
        
        
salary.sort(reverse=True)
intern = open('internships.txt', 'w')

for v in salary:
    print v[0], v[1], v[2], v[3]
    print "http://internshala.com" + v[4]
    print "\n"
    intern.write(str(v[0]) + " " + str(v[1]) + 
                 " " + str(v[2]) + " " + str(v[3]))
    intern.write("\n")
    intern.write("http://internshala.com" + v[4])
    intern.write("\n\n")

intern.close()
"""