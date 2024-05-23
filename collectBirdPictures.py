import wikipedia
import wikipediaapi
# this is beautiful soup
from bs4 import *
import requests

wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')
testerLink = 'https://en.wikipedia.org/wiki/File:Petroica_boodang_Meehan_Range_1_crop.jpg'
# returns a list of strings that are links to the related webpages
def gatherRelatedArticles(ranPage):
    sample_url = ranPage
    res = requests.get(sample_url)

    # get body content
    sampleInfo = BeautifulSoup(res.text, 'html.parser').select('body')[0]

    links = []
    toRemove = ('/wiki/Main_Page', '/wiki/Wikipedia:Contents', '/wiki/Portal:Current_events', '/wiki/Special:Random',
                '/wiki/Wikipedia:About', '//en.wikipedia.org/wiki/Wikipedia:Contact_us',
                'https://donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&utm_medium=sidebar&utm_campaign=C13_en.wikipedia.org&uselang=en',
                'wiki/Help:', 'Special', 'File', 'file', 'upload', '.svg', '.jpeg', '.png', '.gif', '.tiff', '.jpg',
                'wikimedia', '/User', 'Wikipedia_Signpost', 'WikiProject', 'Featured', 'ar.w', 'de.w', 'fa.w', 'ja.w', 'ru.w', 'tr.w', 'ta.w', 'eo.w', 'hyw.w', 'id.w', 'ko.w', 'et.w', 'es.w', 'fiu-vro.w', 'gl.w', 'he.w', 'fa:%', '/ar:%', '/tr:')

    for link in sampleInfo.find_all('a'):
        url = link.get("href", "")
        if not any(ext in url for ext in toRemove) and '/wiki/' in url:
            print(url)
            if not 'https://en.wikipedia.org/' in url:
                url = 'https://en.wikipedia.org/'+url
            links.append(url)
    return links

#returns string of the title of the webpages, a list
def pageSearchPrep(returnedLinks):
    print("       ")
    goodPages = []
    for link in returnedLinks:
        r = requests.get(link)
        pageInfo = BeautifulSoup(r.text, 'html.parser')
        t = pageInfo.title.string
        if not (t == 'Not Found'):
            t= t.replace(' - Wikipedia', '')
            print(t)
            goodPages.append(t)
    print(goodPages)
    return goodPages

def isBirdPage(page):
    categories = page.categories
    for title in sorted(categories.keys()):
        print(title, ".......", type(title))
        isBird = title.__contains__('bird') or title.__contains__('Bird')
        if isBird:
            return True
    return False

def birdSearch():
    print('bird search!')
    birdsFound, pagesSearched = 0, 0
    huntingGrounds = pageSearchPrep(gatherRelatedArticles(testerLink))
    for p in huntingGrounds:
        newPage = wiki_wiki.page(p)
        if newPage.exists():
            print('page is being searched...')
            if isBirdPage(newPage):
                birdsFound += 1
                print('Bird found! Do a new photo now')
                break
            pagesSearched += 1

    print(' ')
    print(f'Pages searched: {pagesSearched}......... Birds found: {birdsFound}')

birdSearch()


