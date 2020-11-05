from bs4 import BeautifulSoup
import requests
url = ["https://www.epey.com/akilli-telefonlar/",
       "https://www.epey.com/akilli-telefonlar/2/",
       "https://www.epey.com/akilli-telefonlar/3/",
       "https://www.epey.com/akilli-telefonlar/4/",
       "https://www.epey.com/akilli-telefonlar/5/",
       "https://www.epey.com/akilli-telefonlar/6/",
       "https://www.epey.com/akilli-telefonlar/7/",
       "https://www.epey.com/akilli-telefonlar/8/",
       "https://www.epey.com/akilli-telefonlar/9/",
       "https://www.epey.com/akilli-telefonlar/10/",
       "https://www.epey.com/akilli-telefonlar/11/",
       "https://www.epey.com/akilli-telefonlar/12/",
       "https://www.epey.com/akilli-telefonlar/13/",
       "https://www.epey.com/akilli-telefonlar/14/",
       "https://www.epey.com/akilli-telefonlar/15/",
       "https://www.epey.com/akilli-telefonlar/16/",
       "https://www.epey.com/akilli-telefonlar/17/",
       "https://www.epey.com/akilli-telefonlar/18/",
       "https://www.epey.com/akilli-telefonlar/19/",
       "https://www.epey.com/akilli-telefonlar/20/"]
i=0
for j in url:
        html = requests.get(j).content
        soup = BeautifulSoup(html,"html.parser")
        tumliste = soup.find("div",{"class":"listele table"}).find_all("ul",{"class":"metin row"})
        for satır in tumliste:
                i+=1
                isimler = satır.find("li",{"class":"adi cell"}).find("div",{"class":"detay cell"}).find("a",{"class":"urunadi"}).text.strip()
                try:
                        link = satır.find("li", {"class": "fiyat cell"}).find("a").get("href")
                        fiyat = satır.find("li", {"class": "fiyat cell"}).find("a").text.split("TL")
                except AttributeError:
                        print("hata")

                print(i, isimler, "" + fiyat[0] + "TL: ", link)



