import urllib.request, urllib.error
from bs4 import BeautifulSoup

url = "https://magazine.jp.square-enix.com/top/comics/"
#python2系ではurllib.request(url)
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")

cnt=0
rcnt=0

h2 = soup.find_all("span")

book_titles = []
book_date = []
book_title_list = []
book_volumes = []

book_info = []
f=open('titles_0806.csv', mode='w+',encoding='utf-8')

# タイトルを取得
titles_lists=[]
titles = soup.find_all('span', class_='numCol')
for i in titles:
    titles_lists.append(i.text)
    #print(titles)

# 巻数を取得
volumes_lists=[]
volumes = soup.find_all('span', class_='numCol2')
for j in volumes:
    volumes_lists.append(j.text)

# 出版日を取得
dates_lists = []
dates = soup.find_all('span', class_='numCol2')
for k in dates:
    dates_lists.append(k.text)

#書影を取得
book_pic = []
pics  = soup.find_all('img')
for l in pics:
    img_url = l.get('src')
    img_url = 'https://magazine.jp.square-enix.com' + img_url
    book_pic.append(img_url)
book_pics = [s for s in book_pic if 'shoei' in s]
#print(book_pics)

for tag in h2:
    try:
        string_ = tag.get("class").pop(0)
        if string_ in "dates fo15":
            ts = tag.string.replace('　',' ')#注1
            book_date.append(ts)
        if string_ in "numCol2":
            print(tag.string)
            tz = tag.string.replace('　',' ')#注1
            book_titles.append(tz)
    except:
        pass

#ここでタイトルと巻数を分けてリストに代入する。
#print(book_titles)
for j in book_titles: #book_titlesは奇数回目にタイトルが入っている
    cnt+=1
    if cnt % 2 == 0: #book_titlesには偶数回目に巻数が入っている
#        print('偶数回')
        #print('%s,' %j)
        book_volumes.append(j)
        #f.write('%s\n' %j) #巻数を記入
    else:
#        print('')
        #print('%s,' %j)
        book_title_list.append(j)
        #f.write('%s,' %j) #タイトルを記入

for a,b,c,d in zip(book_date,book_title_list,book_volumes,book_pics):
    print('%s,%s,%s,%s\n' %(a,b,c,d))
    f.write('%s,%s,%s,%s\n' %(a,b,c,d))
    
'''
for m in book_info:
    print (str(m))
#    f.write('%s' %m)

'''

#print(book_titles)
#x = ','.join(book_titles)
#print(x)

f.close()
