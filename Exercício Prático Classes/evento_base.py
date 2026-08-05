from datetime import datetime, timedelta

class Evento:
    total_eventos = 0

    def __init__(self, titulo: str, data_hora: datetime, descricao: str):
        self.titulo = titulo
        self.data_hora = data_hora
        self.descricao = descricao
        self.is_concluido = False
        Evento.total_eventos += 1