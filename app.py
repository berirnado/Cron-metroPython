import PySimpleGUI as sg
from time import time

def create_window():
    sg.theme('black')
    layout = [

        [
            sg.Push(), 
            sg.Button('X', font = 'Young 20', size=(2, 1), key = "-CLOSEBTN-", button_color=("#FFFFFF", "#FF0000"), border_width = 0)
        ],
        [sg.VPush()],
        [sg.Text('0', font = 'Young 50', key='-TIME-')],
        [
            sg.Button('Start', font = 'Young 20', button_color=("#FFFFFF", "#FF0000"), border_width = 0, key="-STARTSTOP-"),
            sg.Button('Lap', font = 'Young 20', button_color=("#FFFFFF", "#FF0000"), border_width = 0, key='-LAP-', visible=False)
        ],
        [sg.Column([[]], key='-LAPS-')],
        [sg.VPush()]
    ]

    return sg.Window(
            'Cronômetro', 
            layout,
            size = (300, 400),
            no_titlebar = True,
            element_justification= 'center'
        )



window = create_window()
start_time = 0
active = False
laps = 0


while True:
    event, values = window.read(timeout = 10)
    if event in (sg.WIN_CLOSED, '-CLOSEBTN-'):
        break

    if event == '-STARTSTOP-':
        if active:
            active = False
            window['-STARTSTOP-'].update('Reset')
            window['-LAP-'].update(visible = False)
        else:
            if start_time > 0:
                window.close()
                window = create_window()
                start_time = 0
                laps = 0
            else:
                active = True
                start_time = time()
                window['-STARTSTOP-'].update('Stop')
                window['-LAP-'].update(visible = True)

    if active:
        elapsed_time =  round(time() - start_time,1)
        window['-TIME-'].update(elapsed_time)

    if event == '-LAP-':
        laps += 1
        window.extend_layout(window['-LAPS-'], [[sg.Text(laps),sg.VSeparator(),sg.Text(round(time() - start_time,1), font='Young 12')]])
        print(round(time() - start_time,1))

window.close()