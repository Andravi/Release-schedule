from time import sleep
import json
import requests

class AnimeAPI:
    def get_request(self, url_args: str) -> dict:
        """Faz o request e retorna o json_data
        :param - url_args: argumentos colocados na url para pegar o json
        :return - Json resposta na forma de Dict
        """
        try:
            response = requests.get(
                f"https://api.jikan.moe/v4/{url_args}", timeout=None
            )

            json_data = json.loads(response.text)
            return json_data

        except requests.exceptions.ConnectionError:
            print("Something bad ;-;")
            return None

    def lista_do_dia(self) -> list:  # Posso acabar usando muito essa
        """Diz os animes que lançam no dia informado

        return: list[dict{titulo, image, gerenos, dia e hora no brasil}, ...]"""
        anime_list = []
        current_page = 1
        data = self.get_request(f"seasons/now?page={current_page}")
        last_page = data["pagination"]["last_visible_page"]

        while last_page >= current_page:
            try:
                data = self.get_request(f"seasons/now?page={current_page}")
                for anime in data["data"]:
                    if anime["genres"]:
                        if "Hentai" in anime["genres"][0]["name"]:
                            continue
                        else:
                            anime_dict = {}
                            anime_dict["nome"] = anime["title"]
                            anime_dict["image"] = anime["images"]["jpg"]["image_url"]
                            anime_dict["time"] = get_day(anime["broadcast"])
                            anime_dict["generos"] = [genero["name"] for genero in anime["genres"]]
                            anime_list.append(anime_dict)
                current_page += 1

            except KeyError:
                print("Caiu em erro")
                if data['status'] == '429':
                    print('esperando')
                    sleep(3)
                    data = self.get_request(f"seasons/now?page={current_page}")


        return anime_list  # pode retornar uma lista de dicionarios com titulo, imagem e sinopse
        # To começando a gostar dessa ideia


def convert_day(days: str, mod: bool = False) -> str:
    """Converte os dias em inglês para portugues e modifica caso necessário"""

    week = [
        "Sundays",
        "Mondays",
        "Tuesdays",
        "Wednesdays",
        "Thursdays",
        "Fridays",
        "Saturdays",
    ]
    day_num = week.index(days) - 1 if mod else week.index(days)

    if week[day_num] == "Sundays":
        return "Domingos"

    elif week[day_num] == "Mondays":
        return "Segundas"

    elif week[day_num] == "Tuesdays":
        return "Terças"

    elif week[day_num] == "Wednesdays":
        return "Quartas"

    elif week[day_num] == "Thursdays":
        return "Quintas"

    elif week[day_num] == "Fridays":
        return "Sextas"

    elif week[day_num] == "Saturdays":
        return "Sábados"

    else:
        return "ERRO!"


def convert_hours(hours: str) -> str:
    """Converte O fuso horario japonês para o brasileiro"""
    time_zone = 12

    j_hours = int(hours[:2])
    if j_hours >= time_zone:
        br_hours = str(j_hours - time_zone)
    else:
        br_hours = str(j_hours + time_zone)

    return br_hours + hours[2:]


def get_day(data: dict) -> dict:  # pode fazer a conversão para o dia e horas do Brasil
    """diz quando o anime com o ID informado lança novos episodeos
    :param - id_mal
    :return - None
    """
    if data["time"]:
        if int(data["time"][:2]) - 12 <= 0:
            day = convert_day(data["day"], True)
        else:
            day = convert_day(data["day"])

        hours = convert_hours(data["time"])
    else:
        day = "(Incerto)"
        hours = "(Incerto)"

    return {"dia": day, "horas": hours}


def update_season_list(control: AnimeAPI):
    """Update the json of anime week days"""
    with open("weekAnimeDays.json", "w", encoding="utf-8") as f:
        json.dump(control.lista_do_dia(), f)


if __name__ == "__main__":
    api_control: AnimeAPI = AnimeAPI()
    # api_control.lista_do_dia()
    update_season_list(api_control)
