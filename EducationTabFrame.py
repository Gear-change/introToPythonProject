import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from commontools2 import create_combo_set, create_label_entry, create_spin_month_year, create_label_text_field, make_list_from_text

def addNewDegree(DegreeType, DegreeField, degreeMinor, schoolName, schoolCity, schoolState, 
                 SchoolDateEndMonth, SchoolDateEndYear, GPA, degreeDetails):
    """
    Adds a new degree to the user education list.
    
    Args:
        DegreeType (str): Type of the degree (e.g., Bachelor's, Master's).
        DegreeField (str): Field of study.
        degreeMinor (str): Minor field of study.
        schoolName (str): Name of the school.
        schoolCity (str): City where the school is located.
        schoolState (str): State where the school is located.
        SchoolDateEndMonth (int): Month of graduation.
        SchoolDateEndYear (int): Year of graduation.
        GPA (float): Grade Point Average.
        degreeDetails (list): List of details about the degree.
    """
    newEducation = {
        "degreeType": DegreeType,
        "degreeField": DegreeField,
        "degreeMinor": degreeMinor,
        "schoolName": schoolName,
        "degreeDetails": degreeDetails,
        "gradeGPA": GPA,
        "schoolCity": schoolCity,
        "schoolState": schoolState,
        "dateEndYear": SchoolDateEndYear,
        "dateEndMonth": SchoolDateEndMonth,
        "isRelevent": True
    }
    global userEducation
    userEducation.append(newEducation)

def degreeToString(degree):
    """
    Converts a degree dictionary to a string representation.
    
    Args:
        degree (dict): The degree information.
    
    Returns:
        str: The string representation of the degree.
    """
    try:
        return f"{degree['degreeType']} in {degree['degreeField']}: {degree['degreeMinor']}"
    except KeyError as e:
        print(f"Key error: {e} in degree {degree['degreeField']}")
        return " "

def makeEducationTabFrame(parent, listEducation):
    """
    Creates the education tab frame and populates it with input fields.
    
    Args:
        parent (tk.Widget): The parent widget for the tab frame.
        listEducation (list): The list of user's education details.
    
    Returns:
        tk.Frame: The created frame for the education tab.
    """
    global userEducation
    userEducation = listEducation
    newFrame = tk.Frame(parent, name="eduFrame")
    
    # Declare StringVar and IntVar variables
    DegreeType = tk.StringVar(parent, name="DegreeType")
    DegreeField = tk.StringVar(parent, name="DegreeField")
    degreeMinor = tk.StringVar(parent, name="degreeMinor")
    schoolName = tk.StringVar(parent, name="schoolName")
    schoolCity = tk.StringVar(parent, name="schoolCity")
    schoolState = tk.StringVar(parent, name="schoolState")
    SchoolDateEndMonth = tk.IntVar(parent, name="SchoolDateEndMonth")
    SchoolDateEndYear = tk.IntVar(parent, name="SchoolDateEndYear")
    GPA = tk.StringVar(parent, name="GPA")
    degreeDetails = tk.Text()
    
    # Lists for dropdown menus
    yearsList = list(range(1950, 2050))
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
    degreeTypeList = ['Highschool', 'Associate', 'Bachelor', 'Master', 'Doctorate']

    # Setting default values
    DegreeField.set("Field")
    DegreeType.set("select a Type")

    # Populate Education Tab with labels, entries, comboboxes
    curRow, curCol = 0, 0
    newComboBox, newLabel = create_combo_set(newFrame, "Degree type:", DegreeType, degreeTypeList)
    newLabel.grid(column=curCol, row=curRow)
    curCol += 1
    newComboBox.grid(column=curCol, row=curRow)
    curCol, curRow = 0, curRow + 1

    newEntry, newLabel = create_label_entry(newFrame, "Enter your degree's field: ", DegreeField)
    newLabel.grid(column=curCol, row=curRow)
    curCol += 1
    newEntry.grid(column=curCol, row=curRow, columnspan=3)
    curCol, curRow = 0, curRow + 1

    newEntry, newLabel = create_label_entry(newFrame, "Enter your Minor: ", degreeMinor)
    newLabel.grid(column=curCol, row=curRow)
    curCol += 1
    newEntry.grid(column=curCol, row=curRow, columnspan=3)
    curCol, curRow = 0, curRow + 1

    newEntry, newLabel = create_label_entry(newFrame, "Enter the name of the school you got it at: ", schoolName)
    newLabel.grid(column=curCol, row=curRow)
    curCol += 1
    newEntry.grid(column=curCol, row=curRow, columnspan=3)
    curCol, curRow = 0, curRow + 1

    newEntry, newLabel = create_label_entry(newFrame, "Enter that school's city: ", schoolCity)
    newLabel.grid(column=curCol, row=curRow)
    curCol += 1
    newEntry.grid(column=curCol, row=curRow, columnspan=3)
    curCol, curRow = 0, curRow + 1

    newComboBox, newLabel = create_combo_set(newFrame, "Enter that school's state: ", schoolState, stateList)
    newLabel.grid(column=curCol, row=curRow)
    curCol += 1
    newComboBox.grid(column=curCol, row=curRow, columnspan=3)
    curCol, curRow = 0, curRow + 1

    newEntry, newLabel = create_label_entry(newFrame, "Enter your overall GPA: ", GPA)
    newLabel.grid(column=curCol, row=curRow)
    curCol += 1
    newEntry.grid(column=curCol, row=curRow, columnspan=3)
    curCol, curRow = 0, curRow + 1

    newLabel1, newComboBox, newLabel2, newComboBox1 = create_spin_month_year(newFrame, "Grad date (month - year): ", SchoolDateEndMonth, SchoolDateEndYear, yearsList)
    newLabel1.grid(column=curCol, row=curRow)
    curCol += 1
    newComboBox.grid(column=curCol, row=curRow)
    curCol += 1
    newLabel2.grid(column=curCol, row=curRow)
    curCol += 1
    newComboBox1.grid(column=curCol, row=curRow)
    curCol, curRow = 0, curRow + 1

    newLabel, degreeDetails = create_label_text_field(newFrame, "Some details about your time getting this degree:", "degreeDetails")
    newLabel.grid(column=curCol, row=curRow)
    curCol += 1
    degreeDetails.grid(column=curCol, row=curRow, columnspan=3)
    curRow += 1

    # Add Degree Button
    btnSchoolSubmit = tk.Button(newFrame, text="Add Degree", command=lambda: addNewDegree(
        DegreeType.get(), DegreeField.get(), degreeMinor.get(), schoolName.get(), schoolCity.get(), 
        schoolState.get(), SchoolDateEndMonth.get(), SchoolDateEndYear.get(), GPA.get(), 
        make_list_from_text(degreeDetails, "degreeDetail")), name="btnSubmit")
    btnSchoolSubmit.grid(column=curCol, row=curRow)

    return newFrame
