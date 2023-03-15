import json
import requests

def get_request(url_args: str) -> dict:
    """ Faz o request e retorna o json_data
    :param - url_args: argumentos colocados na url para pegar o json
    :return - Json resposta na forma de Dict
    """
    try:
        response = requests.get(f"https://api.jikan.moe/v4/{url_args}", timeout=None)

        json_data = json.loads(response.text)
        return json_data

    except requests.exceptions.ConnectionError:
        print('Something bad ;-;')
        return None


def get_day(id_mal: int): # pode fazer a conversão para o dia e horas do Brasil
    """ diz quando o anime com o ID informado lança novos episodeos
    :param - id_mal
    :return - None
    """
    data = get_request(f"anime/{id_mal}")

    day  = data["data"]["broadcast"]["day"]
    nome = data["data"]["title"]
    time  = data["data"]["broadcast"]["time"]

    print(f"\nO anime {nome} lança um episodio novo as {time} de {day}\n")


def lista_do_dia(day:str) -> list: # Posso acabar usando muito essa
    """ Diz os animes que lançam no dia informado
    
    return: [dict{titulo, image, gerenos, dia e hora no brasil}, ...]"""
    anime_list = []
    current_page = 1
    data = get_request(f"seasons/now?page={current_page}")

    while data["pagination"]["last_visible_page"] >= current_page:
        for anime in data["data"]:
            if anime["broadcast"]["day"] == day:
                anime_dict = {}
                anime_dict["nome"] = anime["title"]
                anime_dict["image"] = anime["images"]["jpg"]["image_url"]
                anime_list.append(anime_dict)
                # anime_list["novo_ep"] = get_day(anime["broadcast"])

        current_page += 1
        data = get_request(f"seasons/now?page={current_page}")
    return anime_list # pode retornar uma lista de dicionarios com titulo, imagem e sinopse # To começando a gostar dessa ideia


#get_day(id_mal=50287)
print(lista_do_dia("Mondays"))
#print(json.dumps(get_request("seasons/now"), indent=4))
