import mysql.connector
import datetime
import PySimpleGUI as sg


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database='Clinic'
    )

cursor = db.cursor()

#mycursor.execute("select fname from DOCTOR WHERE employeeID=123456799")

#sg.change_look_and_feel('LightBrown9')
#sg.change_look_and_feel('BrownBlue')
sg.change_look_and_feel('DarkTeal9')

patientID = 0
appointmentID = 0
def receptionist_form():
    sg.change_look_and_feel('LightBrown9')
    
    layout = [  [sg.Text('Add New Patient')],
        [sg.Text("Patient First Name"), sg.Input(key='patientFName'), sg.Text(size=(40,2))],
        [sg.Text("Patient Last Name"), sg.Input(key='patientLName'), sg.Text(size=(40,2))],
        [sg.Text("Patient ID"), sg.Input(key='patientID'), sg.Text(size=(40,2))],
        [sg.Text("Patient Date of Birth"), sg.Input(key='patientDOB'), sg.Text(size=(40,2))],
        [sg.Text("Patient Insurance ID"), sg.Input(key='insuranceID'), sg.Text(size=(40,2))],
        [sg.Text("Nurse ID"), sg.Input(key='nurseID'), sg.Text(size=(40,2))],
        [sg.Text("Doctor ID"), sg.Input(key='doctorID'), sg.Text(size=(40,2))],
        [sg.Text("Current Time"), sg.Input(key='startTime'), sg.Text(size=(40,2))],
        [sg.Text("Reason For Visit"), sg.Input(key='reason'), sg.Text(size=(40,2))],
        [sg.Button('SUBMIT')]
    ]

    # Create the Window
    window = sg.Window('New Patient Form', layout, size=(500,500))
    # Event Loop to process "events"
    while True:             
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        print("submitted")
        insert_patient = "INSERT INTO PATIENT (fname, lname, patientID, insuranceID)\
            VALUES ('%s', '%s', '%s', '%s')" %\
           (str(values['patientFName']), str(values['patientLName']), str(values['patientID']), str(values['insuranceID']))
        cursor.execute(insert_patient)
    window.close()


receptionist_form()

def doctor_form_window():
    
    # All the stuff inside your window. This is the PSG magic code compactor...
    layout = [  [sg.Text('Dr blah blah blah examining blah blah')],
        [sg.Text("Diagnosis Code"), sg.Input(key='EID'), sg.Text(size=(40,1), key='-OUTPUT-')],
        [sg.Text("End Time"), sg.Input(key='EID'), sg.Text(size=(40,1), key='-OUTPUT-')],
        [sg.Text("Doctor Notes"), sg.Input(key='EID'), sg.Text(size=(40,1), key='-OUTPUT-')]
    ]

    # Create the Window
    window = sg.Window('Doctor_Form', layout, size=(500,600))
    # Event Loop to process "events"
    while True:             
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break

    window.close()
    
def doctor_schedule():
    sg.change_look_and_feel('LightBrown5')
    layout = [
        [sg.Text("Enter Employee Portal")]
    ]

    window = sg.Window('Doctor Evaluation Form', layout, modal=True)
    print("yeys")
    window.close()
    # All the stuff inside your window. This is the PSG magic code compactor...
    layout = [  [sg.Text('Dr blah blah blah examining blah blah')],
        [sg.Text("Diagnosis Code"), sg.Input(key='EID'), sg.Text(size=(40,1), key='-OUTPUT-')],
        [sg.Text("End Time"), sg.Input(key='EID'), sg.Text(size=(40,1), key='-OUTPUT-')],
        [sg.Text("Doctor Notes"), sg.Input(key='EID'), sg.Text(size=(40,1), key='-OUTPUT-')]
    ]

    # Create the Window
    window = sg.Window('Doctor_Form', layout, size=(500,600))
    # Event Loop to process "events"
    while True:             
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break

    window.close()


employee_column = [
    [sg.Text("Login As Doctor")],
    [sg.Input(key='EID')],
    [sg.Text(size=(40,1), key='-OUTPUT-')],
    [sg.Text("Login as Nurse")],
    [sg.Input(key='NID')],
    [sg.Text(size=(40,1), key='-OUTPUT-')],
    [sg.Text("Login as Receptionist")],
    [sg.Input(key='RID')],
    [sg.Text(size=(40,1), key='-OUTPUT-')]
]

patient_column = [
    [sg.Text("Enter Patient Portal")],
    [sg.Input(key='PID')],
    [sg.Text(size=(40,1), key='-OUTPUT-')],
    [sg.Button('Ok'), sg.Button('Quit')]
]

# Define the window's contents
layout = [
    [
        sg.Column(employee_column),
        sg.VSeperator(),
        sg.Column(patient_column)
    ],
]

# Create the window
window = sg.Window('LOGIN', layout, margins=(20,100))

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    employee_query = "select fname, lname from RECEPTIONIST WHERE employeeID=" + str(values['RID']) + ";"
    cursor.execute(employee_query)
    myResult = cursor.fetchall()
    print(myResult)
    window['-OUTPUT-'].update('Welcome ' + str(myResult))
    receptionist_form()



# Finish up by removing from the screen
window.close()


















