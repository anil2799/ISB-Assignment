#Import necessary libraries
import urllib2
from bs4 import BeautifulSoup

url="http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PALL&p=1&u=%2Fnetahtml%2FPTO%2Fsrchnum.htm&r=1&f=G&l=50&s1=8829700.PN.&OS=PN/8829700&RS=PN/8829700"
page=urllib2.urlopen(url)
soup=BeautifulSoup(page)
#print type(soup)
#print soup.title
soup.prettify() #for nested structure of html page

all_tables=soup.find_all("table")
right_table=all_tables[3]

required_row=right_table.findAll("tr")[3]

#Extract the information to Lists nd convert into a Data Frame



#Extract Names list of Inventors
A = []
nameslist=[]
nameslist1=[] #to convert unicode list to normal list with strings
A = required_row.findAll("td")[0].get_text()
nameslist=A.split("\n")
for i in nameslist:
	i=str(i)
	if(i[0]==' '):
		i=i[1:]
	nameslist1.append(i.encode('ascii'))
#	print i
#print nameslist
#print nameslist1



#Extract Cities list of Inventors
B=[]
citieslist=[]
B=required_row.findAll("td")[1].get_text()
citieslist=B.split("\n")
for i in citieslist:
	i=str(i)
	if(i[0]==' '):
		i=i[1:]
#print citieslist


#Extract Countries list of Inventors
C=[]
countrieslist=[]
countrieslist1=[]
C=required_row.findAll("td")[3].get_text()
countrieslist=C.split("\n")
for i in countrieslist:
	i=str(i)
	if(i[len(i)-1]==' '):
		i=i[0:len(i)-1]
	if(i[0]==' '):
	#	print "yes"
		i=i[1:]
	countrieslist1.append(i.encode('ascii'))
#print countrieslist
#print countrieslist1



#Merge Cities list and Countries list
Locations=[]
Locations1=[]
Locations=[x+', '+y for x,y in zip(citieslist,countrieslist1)]
#print Locations
#print "\n" + "\n"
for i in Locations:
	if(i[0]==' '):
		i=i[1:]
	Locations1.append(i.encode('ascii'))
#	print i
#print Locations1

print "Inventors:"
'''
print "\n"
for i,j in zip(nameslist1,Locations1):
	print (i + "         " + j)
'''
print "\n"

import pandas as pd
df1=pd.DataFrame(nameslist1,columns=['Names'])
df1['City']=citieslist
df1['Country']=countrieslist1
print df1 + "\n"



												#Extract Patent Number from title
soup_title=soup.title
soup_text=soup_title.get_text()
soup_text=soup_text.encode('ascii')
#print soup_text
soup_text_split=soup_text.split()
#print soup_text_split
for s in soup_text_split:
	if s.isdigit():
		patent_number=int(s)
#print patent_number
patent_number_list=[]
patent_number_list.append(patent_number)
print "\n"
print "Patent Number : " + str(patent_number_list[0])
#print "\n"


												#Extract Assignee Information

#print right_table
assignee_row=right_table.find_all("tr")[4]
#print assignee_row

assignee_th=assignee_row.find_all("th")
#print assignee_th[0].get_text()
assignee_header=assignee_th[0].get_text()

assignee_td=assignee_row.find_all("td")
#print assignee_td[0].get_text()
btag1=assignee_td[0].b
#print btag1.contents
assignee_req=btag1.contents[0].encode('ascii')
#print type(assignee_req)

assignee_req_list = []
assignee_req_list.append(assignee_req)
#print assignee_req_list[0]
print assignee_th[0].get_text() + " " + assignee_req_list[0]
#print "\n"



												#Extract Filed Information

filed_row=right_table.find_all("tr")[7]
#print filed_row

filed_th=filed_row.find_all("th")
#print filed_th[0].get_text()
filed_header=filed_th[0].get_text()
filed_header=filed_header.split("\n")
#print filed_header
filed_header_req=filed_header[0].encode('ascii')
#print filed_header_req
#print len(filed_header)

filed_td=filed_row.find_all("td")
btag2=filed_td[0].b
#print btag2.contents
filed_req=btag2.contents[0].encode('ascii')

filed_req_list=[]
filed_req_list.append(filed_req)
#print filed_req_list[0]
print filed_header_req + " " + filed_req_list[0]
print "\n"



										 #import pandas to convert list to data frame 

#import pandas as pd
#df=pd.DataFrame(Locations1,columns=['Locations'])
#df['Inventors']=nameslist1
df=pd.DataFrame(patent_number_list,columns=['Patent Number'])
df['Filed']=filed_req_list
df['Assignee']=assignee_req_list
df['Inventor 1']=nameslist1[0]
df['Location 1']=Locations1[0]
df['Inventor 2']=nameslist1[1]
df['Location 2']=Locations1[1]
df['Inventor 3']=nameslist1[2]
df['Location 3']=Locations1[2]
df['Inventor 4']=nameslist1[3]
df['Location 4']=Locations1[3]
df['Inventor 5']=nameslist1[4]
df['Location 5']=Locations1[4]
df['Inventor 6']=nameslist1[5]
df['Location 6']=Locations1[5]


#df=df.drop(0)
#print df
#print df.columns




#import xlsxwriter
writer=pd.ExcelWriter('ISB_Strat_Assignement_Patent.xlsx',engine='xlsxwriter') # Create a Pandas Excel writer using XlsxWriter as the engine.
df.to_excel(writer,'Sheet1',merge_cells=False) # Convert the dataframe to an XlsxWriter Excel object.
writer.save() # Close the Pandas Excel writer and output the Excel file.

print "Data written to ISB_Strat_Assignement_Patent.xlsx" 
print "\n"