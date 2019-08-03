#图片
import urllib.request
import re
import urllib.error
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
#for j in range(2,12):
    #url=""+str(j)+""构造网址
    try:
        data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
        #pat = ''不完全图片网址
        result = re.compile(pat).findall(data)
        for i in range(len(result)):
            #imgurl = ""+result[i]构造完整图片网址
            #file = ""+str(j)+"-"+str(i)+".jpg"存放目录
            urllib.request.urlretrieve(imgurl, filename=file)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    except Exception as e:
        print(e)
