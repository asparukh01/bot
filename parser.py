import requests
from bs4 import BeautifulSoup

url = 'https://drivemusic.club'

proxies = {
            'http': 'http://proxy.halykbank.nb:8080',
            'https': 'http://proxy.halykbank.nb:8080',
        }

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; '
                          'Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/106.0.0.0 Safari/537.36'
}


response = requests.get(url, verify=False, headers=headers, proxies=proxies)
content = response.content
soup = BeautifulSoup(content, 'lxml')

music_block = soup.find('div', attrs={'class': 'main-music-popular'})
download_block = music_block.find('div', attrs={'class': 'popular-download'})
for a in download_block.find_all('a', href=True):
    link = url + a['href']
print(link)
response = requests.get(link, verify=False, headers=headers, proxies=proxies)
content = response.content
soup_v2 = BeautifulSoup(content, 'lxml')
link_music = soup_v2.find('div', attrs={'class': 'song-author-btn-box'})
print(link_music)
for a in link_music.find_all('a', href=True):
    music = a['href']
    with open('mus.mp3', 'wb') as f:
        f.write(requests.get(url+music).content)
# print(download_block)