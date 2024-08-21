import PySimpleGUI as sg

# Função para buscar uma matéria pelo nome
def find_subject(subjects, name):
    for subject in subjects:
        if subject['name'].lower() == name.lower():
            return subject
    return None

# Lista de matérias escolares com contagem de votos
subjects = []

# Layout da interface
layout = [
    [sg.Text("Cadastro e Votação de Matérias Escolares", font=("Helvetica", 16))],
    [sg.Text("Nome da Matéria:", size=(15, 1)), sg.InputText(key='subject_name')],
    [sg.Button("Cadastrar/Votar", size=(15, 1)), sg.Button("Sair", size=(10, 1))],
    [sg.Text("Matérias Cadastradas e Votos:", font=("Helvetica", 14), pad=((0, 0), (20, 5)))],
    [sg.Listbox(values=[], size=(40, 10), key='subject_list', select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, enable_events=True)],
]

# Criação da janela
window = sg.Window("Cadastro de Matérias", layout, finalize=True)

# Loop de eventos
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Sair':
        break

    if event == 'Cadastrar/Votar':
        subject_name = values['subject_name'].strip()

        if subject_name:
            # Verifica se a matéria já está na lista
            subject = find_subject(subjects, subject_name)
            if subject:
                subject['votes'] += 1
            else:
                # Adiciona nova matéria com 1 voto
                subjects.append({'name': subject_name, 'votes': 1})

            # Atualiza a lista de matérias na interface
            window['subject_list'].update([f"{sub['name']} - Votos: {sub['votes']}" for sub in subjects])

# Fechamento da janela
window.close()
