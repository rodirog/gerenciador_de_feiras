from limite.telaFeira import TelaFeira
from entidade.Feira import Feira
from entidade.DiaSemanaEnum import DiaSemana
from persistencia.feiraDao import FeiraDAO


class ControladorFeira:
    def __init__(self):
        self.__tela_feira = TelaFeira()
        self.__feira_dao = FeiraDAO()

    def iniciar(self):
        self.mostrar_tela_opcoes()

    def mostrar_tela_opcoes(self):
        opcoes = {1: self.incluir_feira,
                  2: self.excluir_feira,
                  3: self.listar_feiras,
                  4: self.alterar_feira}

        while True:
            opcao = self.__tela_feira.tela_opcoes()
            if opcao == 0:
                break
            opcoes[opcao]()

    def incluir_feira(self):
        ja_existe = False
        try:
            dados_feira = self.__tela_feira.pegar_dados_feira()
        except ValueError:
            self.__tela_feira.mostrar_mensagem("Cadastro nao efetuado. \
                                                Houve um erro na inserção dos dados!")
            self.__tela_feira.close()
            return

        if dados_feira:
            for feira in self.__feira_dao.get_all():

                if dados_feira["id_feira"] == feira.id:
                    self.__tela_feira.mostrar_mensagem("Uma feira com este id já existe!")
                    ja_existe = True

            if not ja_existe:
                feira = Feira(dados_feira["dias_semana_feira"],
                                         dados_feira["id_feira"],
                                         dados_feira["municipio_feira"],
                                         dados_feira["logradouro_feira"],
                                         dados_feira["numero_logradouro_feira"])

                self.__feira_dao.add(feira)
                self.__tela_feira.mostrar_mensagem("Feira inclusa com sucesso!")

    def excluir_feira(self):
        dados_feiras = []
        feiras = self.__feira_dao.get_all()

        for feira in feiras:
            dados_feiras.append({"id_feira": feira.id,
                                   "dias_semana_feira": feira.dias_semana,
                                   "municipio_feira": feira.municipio,
                                   "logradouro_feira": feira.logradouro,
                                   "numero_logradouro_feira": feira.numero_logradouro})

        id_feira_a_excluir = self.__tela_feira.selecionar_feira(dados_feiras)

        if id_feira_a_excluir:
            self.__feira_dao.remove(id_feira_a_excluir)
            self.__tela_feira.mostrar_mensagem("Feira excluída com sucesso!")

    def listar_feiras(self):
        dados_feiras = []
        feiras = self.__feira_dao.get_all()

        for feira in feiras:
            dados_feiras.append({"id_feira": feira.id,
                                   "dias_semana_feira": feira.dias_semana,
                                   "municipio_feira": feira.municipio,
                                   "logradouro_feira": feira.logradouro,
                                   "numero_logradouro_feira": feira.numero_logradouro})

        self.__tela_feira.listar_feiras(dados_feiras)

    def alterar_feira(self):
        dados_feiras = []
        feiras = self.__feira_dao.get_all()

        for feira in feiras:
            dados_feiras.append({"id_feira": feira.id,
                                 "dias_semana_feira": feira.dias_semana,
                                 "municipio_feira": feira.municipio,
                                 "logradouro_feira": feira.logradouro,
                                 "numero_logradouro_feira": feira.numero_logradouro})

        id_feira_a_alterar = self.__tela_feira.selecionar_feira(dados_feiras)

        if id_feira_a_alterar:
            feira_a_alterar = self.__feira_dao.get(id_feira_a_alterar)

            dados_feira = {"id_feira": feira_a_alterar.id,
                             "dias_semana_feira": feira_a_alterar.dias_semana,
                             "municipio_feira": feira_a_alterar.municipio,
                             "logradouro_feira": feira_a_alterar.logradouro,
                             "numero_logradouro_feira": feira_a_alterar.numero_logradouro}
            try:
                novos_dados_feira = self.__tela_feira.alterar_feira(dados_feira)
            except ValueError:
                self.__tela_feira.mostrar_mensagem("Alteração nao efetuada. \
                                                    Houve um erro na inserção dos dados!")
                self.__tela_feira.close()
                return

            if novos_dados_feira:

                feira_a_alterar.dias_semana = novos_dados_feira["dias_semana_feira"]
                feira_a_alterar.municipio = novos_dados_feira["municipio_feira"]
                feira_a_alterar.logradouro = novos_dados_feira["logradouro_feira"]
                feira_a_alterar.numero_logradouro = novos_dados_feira["numero_logradouro_feira"]

                self.__feira_dao.update()

                self.__tela_feira.mostrar_mensagem("Feira alterada com sucesso!")
