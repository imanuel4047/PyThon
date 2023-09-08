import PySimpleGUI as sg

layout=[[sg.Button('Klik saya')]]

window=sg.Window('Contoh PRogram PySimpleGUI', layout)

while True:
    event, values=window.read()
    if event==sg.WINDOW_CLOSED:
        break
    elif event=='Klik saya':
        print('Tombol diklik')

window.close()