import crawlers.object


def getCheapestExclusiveItems():
    from bs4 import BeautifulSoup
    from requests import get

    url = 'https://steamcommunity.com/market/search/render/?query=&start=0&count=10&search_descriptions=0&sort_column=price&sort_dir=asc&appid=730&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Quality%5B%5D=tag_unusual&category_730_Quality%5B%5D=tag_unusual_strange'
    page = get(url) # Pobranie źródła strony strony
    json = page.json() # Przerobienie źródła na jsona (w tym przypadku taki format strony zwraca get)
    bs = BeautifulSoup(json["results_html"]) # stworzenie obiektu BeautifulSoup z danymi pobranymi z obiektu results_html z jsona

    exclusiveItemList = []
    for exclusiveItemPrice in bs.find_all(lambda tag: tag.name == 'span' and tag.get('class') == ['normal_price']): # wykorzystanie wyrażenia lambda pozwala uzyskać klase o dokłądnej nazwie (normalnie pobierane również klasy zawirające nazwę)
        exclusiveItemList.append(crawlers.object.item('',exclusiveItemPrice.attrs['data-price'])) # pobranie wartości z atrybutu 'data-price'

    i = 0
    for exclusiveItemName in bs.find_all(lambda tag: tag.name == 'span' and tag.get('class') == ['market_listing_item_name']):
        exclusiveItemList[i].name = exclusiveItemName.text
        i += 1

    for item in exclusiveItemList:
        print(item.name, item.price)

