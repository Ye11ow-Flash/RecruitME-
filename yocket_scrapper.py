import requests
import sys
from bs4 import BeautifulSoup

url = "https://yocket.in/profiles/Yashwanth1997nerdy"
def get_codeforces_rating(url):
  source_code = requests.get(url)
  plain_text=source_code.text
  soup = BeautifulSoup(plain_text)
  info=[]
  for link in soup.findAll('h4'):
    info.append(link.text)
    # print(link.small.br)
  # print(info[46])
  for i in info:
  	if 'Work Exp.' in i:
  		work_exp = i.split('.')[1]
  		# print(i.split('.')[1])
  	elif 'Tech Papers' in i:
  		# print(i.split('Tech Papers')[1])
  		tech_paper = i.split('Tech Papers')[1]


  sk = []
  for skill in soup.findAll('div', class_ = 'col-sm-12 more-detail-info border-top'):
  	sk.append(skill.text)

  
  s = str(sk)
  # print(s)
  skillset = []
  sk = s.split('\\n')
  for i in sk:
  	if i != '':
  		skillset.append(i)
  skillset = skillset[1:]
  skillset = skillset[:-1]


  print(work_exp)
  print(tech_paper)
  print(skillset)

get_codeforces_rating(url)