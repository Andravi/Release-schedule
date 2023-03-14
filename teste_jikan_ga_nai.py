import json
import requests


def get_day(id_mal: int):
    """ diz quando o anime com o ID informado lança novos episodeos
    :param - id_mal
    :return - 
    """
    try:
        response = requests.get(f"https://api.jikan.moe/v4/anime/{id_mal}", timeout=10)

        json_data = json.loads(response.text)
    except requests.exceptions.ConnectionError:
        pass
    # print(json.dumps(json_data, indent=4))


    nome = json_data["data"]["title"]
    day  = json_data["data"]["broadcast"]["day"]
    time  = json_data["data"]["broadcast"]["time"]

    print(f"\nO anime {nome} lança um episodio novo as {time} de {day}\n")


def lista_do_dia(day:str):
    """ Diz os animes que lançam no dia informado"""
    current_page = 1
    response = requests.get(f"https://api.jikan.moe/v4/seasons/now?page={current_page}", timeout=10) # Criar uma função para a respostas e load de json seria uma boa
    json_data = json.loads(response.text)

    while json_data["pagination"]["last_visible_page"] >= current_page:
        # print(current_page)
        for title in json_data["data"]:
            if title["broadcast"]["day"] == day:
                print(title["title"], f"id={title['mal_id']},\n")

        current_page += 1
        response = requests.get(f"https://api.jikan.moe/v4/seasons/now?page={current_page}", timeout=10)
        json_data = json.loads(response.text)



get_day(id_mal=51815)
#lista_do_dia("Mondays")
