import PySimpleGUI as sg
ContactsArray = []
NameArray = []

class AddContact():
    def __init__(self, Name, Number, Email):
        self.Name = Name
        self.Number = Number
        self.Email = Email 
        ContactsArray.append(self)
        NameArray.append(Name)


sg.theme('DarkAmber')  
One = AddContact("Random Random", "778-917-2994", "Barzans@outlook.com")
Two = AddContact("Random Again", "604-583-4498", "random@outlook.com")

def EditContact(Contact):
    layout = [[sg.Text('Edit contact Name:'), sg.InputText()],
            [sg.Text('Edit contact Number:'), sg.InputText()],
            [sg.Text('Edit contact Email:'), sg.InputText()],
            [sg.Button("Back"), sg.Button('Submit')] ]
    window = sg.Window(f'Edit: {Contact.Name}', layout)
    while True: 
        event, values = window.read() # type: ignore
        if event == sg.WIN_CLOSED or event == "Back":
            window.close()
            Open_SpecificContact(Contact)
            break
        elif event == "Submit":
            Contact.Name = values[0]
            Contact.Number = values[1]
            Contact.Email = values[2]
            print(Contact)
            window.close()
            open_ContactList()
            break
        window.close()
        

def Open_SpecificContact(ContactInfo):
    layout = [
        [sg.Text("Contacts")],
        [sg.Text(f'Name: {ContactInfo.Name}')],
        [sg.Text(f'Phone Number: {ContactInfo.Number}')],
        [sg.Text(f'Email: {ContactInfo.Email}')],
        [sg.Button("Back"), sg.Button("Edit Contact")]
    ]
    window = sg.Window('Contact', layout)
    while True:
        event, values = window.read() # type: ignore
        if event == sg.WIN_CLOSED or event == "Back":
            window.close()
            open_ContactList()
            break
        elif event == "Edit Contact":
            window.close()
            EditContact(ContactInfo)
            break
    window.close()

def open_ContactList():
    for i in range(0, len(NameArray)):
        print(NameArray[i])
    layout1 = [
        [sg.Text("Your Contacts:")],
        [sg.Button(text) for text in NameArray],
        [sg.Button('Exit'), sg.Button('Create Contact')],
    ]
    window1 = sg.Window('Contacts List', layout1)
    while True: 
        event, values = window1.read() #type: ignore
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "Create Contact":
            window1.close()
            open_ContactMaker()
            break
        else: 
            for i in range(0, len(ContactsArray)):
                if ContactsArray[i].Name == str(event): 
                    Contact = ContactsArray[i]
                    window1.close()
                    Open_SpecificContact(Contact)
                    break                
    window1.close()


def open_ContactMaker():
    layout = [  [sg.Text('Enter contact Name:'), sg.InputText()],
            [sg.Text('Enter contact Number:'), sg.InputText()],
            [sg.Text('Enter contact Email:'), sg.InputText()],
            [sg.Button("Back"), sg.Button('Ok')] ]
    window2 = sg.Window('Create Contact', layout)
    while True:
        event, values = window2.read() #type: ignore
        if event == sg.WIN_CLOSED or event == "Back":
            window2.close()
            open_ContactList()
            break
        elif event == "Ok":
            AddContact(values[0], values[1], values[2])
            window2.close()
            open_ContactList()
            break 
        elif event == "Back":
            window2.close()
            open_ContactList()
            break
    window2.close()

open_ContactList()