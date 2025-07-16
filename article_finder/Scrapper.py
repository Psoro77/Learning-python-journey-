import requests
from bs4 import BeautifulSoup
import json
from Ai_intface import Ai_intface

class Scrapper :
    def __init__(self):
        url = []
        responses = []
        html =[]
        pagedt = {}
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/116.0.0.0 Safari/537.36'
        }

        # ------------------------------------------------------------------------------------------------------
        def gettitle(soup):
            title = soup.title.text.strip()
            return title

        def getartcltechrunch(soup):
            items_a = soup.find_all('a', class_='loop-card__title-link')
            itemlist =[]
            for item in items_a :
                itemlist.append(item.text.strip())
            
            items = dict(zip(itemlist, itemlist))
            return items


        def getartcl_artcnica(soup):

            items_a = soup.find_all('a', class_=[
            'dusk:text-gray-100',
            'dusk:visited:text-gray-400',
            'dusk:hover:text-orange-400',
            'text-gray-700',
            'visited:text-gray-400',
            'hover:text-orange-400',
            'dark:text-gray-100',
            'dark:visited:text-gray-400',
            'dark:hover:text-orange-400'
            ])

            items_p = soup.find_all('p', class_=[
                'text-gray-550',
                'dark:text-gray-250',
                'dusk:text-gray-250',
                'mb-2',
                'text-lg',
                'leading-tight'
            ])
            artitle = []
            artclecontent = []
            for item1, item2 in zip(items_a, items_p) :
                artitle.append(item1.text.strip())
                artclecontent.append(item2.text.strip())

            items = dict(zip(artitle, artclecontent))
            return items
        # data processing
        # ---------------------------------------------------------------------------------------------------------------
        while (True) :
            print('enter url : s to stop')
            enter = str(input())
            if (enter == 's' or enter == 'S') :
                break
            url.append(enter)

        for i in range(0, len(url)):
            try :
                responses.append(requests.get(url[i], timeout= 10 ,headers= header))
                responses[i].raise_for_status()  #  exception if erreur HTTP
                html.append(responses[i].text)
            except requests.RequestException as e:
                print(f"Erreur pour {url[i]} : {e}")

        # triatement de la page html 
        webptitles= []
        articles = []
        for page_html in html :
            soup = BeautifulSoup(page_html, 'html.parser')
            title =(gettitle(soup))
            webptitles.append(title)
            # choose the right type of method because of diff website 
            if ('TechCrunch' in title):
                articles.append(getartcltechrunch(soup))
            elif('Ars Technica' in title) : 
                articles.append(getartcl_artcnica(soup))
            else : 
                print(f"Unsupported website for title: {title}")
                
        dtglob = dict(zip(webptitles,articles))
        # fichier en mode ecriture 
        with open('C:\\Users\\USER\\Documents\\projet&code\\Python\\Learning-python-journey-\\article_finder\\json\\daily_tech.json', 'w', encoding='utf-8') as fichier :
            json.dump(dtglob, fichier, indent=4,)
        Ai_intface()
