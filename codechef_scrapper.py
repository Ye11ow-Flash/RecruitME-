import requests
from bs4 import BeautifulSoup
import sys


url = "https://www.codechef.com/users/ye11ow_flash"
def get_codechef_rating(url):
  source_code = requests.get(url)
  plain_text=source_code.text
  soup = BeautifulSoup(plain_text)
  info=[]
  for link in soup.findAll('div',{'class' : 'rating-number'}):
    info.append(link.string)
  print(info[0])
  for link in soup.findAll('li'):
    info.append(link.text)
  # print(info)
  # for i in range(len(info)):
  	# print(info[i])
  # print("-----------------------------------------------")
  print(info[67])
  print(info[66].split("")[0])



  for link in soup.findAll('g'):
  	print(link)
  # x = soup.find('a').find('strong').text
  # print(x)

  # get_codechef_rating(sys.argv[1])
get_codechef_rating(url)



# URL = "https://www.linkedin.com/in/sangram-desai-aab001168/"
# from linkedin_scraper import Person
# person = Person("https://www.linkedin.com/in/sangram-desai-aab001168/")
# print(person)

# from pylinkedin.scraper import LinkedinItem
# l = LinkedinItem(url='https://www.linkedin.com/in/sangram-desai-aab001168/')
# l = LinkedinItem(html_string=profile_string)
# print(l)
# from linkedin_scraper import Person, actions
# from selenium import webdriver
# driver = webdriver.Chrome()
# email = "some-email@email.address"
# password = "password123"
# actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
# person = Person("https://www.linkedin.com/in/sangram-desai-aab001168/", driver=driver)


# driver = webdriver.Chrome()
# # person = Person("https://www.linkedin.com/in/andre-iguodala-65b48ab5", driver = driver, scrape=True)
# person = Person("https://www.linkedin.com/in/sangram-desai-aab001168/", scrape=True)
# # print(person)
# scrape(close_on_complete=True)



# r = requests.get(URL)
# soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify()) 
# # print(r.content)
# URL = "https://www.hackerrank.com/atharva456"
# r = requests.get(URL)

# soup = BeautifulSoup(r.content, 'html5lib') 
  
# quotes=[]  # a list to store quotes 
  
# table = soup.find('section', attrs = {'id':'content'}) 
  
# for row in table.findAll('div', attrs = {'class':'quote'}): 
#     quote = {} 
#     quote['theme'] = row.h5.text 
#     quote['url'] = row.a['href'] 
#     quote['img'] = row.img['src'] 
#     quote['lines'] = row.h6.text 
#     quote['author'] = row.p.text 
#     quotes.append(quote) 





# URL = "https://internshala.com/student/resume?detail_source=resume_direct"
# r = requests.get(URL)
# # soup = BeautifulSoup(r.content, 'html5lib') 
# # print(soup)
# # content = BeautifulSoup(soup)

# # for div in content.findAll('div', attrs={'class':'badge-title'}):
# #     print(div.text)
# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup)
# # txt = "1"
# txt = soup.find('body', id = 'content')
# if txt == '1':
# 	print("not done")
# else:
# 	print(txt)
# for cont in txt:
# 	if cont.find('section', class_ = 'hacker-badges-section'):
# 		op = cont.find('h2', class_ = 'hacker-badges-title')
# 		op1 = op.text
# 		print(op1)

# 		xx = cont.h2.plain_text
# 		print(xx)
# txt1 = txt.find('section', class_ = 'hacker-badges-section')
# txt = txt.findAll('div', attrs = {'class':'ui-kit-root'})
# txt = soup.findAll('div', attrs = {'class':'show-cookie-banner'})
# txt = soup.findAll('div', attrs = {'class':'new-design'})
# txt = soup.findAll('div', attrs = {'class':'community-content'})
# # txt = soup.findAll('div', attrs = {'class':'content'})
# # txt = soup.findAll('div', attrs = {'class':'content'})
# # txt = soup.findAll('div', attrs = {'class':'content'})
# print(txt1)


# soup = BeautifulSoup(r.content, 'html5lib') 
# print(soup.prettify()) 

# def get_linkedin(url):
#   source_code = requests.get(url)
#   plain_text=source_code.text
#   soup = BeautifulSoup(plain_text)
#   # print(soup)
#   str=[]
#   for link in soup.findAll('a',{'class':'section_card'}):
#     str.append(link.string.replace("\n","").strip())
#   print(str)

# get_linkedin(url)
