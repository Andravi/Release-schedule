import json
import requests


def get_request(url_args: str) -> dict:
    """ Faz o request e retorna o json_data
    :param - url_args: argumentos colocados na url para pegar o json
    :return - Json resposta na forma de Dict
    """
    try:
        response = requests.get(f"https://api.jikan.moe/v4/{url_args}", timeout=10)

        json_data = json.loads(response.text)
        return json_data

    except requests.exceptions.ConnectionError:
        print('Something bad ;-;')
        return None


def get_day(id_mal: int):
    """ diz quando o anime com o ID informado lança novos episodeos
    :param - id_mal
    :return - None
    """
    data = get_request(f"anime/{id_mal}")

    day  = data["data"]["broadcast"]["day"]
    nome = data["data"]["title"]
    time  = data["data"]["broadcast"]["time"]

    print(f"\nO anime {nome} lança um episodio novo as {time} de {day}\n")


def lista_do_dia(day:str):
    """ Diz os animes que lançam no dia informado"""
    current_page = 1
    data = get_request(f"seasons/now?page={current_page}")

    while data["pagination"]["last_visible_page"] >= current_page:
        # print(current_page)
        for title in data["data"]:
            if title["broadcast"]["day"] == day:
                print(title["title"], f"id={title['mal_id']},\n")

        current_page += 1
        data = get_request(f"seasons/now?page={current_page}")



get_day(id_mal=1)
#lista_do_dia("Mondays")
