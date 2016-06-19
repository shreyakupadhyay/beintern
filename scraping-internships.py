import requests
from BeautifulSoup import BeautifulSoup
import sys

salary = []
pages = int(sys.argv[1])


s = requests.session()

# for i in range(0, pages):
#    soup = s.get('')

for i in range(1, pages):
    try:
        soup = s.get('http://internshala.com/internships/page-' + str(i)).text
        html = BeautifulSoup(soup)
        print i
        jobs = html.findAll('div', {'class': 'container-fluid individual_internship'})
        
        for val in jobs:
            stipend = val.td.findNextSibling('td').findNextSibling('td')
            posted_on = val.td.findNextSibling('td').findNextSibling('td').findNextSibling('td').text
            company_name = val.h4.findNextSibling('h4')
            url = val.findAll('a')[2]['href']
    
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
