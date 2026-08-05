def __str__(self):
        return f"Evento: {self.titulo}, Data: {self.data_hora}, Descrição: {self.descricao}, Concluido: {self.is_concluido}"

    def __eq__(self, outro):
        return self.data_hora == outro.data_hora if isinstance(outro, Evento) else False

    def __ne__(self, outro):
        return self.data_hora != outro.data_hora if isinstance(outro, Evento) else True

    def __lt__(self, outro):
        return self.data_hora < outro.data_hora if isinstance(outro, Evento) else NotImplemented

    def __le__(self, outro):
        return self.data_hora <= outro.data_hora if isinstance(outro, Evento) else NotImplemented

    def __gt__(self, outro):
        return self.data_hora > outro.data_hora if isinstance(outro, Evento) else NotImplemented

    def __ge__(self, outro):
        return self.data_hora >= outro.data_hora if isinstance(outro, Evento) else NotImplemented