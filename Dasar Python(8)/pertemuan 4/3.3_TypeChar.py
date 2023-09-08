import PySimpleGUI as sg

sg.theme('BluePurple')

layout=[[sg.Text('Your typed chars appear here:'), sg.Text(size=(15,1), key='-OUTPUT-')],
        [sg.Input(key='-IN-')],
        [sg.Button('Show'), sg.Button('Exit')]]

window=sg.Window('Pattern 2B', layout)

while True: 
    event, value=window.read()
    print(event, value)
    if event==sg.WIN_CLOSED or event == 'Exit':
        break
    if event=="Show":
        window['-OUTPUT-'].update(value['-IN-'])


window.close