from django.shortcuts import render
from django.http import HttpResponse
import requests
import bs4  #beautiful_soup

page= requests.get('https://fabpedigree.com/james/mathmen.htm')
soup= bs4.BeautifulSoup(page.content,'html.parser')

li= soup.findAll('li')
names=[]

for data in li:
    d=data.find('a')
    names.append(d.text)

# Create your views here.
def home(request):
    #return HttpResponse('Hello,Laxmi')
   # names= ['anu','laxmi','rubina']
   # d= {
   #     'name': names,
    #    'college': 'Aberdeen'
   # }
    d={
        'name':names
    }

    return render(request,'home.html',context=d)


def bootcamp(abc):

    return HttpResponse('<h1>Hello Bootcamp</h1>')

