"""Anime Models"""


class AnimeCardModel:
    """Vai receber as informações e converter em dicionario"""

    def __init__(
        self,
        name: str = "Sem nome",
        image_source: str = "Sem imagem Encontrada",
        time: dict = None,
        sinopse: str = "Sem Sinopse",
        is_adult: bool = False,
    ) -> None:
        self.name = name
        self.image_source = image_source
        self.time = time
        self.is_adult = is_adult
        self.sinopse = sinopse

    def to_dict(self) -> dict:
        """Turn the object to Dict"""
        return {
            "name": self.name,
            "image_source": self.image_source,
            "time": self.time,
            "isAdult": self.is_adult,
            "sinopse": self.sinopse,
        }
