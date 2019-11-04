
def elpaisScrap(year, month, day, gap):

    # Libraries
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    from newspaper import Article
    import re

    # open html
    page = "https://elpais.com/hemeroteca/elpais/" + str(year) + "/" + str(month) + "/" + str(day) + "/" + gap + "/portada.html"
    page = urlopen(page)
    soup = BeautifulSoup(page, 'html.parser')

    # find links
    urls = soup.findAll("h2")
    links = []
    for i in urls:
        links.append(i.find("a").get("href"))

    # filter links (no adds)
    goodLinks = []
    for link in links:
        for m in re.finditer(r'\b.html\b', link):
            goodLinks.append(link)

    # extract text and save in .txt

    file = "news" + str(year) + "-" + str(month) + "-" + str(day) + "-" + gap + ".txt"
    print("a file with the " + file + " name will be saved")
    for i in goodLinks:
        if i[0] != "h":
            i = "https://elpais.com/" + i
        try:
            a = Article(i, language='es')
            a.download()
            a.parse()
            with open(file, 'a') as f:
                print(a.title, file=f)
                print(a.text, file=f)
        except:
            pass

def elpaisScrapEarly(year, month, day):

    # Libraries
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    from newspaper import Article
    import re

    # open html
    page = "https://elpais.com/tag/fecha/" + str(year) + str(month) + str(day)
    page = urlopen(page)
    soup = BeautifulSoup(page, 'html.parser')

    # find links
    urls = soup.findAll("h2")
    links = []
    for i in urls:
        links.append(i.find("a").get("href"))

    # filter links (no adds)
    goodLinks = []
    for link in links:
        for m in re.finditer(r'\b.html\b', link):
            goodLinks.append(link)

    # extract text and save in .txt

    file = "news" + str(year) + "-" + str(month) + "-" + str(day) + ".txt"
    print("a file with the " + file + " name will be saved")
    for i in goodLinks:
        if i[0] != "h":
            i = "https:" + i
        try:
            a = Article(i, language='es')
            a.download()
            a.parse()
            with open(file, 'a') as f:
                print(a.title, file=f)
                print(a.text, file=f)
        except:
            pass

year = str(input("Type the year: "))
month = str(input("Type the month: "))
day = str(input("Type the day: "))
gap = input("Type the gap (m = morning, t = evening, n = night): ")

if len(month) == 1:
    month = "0"+month

if len(day) == 1:
    day = "0"+day

if int(year) >= 2012:
    elpaisScrap(year, month, day, gap)
else:
    elpaisScrapEarly(year, month, day)
