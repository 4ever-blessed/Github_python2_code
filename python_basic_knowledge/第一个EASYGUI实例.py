import easygui
import sys

while True:
    easygui.msgbox('Welcome to my first GUI')
    msg = 'Where are you from ? '
    title = 'Univ'
    choices = ['THU','PKU','UTSC','HIT']
    choice = easygui.choicebox(msg,title,choices)

    easygui.msgbox('Your univ is ' + str(choice))
    msg = 'Do you wanna restart ? '
    title = 'RECHOICE'

    if easygui.ccbox(msg,title):
        pass
    else:
        sys.exit(0)

# This is the tutorial demo !
# easygui.egdemo()