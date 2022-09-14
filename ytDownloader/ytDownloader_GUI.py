import PySimpleGUI as sg
import ytDownloader as Ytd

# Define the window's contents
layout = [[sg.Text("Please enter Youtube Url:")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40, 1), key='-OUTPUT-')],
          [sg.Button('Download'), sg.Button('Quit')]]

# Creates the window
window = sg.Window('My Simple YouTube Downloader', layout)



# Checking for an event on the window
while True:
    event, values = window.read()
    url = values['-INPUT-']
    # If user clicked Download button and no input
    if event == 'Download' and url == "":
        window['-OUTPUT-'].update("Download What?")
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Download button clicked
    if event == 'Download' and url != "":
        Ytd.get_video(url)
        sg.popup(Ytd.get_title(url) + " downloaded!")
        window['-INPUT-'].update("")

# Finish up by removing from the screen
window.close()
