import PySimpleGUI as sg


class TelaFeira:

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        opcao = None
        button, values = self.open()
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['4']:
            opcao = 4
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        # Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0'] or button in (None, 'Voltar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('Green')
        layout = [
            [sg.Text('Gerenciamento de feiras', font=("Helvica", 22))],
            [sg.Text('Escolha sua opção', font=("Helvica", 13))],
            [sg.Radio('Incluir feira', "RD1", key='1')],
            [sg.Radio('Excluir feira', "RD1", key='2')],
            [sg.Radio('Listar feiras', "RD1", key='3')],
            [sg.Radio('Alterar feiras', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Gerenciamento de feiras').Layout(layout)

    def pegar_dados_feira(self):
        sg.ChangeLookAndFeel('Green')
        layout = [
            [sg.Text("Cadastre a feira", font=("Helvica", 16), size=(15, 1))],
            [sg.Text("*Id", size=(15, 1)), sg.InputText(key="it_id", size=(6, 1))],
            [sg.Text("*Dia(s) da Semana:"),
            sg.Checkbox("Domingo", key="domingo"),
            sg.Checkbox("Segunda", key="segunda"),
            sg.Checkbox("Terça", key="terca"),
            sg.Checkbox("Quarta", key="quarta"),
            sg.Checkbox("Quinta", key="quinta"),
            sg.Checkbox("Sexta", key="sexta"),
            sg.Checkbox("Sábado", key="sabado")],
            [sg.Text("*Município", size=(15, 1)), sg.InputText(key="it_municipio")],
            [sg.Text("*Logradouro", size=(15, 1)), sg.InputText(key="it_logradouro")],
            [sg.Text("*Número", size=(15, 1)), sg.InputText(key="it_numero_logradouro", size=(6, 1))],
            [sg.HorizontalSeparator()],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Gerenciemento de feiras').Layout(layout)

        button, values = self.open()
        if button in (None, "Cancelar"):
            self.close()
            return
        id = int(values['it_id'])

        dias_semana = []
        if values['domingo']:
            dias_semana.append("domingo")
        if values['segunda']:
            dias_semana.append("segunda-feira")
        if values['terca']:
            dias_semana.append("terça-feira")
        if values['quarta']:
            dias_semana.append("quarta-feira")
        if values['quinta']:
            dias_semana.append("quinta-feira")
        if values['sexta']:
            dias_semana.append("sexta-feira")
        if values['sabado']:
            dias_semana.append("sábado")

        if len(dias_semana) == 0:
            raise ValueError

        municipio = values['it_municipio']
        logradouro = values['it_logradouro']
        numero_logradouro = int(values['it_numero_logradouro'])

        self.close()
        return {"id_feira": id, "dias_semana_feira": dias_semana, "municipio_feira": municipio,
                "logradouro_feira": logradouro, "numero_logradouro_feira": numero_logradouro}

    def selecionar_feira(self, dados_feiras):
        sg.ChangeLookAndFeel('Green')
        feira_layout = []

        for feira in dados_feiras:
            feira_id = feira["id_feira"]
            feira_dias_semana = feira["dias_semana_feira"]
            feira_municipio = feira["municipio_feira"]
            feira_logradouro = feira["logradouro_feira"]
            feira_numero_logradouro = feira["numero_logradouro_feira"]

            radio_key = f'feira_{feira_id}'

            feira_dias_semana_str = ', '.join(feira_dias_semana)

            feira_info = [
                [sg.Text(f"Feira {feira_id}", font=("Helvetica", 16), size=(15, 1))],
                [sg.Text(f"Id: {feira_id}", size=(15, 1))],
                [sg.Text(f"Dia(s) da semana: {feira_dias_semana_str}")],
                [sg.Text(f"Município: {feira_municipio}")],
                [sg.Text(f"Logradouro: {feira_logradouro}")],
                [sg.Text(f"Número: {feira_numero_logradouro}")],
                [sg.Radio(f'Selecionar feira {feira_id}', 'RD1', key=radio_key)],
                [sg.HorizontalSeparator()],
            ]

            feira_layout.extend(feira_info)

        column_layout = sg.Column(feira_layout, size=(400, 300), scrollable=True)

        layout = [
            [column_layout],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]

        self.__window = sg.Window('Gerenciamento de feiras').Layout(layout)

        while True:
            event, values = self.__window.Read()

            if event in (None, 'Voltar'):
                self.__window.Close()
                break

            elif event == 'Confirmar':
                selected_feira_id = None

                for feira in dados_feiras:
                    radio_key = f'feira_{feira["id_feira"]}'  # Calculate the radio key for each feira
                    if values[radio_key]:
                        selected_feira_id = feira["id_feira"]
                        break

                self.__window.Close()

                return selected_feira_id

    def listar_feiras(self, dados_feiras):
        sg.ChangeLookAndFeel('Green')
        feira_layout = []

        for feira in dados_feiras:
            feira_id = feira["id_feira"]
            feira_dias_semana = feira["dias_semana_feira"]
            feira_municipio = feira["municipio_feira"]
            feira_logradouro = feira["logradouro_feira"]
            feira_numero_logradouro = feira["numero_logradouro_feira"]

            feira_dias_semana_str = ', '.join(feira_dias_semana)

            feira_info = [
                [sg.Text(f"Feira {feira_id}", font=("Helvetica", 16), size=(15, 1))],
                [sg.Text(f"Id: {feira_id}", size=(15, 1))],
                [sg.Text(f"Dia(s) da semana: {feira_dias_semana_str}")],
                [sg.Text(f"Município: {feira_municipio}")],
                [sg.Text(f"Logradouro: {feira_logradouro}")],
                [sg.Text(f"Número: {feira_numero_logradouro}")],
                [sg.HorizontalSeparator()],
            ]

            feira_layout.extend(feira_info)

        column_layout = sg.Column(feira_layout, size=(400, 300), scrollable=True)

        layout = [
            [column_layout],
            [sg.Cancel('Voltar')]
        ]

        self.__window = sg.Window('Gerenciamento de feiras').Layout(layout)

        while True:
            event, values = self.__window.Read()

            if event in (None, 'Voltar'):
                self.__window.Close()
                break

    def alterar_feira(self, dados_feira):
        sg.ChangeLookAndFeel('Green')

        checkbox_values = {
            'domingo': False,
            'segunda-feira': False,
            'terça-feira': False,
            'quarta-feira': False,
            'quinta-feira': False,
            'sexta-feira': False,
            'sábado': False
        }

        for weekday in dados_feira["dias_semana_feira"]:
            checkbox_values[weekday.lower()] = True

        layout = [
            [sg.Text("Alterar feira", font=("Helvica", 16), size=(15, 1))],
            [sg.Text(f"Id: {dados_feira['id_feira']}", size=(15, 1))],
            [sg.Text("*Dia(s) da semana", size=(15, 1)),
             sg.Checkbox("Domingo", key="domingo", default=checkbox_values['domingo']),
             sg.Checkbox("Segunda", key="segunda", default=checkbox_values['segunda-feira']),
             sg.Checkbox("Terça", key="terca", default=checkbox_values['terça-feira']),
             sg.Checkbox("Quarta", key="quarta", default=checkbox_values['quarta-feira']),
             sg.Checkbox("Quinta", key="quinta", default=checkbox_values['quinta-feira']),
             sg.Checkbox("Sexta", key="sexta", default=checkbox_values['sexta-feira']),
             sg.Checkbox("Sábado", key="sabado", default=checkbox_values['sábado'])],
            [sg.Text("*Município", size=(15, 1)), sg.InputText(dados_feira["municipio_feira"], key="it_municipio")],
            [sg.Text("*Logradouro", size=(15, 1)), sg.InputText(dados_feira["logradouro_feira"], key="it_logradouro")],
            [sg.Text("*Número", size=(15, 1)), sg.InputText(dados_feira["numero_logradouro_feira"], \
                                                            key="it_numero_logradouro", size=(6, 1))],
            [sg.HorizontalSeparator()],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Gerenciamento de feiras').Layout(layout)

        button, values = self.open()
        if button in (None, "Cancelar"):
            self.close()
            return None

        dias_semana = []
        if values['domingo']:
                dias_semana.append("domingo")
        if values['segunda']:
            dias_semana.append("segunda-feira")
        if values['terca']:
            dias_semana.append("terça-feira")
        if values['quarta']:
            dias_semana.append("quarta-feira")
        if values['quinta']:
            dias_semana.append("quinta-feira")
        if values['sexta']:
            dias_semana.append("sexta-feira")
        if values['sabado']:
            dias_semana.append("sábado")

        if len(dias_semana) == 0:
            raise ValueError

        municipio = values['it_municipio']
        logradouro = values['it_logradouro']
        numero_logradouro = int(values['it_numero_logradouro'])

        self.close()
        return {"id_feira": id, "dias_semana_feira": dias_semana, "municipio_feira": municipio,
                "logradouro_feira": logradouro, "numero_logradouro_feira": numero_logradouro}

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def mostrar_mensagem(self, msg):
        sg.popup("", msg)