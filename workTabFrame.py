import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Tcl
from commontools2 import create_label_entry, create_combo_set, create_spin_month_year, create_label_text_field, make_list_from_text

def make_list_from_text_2(text_box_in, string_detail_name):
    """
    Creates a list of dictionaries from the text content of a text box with title numbers.
    
    Args:
        text_box_in (tk.Text): The text box widget.
        string_detail_name (str): The name of the detail to be included in the dictionary.
    
    Returns:
        list: A list of dictionaries with the text details.
    """
    newList = []
    intTempNo = 0
    for item in text_box_in.get("1.0", 'end-1c').split('\n'):
        newList.append({
            "isRelevent": True,
            string_detail_name: item,
            "titleNo": intTempNo
        })
        intTempNo += 1
    return newList

def addWorkToList(userWork2, companyName, companyCity, companyState, OccupationTitlelist, 
                  occupationDetailsList, startYear, startMonth, endYear, endMonth):
    """
    Adds a new work experience to the user work list.
    
    Args:
        userWork2 (list): The list of user's work experiences.
        companyName (str): Name of the company.
        companyCity (str): City where the company is located.
        companyState (str): State where the company is located.
        OccupationTitlelist (list): List of occupation titles.
        occupationDetailsList (list): List of occupation details.
        startYear (int): Year the job started.
        startMonth (int): Month the job started.
        endYear (int): Year the job ended.
        endMonth (int): Month the job ended.
    """
    newWork = {
        "companyName": companyName,
        "companyCity": companyCity,
        "companyState": companyState,
        "OccupationTitle": OccupationTitlelist,
        "occupationDetails": occupationDetailsList,
        "isRelevent": True,
        "dateEndYear": endYear,
        "dateEndMonth": endMonth,
        "dateStartYear": startYear,
        "dateStartMonth": startMonth,
    }
    global userWork
    userWork = userWork2
    userWork.append(newWork)

def WorkFrame(parent, listWork):
    """
    Creates the work tab frame and populates it with input fields.
    
    Args:
        parent (tk.Widget): The parent widget for the tab frame.
        listWork (list): The list of user's work experiences.
    
    Returns:
        tk.Frame: The created frame for the work tab.
    """
    global userWork
    userWork = listWork

    # Initialize the frame and variables
    thisFrame = tk.Frame(parent, name="worFrame")
    companyName = tk.StringVar(parent, name="companyName")
    companyCity = tk.StringVar(parent, name="companyCity")
    companyState = tk.StringVar(parent, name="companyState")
    occupationTitle = tk.Text(parent, name="occupationTitle")
    occupationDetailsText = tk.Text(parent, name="occupationDetailsText")
    oDateStartYear = tk.IntVar(parent, name="oDateStartYear")
    oDateStartMonth = tk.IntVar(parent, name="oDateStartMonth")
    oDateEndYear = tk.IntVar(parent, name="oDateEndYear")
    oDateEndMonth = tk.IntVar(parent, name="oDateEndMonth")

    # Lists for dropdown menus
    stateList = [
        'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
        'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
        'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
        'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
        'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
        'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
        'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia',
        'Wisconsin', 'Wyoming'
    ]
    yearsList = list(range(1950, 2050))

    # Set default values
    companyName.set("Company")
    companyCity.set("City")

    # Create fields for entering data
    curCol, curRow = 0, 0

    newEntry, newLabel = create_label_entry(thisFrame, "Name of company: ", companyName)
    newLabel.grid(column=curCol, row=curRow)
    curCol += 1
    newEntry.grid(column=curCol, row=curRow, columnspan=3)
    curCol, curRow = 0, curRow + 1

    newEntry, newLabel = create_label_entry(thisFrame, "Company's city: ", companyCity)
    newLabel.grid(column=curCol, row=curRow)
    curCol += 1
    newEntry.grid(column=curCol, row=curRow, columnspan=3)
    curCol, curRow = 0, curRow + 1

    newComboBox, newLabel = create_combo_set(thisFrame, "Company's state: ", companyState, stateList)
    newLabel.grid(column=curCol, row=curRow)
    curCol += 1
    newComboBox.grid(column=curCol, row=curRow, columnspan=3)
    curCol, curRow = 0, curRow + 1

    newLabel, newComboBox, newLabel2, newComboBox1 = create_spin_month_year(thisFrame, "When were you hired (month-year): ", oDateStartMonth, oDateStartYear, yearsList)
    newLabel.grid(column=curCol, row=curRow)
    curCol += 1
    newComboBox.grid(column=curCol, row=curRow)
    curCol += 1
    newLabel2.grid(column=curCol, row=curRow)
    curCol += 1
    newComboBox1.grid(column=curCol, row=curRow)
    curCol, curRow = 0, curRow + 1

    newLabel, newComboBox, newLabel2, newComboBox1 = create_spin_month_year(thisFrame, "When were you fired (month-year): ", oDateEndMonth, oDateEndYear, yearsList)
    newLabel.grid(column=curCol, row=curRow)
    curCol += 1
    newComboBox.grid(column=curCol, row=curRow)
    curCol += 1
    newLabel2.grid(column=curCol, row=curRow)
    curCol += 1
    newComboBox1.grid(column=curCol, row=curRow)
    curCol, curRow = 0, curRow + 1

    newLabel, occupationTitle = create_label_text_field(thisFrame, "Enter each title you had during your time here:", "occupationTitle")
    newLabel.grid(column=curCol, row=curRow)
    curCol += 1
    occupationTitle.grid(column=curCol, row=curRow, columnspan=3)
    curCol, curRow = 0, curRow + 1

    newLabel, occupationDetailsText = create_label_text_field(thisFrame, "Enter the responsibilities you had at this job: ", "occupationDetailsText")
    newLabel.grid(column=curCol, row=curRow)
    curCol += 1
    occupationDetailsText.grid(column=curCol, row=curRow, columnspan=3)
    curCol, curRow = 0, curRow + 1

    btnSubmit = tk.Button(
        thisFrame, 
        text="Add to Work History", 
        command=lambda: addWorkToList(
            userWork,
            companyName.get(),
            companyCity.get(),
            companyState.get(),
            make_list_from_text_2(occupationTitle, "OccupationTitle"),
            make_list_from_text(occupationDetailsText, "OccupationDetail"),
            oDateStartYear.get(),
            oDateStartMonth.get(),
            oDateEndYear.get(),
            oDateEndMonth.get()
        ),
        name="btnSubmit"
    )
    btnSubmit.grid(column=curCol, row=curRow)

    return thisFrame
