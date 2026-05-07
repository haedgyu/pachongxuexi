import requests
from bs4 import BeautifulSoup
def douban():
    headers = {
    'User-agent':(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                 ' AppleWebKit/537.36 (KHTML, like Gecko)'
                 ' Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0'
    ),
    'Host':(
        'movie.douban.com'
    )
}
    movie_list=[]
    for i in range(1,10):
        url = f"https://movie.douban.com/top250?start={i * 25}"
        r = requests.get(url, headers=headers, timeout=5)
        print(str(i+1),"页响应状态码：",r.status_code)

        soup = BeautifulSoup(r.text, 'lxml')
        div_list=soup.find_all('div', class_='hd')
        for each in div_list:
            movie =each.a.span.text.strip()
            movie_list.append(movie)
    return movie_list
movies = douban()
with open('movie_list.txt','w',encoding='utf-8') as f:
    f.write("")
with open('movie_list.txt','a',encoding='utf-8') as f:
    f.write('\n'.join(movies))


