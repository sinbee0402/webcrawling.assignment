gimport requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"

req = requests.get(url)

html = req.text
soup = BeautifulSoup(html, 'html.parser')

titles = soup.find('ul', class_='r_ranking box').find_all('li')

title = []

for i in titles:
    title.append(i.get_text().strip())

title = title[:]

print(title)

f = open("ict웹크롤링과제.txt", 'w')  #'r' , 'w', 'a'
for i in range(len(title)):
    f.write(str(i+1)+"."+title[i]+"\n")

f.close()

# txt파일에 안적어져요~~~~~ 나 입구컷당했어~~~~~
#울어야지~~~~~~~으어ㅓ어ㅓㅇ어ㅓ어어엉엉우우어안ㅁㅇ린몽림넝롬