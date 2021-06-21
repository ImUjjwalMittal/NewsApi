from django.shortcuts import render
from django.http import HttpResponse
import json 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import time 



@api_view()
def index(request):
    
    

    my_url='https://www.google.com/finance/'

    uclient=uReq(my_url)
    page_html=uclient.read()
    uclient.close()
    page_soup=soup(page_html,"html.parser")



    #data = soup(req.content,"html.parser")
    containers = page_soup.findAll("div",{"class":"yY3Lee"})
    URLS = page_soup.findAll("div",{"class":"z4rs2b"})

    headlines=[]
    image_link=[]
    urls=[]

    #print(len(containers))
    #print(soup.prettify(containers[0]))



    for container in URLS:
        links=container.findAll('a',href=True)
        for link in links:
            a=link['href']
            if a.startswith('https'):
                urls.append(a)       

    #for images 
    for container in containers:
        images=container.findAll('img')
        #print(images)
        for image in images:
            link=image['src']
            image_link.append(link)





    #for the headlines 
    for container in containers:
        inside =container.find("div",{"class":"AoCdqe"})
        text=inside.string
        headlines.append(text)

    headlines1 = []
    urls1 = []
    image_link1 = []

    headlines1 = headlines 
    urls1 = urls 
    image_link1 = image_link


    
    my_url='https://www.moneycontrol.com/news/economy-on-coronavirus-369.html'

    uclient=uReq(my_url)
    page_html=uclient.read()
    uclient.close()
    page_soup=soup(page_html,"html.parser")

    page_soup=page_soup.find('ul',attrs={'id':'cagetory'})

    headlines=[]
    image_link=[]
    urls=[]


    containers = page_soup.findAll("li",{"class":"clearfix"})

    for container in containers:
        links=container.findAll('a',href=True)
        for link in links:
            a=link['href']
            urls.append(a)
            break
            

            
    for container in containers:
        links=container.findAll('a',href=True)
        for link in links:
            b=link['title']
            headlines.append(b)
            break
        
        
        

    for container in containers:
        images=container.findAll('img')
        for image in images:
            link=image['data']
            image_link.append(link)

    urls3 = []
    headlines3 = []
    image_link3 = []

    urls3 = urls
    image_link3 = image_link
    headlines3 = headlines
        

    
    

    context = {'URL1' : urls1 , 'HEADLINES1' : headlines1 , 'IMAGE_LINK1' : image_link1 , 'URL3' : urls3 , 'HEADLINES3' : headlines3 , 'IMAGE_LINK3' : image_link3 }
    return Response(context)




    

