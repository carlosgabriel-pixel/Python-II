def isConcluido(self):
        if self.data_hora < datetime.now():
            self.is_concluido = True
        return self.is_concluido

    @classmethod
    def num_eventos(cls):
        return cls.total_eventos

    @staticmethod
    def valida_evento(nome, data_hora, descricao):
        valido_nome = isinstance(nome, str)
        valido_data = isinstance(data_hora, datetime)
        valido_desc = isinstance(descricao, str)
        return valido_nome and valido_data and valido_desc