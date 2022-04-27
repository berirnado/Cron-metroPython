import PySimpleGUI as sg

sg.theme('black')
layout = [
    [sg.Text('time')],
    [sg.Button('Start'), sg.Button('Lap')]
]

window = sg.Window(
        'Cronômetro', 
        layout,
        size = (300, 300),
        no_titlebar = True
    )

while True:
    event, values = window.read()
    if event == (sg.WIN_CLOSED, 'Start'):
        break

window.close()