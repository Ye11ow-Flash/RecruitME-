import requests
import sys
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/users/10905798/sangram-desai"
def get_codeforces_rating(url):
  source_code = requests.get(url)
  plain_text=source_code.text
  soup = BeautifulSoup(plain_text)
  info=[]
  # grid--cell ws-nowrap
  for link in soup.findAll('div', class_ = 'profile-top-tags'):
    info.append(link.text)
    temp = soup.find('span', class_ = 'fc-medium fs-title')
    # temp2 = soup.find('span', class_ = 'mr4 fw-bold tt-uppercase')
    for j in temp:
      info.append(j)


  s = str(info)
  # print(s)
  skillset = []
  sk = s.split('\\r')[0]
  sk = sk.split('\\n')
  for i in sk:
    if i != '':
      skillset.append(i)
  skillset = skillset[1:]
  skillset = skillset[0:4]+skillset[6:]
  print(skillset)

  # final_skill = []

  # for i in range(len(skillset)):
  #   if skillset[i] == 'Posts %' and isinstance(int(skillset[i+1]), int):
  #     pass
  #   else:
  #     final_skill.append(skillset[i])
  # for i in final_skill:
  #   if is
  # print(final_skill)
  # print(sk)

  # for i in info:
    # print(i)


    # print(link.small.br)
  # print(info[46])
  

get_codeforces_rating(url)