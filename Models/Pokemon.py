from requests_html import HTMLSession
import  os
from  dotenv import load_dotenv

load_dotenv()

#retornar pokemon como un diccionario
def get_data_pokemon(name,types,attacks):
     return {
         "name": name,
         "current_health": 100,
         "base_health": 100,
         "level": 1,
         "type": types,
         "attacks": attacks,
         "current_exp": 0
     }


#obtener la informacion base de los pokemon de la url de la wiki
def get_pokemon(index):
    url="{} {}".format(os.environ["URL_BASE"],index)
    session=HTMLSession()
    pokemon_page=session.get(url)
    name=pokemon_page.html.find(".mini",first=True).text
    type=[]

    for img in pokemon_page.html.find(".pkmain",first=True).find(".bordeambos",first=True).find("img"):
         type.append(img.attrs["alt"])

    attacks=[]

    for attack_item in  pokemon_page.html.find(".pkmain")[-1].find("tr.check3"):
        attack={
            "name":attack_item.find("td",first=True).find("a",first=True).text,
            "type":attack_item.find("td")[1].find("img",first=True).attrs["alt"],
            "min_level":attack_item.find("th",first=True).text,
            "damage":int(attack_item.find("td")[4].text),

        }
        attacks.append(attack)


    return get_data_pokemon(name,type,attacks)


