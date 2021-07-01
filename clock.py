#First I import all the modules I need
import PySimpleGUI as sg
from datetime import datetime

#The I create a list for the layout
months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']

#I identify what day it is
date = datetime.now().day
#I print it to see if it works
print(date)

#Now, I make sure I identify what month it is now.
cur_month = datetime.now().month
#I print it to make sure it works
print(cur_month)

#I identify what minute it is
cur_min = datetime.now().minute
#I print it to make sure it works
print(cur_min)

#I identify what hour it is
cur_hour = datetime.now().hour
#I print it to see if it works
print(cur_hour)


#I created this many layouts so I have a selection of which one to pick based on which month, hour, and minute it is
layout = [[sg.Text(months[0], background_color='#277533'), sg.Text(months[1]), sg.Text(months[2]),
          sg.Text(months[3]),
           sg.Text(months[4]), sg.Text(months[5]), sg.Text(months[6]), sg.Text(months[7]),
           sg.Text(months[8]), sg.Text(months[9]), sg.Text(months[10]), sg.Text(months[11])],
          [sg.Text("Day: "), sg.Text(date), sg.Text("Hour:"), sg.Text(cur_hour), sg.Text("Minute:"), sg.Text(cur_min)]]

layout1 = [[sg.Text(months[0]), sg.Text(months[1], background_color='#277533'), sg.Text(months[2]),
          sg.Text(months[3]),
           sg.Text(months[4]), sg.Text(months[5]), sg.Text(months[6]), sg.Text(months[7]),
           sg.Text(months[8]), sg.Text(months[9]), sg.Text(months[10]), sg.Text(months[11])],
          [sg.Text("Day: "), sg.Text(date), sg.Text("Hour:"), sg.Text(cur_hour), sg.Text("Minute:"), sg.Text(cur_min)]]

layout2 = [[sg.Text(months[0]), sg.Text(months[1]), sg.Text(months[2], background_color='#277533'),
          sg.Text(months[3]),
           sg.Text(months[4]), sg.Text(months[5]), sg.Text(months[6]), sg.Text(months[7]),
           sg.Text(months[8]), sg.Text(months[9]), sg.Text(months[10]), sg.Text(months[11])],
          [sg.Text("Day: "), sg.Text(date), sg.Text("Hour:"), sg.Text(cur_hour), sg.Text("Minute:"), sg.Text(cur_min)]]

layout3 = [[sg.Text(months[0]), sg.Text(months[1]), sg.Text(months[2]),
          sg.Text(months[3], background_color='#277533'),
           sg.Text(months[4]), sg.Text(months[5]), sg.Text(months[6]), sg.Text(months[7]),
           sg.Text(months[8]), sg.Text(months[9]), sg.Text(months[10]), sg.Text(months[11])],
          [sg.Text("Day: "), sg.Text(date), sg.Text("Hour:"), sg.Text(cur_hour), sg.Text("Minute:"), sg.Text(cur_min)]]

layout4 = [[sg.Text(months[0]), sg.Text(months[1]), sg.Text(months[2]),
          sg.Text(months[3]),
           sg.Text(months[4], background_color='#277533'), sg.Text(months[5]), sg.Text(months[6]), sg.Text(months[7]),
           sg.Text(months[8]), sg.Text(months[9]), sg.Text(months[10]), sg.Text(months[11])],
          [sg.Text("Day: "), sg.Text(date), sg.Text("Hour:"), sg.Text(cur_hour), sg.Text("Minute:"), sg.Text(cur_min)]]

layout5 = [[sg.Text(months[0]), sg.Text(months[1]), sg.Text(months[2]),
          sg.Text(months[3]),
           sg.Text(months[4]), sg.Text(months[5], background_color='#277533'), sg.Text(months[6]), sg.Text(months[7]),
           sg.Text(months[8]), sg.Text(months[9]), sg.Text(months[10]), sg.Text(months[11])],
          [sg.Text("Day: "), sg.Text(date), sg.Text("Hour:"), sg.Text(cur_hour), sg.Text("Minute:"), sg.Text(cur_min)]]

layout6 = [[sg.Text(months[0]), sg.Text(months[1]), sg.Text(months[2]), sg.Text(months[3]),
           sg.Text(months[4]), sg.Text(months[5]), sg.Text(months[6], background_color='#277533'),
           sg.Text(months[7]),
           sg.Text(months[8]), sg.Text(months[9]), sg.Text(months[10]), sg.Text(months[11])],
          [sg.Text("Day: "), sg.Text(date), sg.Text("Hour:"), sg.Text(cur_hour), sg.Text("Minute:"), sg.Text(cur_min)]]

layout7 = [[sg.Text(months[0]), sg.Text(months[1]), sg.Text(months[2]),
          sg.Text(months[3]),
           sg.Text(months[4]), sg.Text(months[5]), sg.Text(months[6]), sg.Text(months[7], background_color='#277533'),
           sg.Text(months[8]), sg.Text(months[9]), sg.Text(months[10]), sg.Text(months[11])],
          [sg.Text("Day: "), sg.Text(date), sg.Text("Hour:"), sg.Text(cur_hour), sg.Text("Minute:"), sg.Text(cur_min)]]

layout8 = [[sg.Text(months[0]), sg.Text(months[1]), sg.Text(months[2]),
          sg.Text(months[3]),
           sg.Text(months[4]), sg.Text(months[5]), sg.Text(months[6]), sg.Text(months[7]),
           sg.Text(months[8], background_color='#277533'), sg.Text(months[9]), sg.Text(months[10]),
            sg.Text(months[11])],
          [sg.Text("Day: "), sg.Text(date), sg.Text("Hour:"), sg.Text(cur_hour), sg.Text("Minute:"), sg.Text(cur_min)]]

layout9 = [[sg.Text(months[0]), sg.Text(months[1]), sg.Text(months[2]),
          sg.Text(months[3]),
           sg.Text(months[4]), sg.Text(months[5]), sg.Text(months[6]), sg.Text(months[7]),
           sg.Text(months[8]), sg.Text(months[9], background_color='#277533'), sg.Text(months[10]),
            sg.Text(months[11])],
          [sg.Text("Day: "), sg.Text(date), sg.Text("Hour:"), sg.Text(cur_hour), sg.Text("Minute:"), sg.Text(cur_min)]]

layout10 = [[sg.Text(months[0]), sg.Text(months[1]), sg.Text(months[2]),
          sg.Text(months[3]),
           sg.Text(months[4]), sg.Text(months[5]), sg.Text(months[6]), sg.Text(months[7]),
           sg.Text(months[8]), sg.Text(months[9]), sg.Text(months[10], background_color='#277533'),
             sg.Text(months[11])],
          [sg.Text("Day: "), sg.Text(date), sg.Text("Hour:"), sg.Text(cur_hour), sg.Text("Minute:"), sg.Text(cur_min)]]

layout11 = [[sg.Text(months[0]), sg.Text(months[1]), sg.Text(months[2]),
          sg.Text(months[3]),
           sg.Text(months[4]), sg.Text(months[5]), sg.Text(months[6]), sg.Text(months[7]),
           sg.Text(months[8]), sg.Text(months[9]), sg.Text(months[10]),
             sg.Text(months[11], background_color='#277533')],
          [sg.Text("Day: "), sg.Text(date), sg.Text("Hour:"), sg.Text(cur_hour), sg.Text("Minute:"), sg.Text(cur_min)]]


layout_holder=[layout,layout1, layout2, layout3, layout4, layout5, layout6, layout7, layout8, layout9, layout10, layout11]
#I made this so the correct layout shows
window = sg.Window('Clock', layout_holder[cur_month-1], size=(800, 100))

#I make it so that the window can stay up. If I did not have this, the window would pop up for a second and close
# imediatly
while True:
    event, values = window.read()
    if None:
        break
quit()

#I update the display
def update_display(display_value: str):
    try:
        window['-TEXT-'].update(value='{:,.f}'.format(display_value))
    except:
        window['-TEXT-'].update(value=display_value)
