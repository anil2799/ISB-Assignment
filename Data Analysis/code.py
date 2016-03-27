#import requests
#from BeautifulSoup import BeautifulSoup

import urllib2
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'
#response =requests.get(url)
#html = response.content
#print (html)

#soup = BeautifulSoup(html)

page=urllib2.urlopen(url)
soup=BeautifulSoup(page)

print type(soup)
#print soup.prettify()[0:100]
print soup.title
#print soup.a

#all_links=soup.find_all("a")
#for link in all_links:
#	print link.get("href")

all_tables=soup.find_all("table")
#print all_tables

right_table = soup.find("table",class_="wikitable sortable plainrowheaders")
#print right_table

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]


print right_table.findAll("tr")[0]
print "printing td"
print len(right_table.findAll("tr")[0].findAll("td"))
print right_table.findAll("tr")[0].findAll("td")
print "printing th"
print len(right_table.findAll("tr")[0].findAll("th"))
print right_table.findAll("tr")[0].findAll("th")

print right_table.findAll("tr")[1]
print "printing td"
print len(right_table.findAll("tr")[1].findAll("td"))
print right_table.findAll("tr")[1].findAll("td")
print "printing th"
print len(right_table.findAll("tr")[1].findAll("th"))
print right_table.findAll("tr")[1].findAll("th")


for row in right_table.findAll("tr"):
	cells=row.findAll("td")
	states=row.findAll("th")
#	print len(cells)
#	print len(states)
	if len(cells)==6 :
#		print cells[4]
		A.append(cells[0].find(text=True))
		B.append(states[0].find(text=True))
		C.append(cells[1].find(text=True))
		D.append(cells[2].find(text=True))
		E.append(cells[3].find(text=True))
		F.append(cells[4].find(text=True))
		G.append(cells[5].find(text=True))
#	print cells
#	print states
'''
	if len(cells)==6 :
		A.append(cells[0].find(text=True))
		B.append(states[0].find(text=True))
		C.append(cells[1].find(text=True))
		D.append(cells[2].find(text=True))
		E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))

print A
print B
print C
print D
print E
print F
print G
'''

import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G
#print df.head()