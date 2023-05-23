from cores import *

class galaxy():
    def __init__(self, rect):
        self.rect = rect
        self.dic_entidades = {}
        self.entidades_id = 0

    def add_entidade(self, entidade):
        self.dic_entidades[self.entidades_id] = entidade
        entidades_id = self.entidades_id
        self.entidades_id += 1

    def update(self, time_passed, event_list):
        time_passed_seconds = time_passed / 1000.0
        for entidade in self.dic_entidades.values():
            entidade.upadate(time_passed, event_list)

    def render(self, surface):
        for entidade in self.dic_entidades.values():
            entidade.render(surface)
