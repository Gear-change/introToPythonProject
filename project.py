import tkinter as tk
from tkinter import ttk

def degreeToString(degree):
    try:
        return f"{degree['degreeType']} in {degree['degreeField']}: {degree['degreeSubField']}"
    except KeyError as e:
        print(f"Key error: {e} in degree")
        return " "

def addNewDegree(DegreeType, DegreeField, degreeSubField, schoolAddress1, schoolCity, schoolAddress2, schoolState, SchoolDateEndMonth, SchoolDateEndYear, SchoolDateStartMonth, SchoolDateStartYear, GPA):
    newEducation = {
        "degreeType": DegreeType,
        "degreeField": DegreeField,
        "degreeSubField": degreeSubField,
        "schoolAddress1": schoolAddress1,
        "schoolAddress2": schoolAddress2,
        "gradeGPA": GPA,
        "schoolCity": schoolCity,
        "schoolState": schoolState,
        "dateStartYear": SchoolDateStartYear,
        "dateStartMonth": SchoolDateStartMonth,
        "dateEndYear": SchoolDateEndYear,
        "dateEndMonth": SchoolDateEndMonth
    }
    userEducation.append(newEducation)

def createLabelEntry(parent, labelText, row, column):
    ttk.Label(parent, text=labelText).grid(row=row, column=column)
    entry = Entry(parent)
    entry.grid(row=row, column=column+1)
    return entry

def mainApp():
    root = tk.Tk()
    root.title("Resume Generator")
    tabControl = ttk.Notebook(root)

    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    # ... Create other tabs ...

    tabControl.add(tab1, text='Personal Information')
    tabControl.add(tab2, text='Education')
    # ... Add other tabs ...

    tabControl.pack(expand=1, fill="both")

    # Personal Information Tab
    currRow = 0
    firstName = createLabelEntry(tab1, "First Name:", currRow, 0)
    currRow += 1
    middleInitial = createLabelEntry(tab1, "Middle Initial:", currRow, 0)
    currRow += 1
    lastName = createLabelEntry(tab1, "Last Name:", currRow, 0)
    # ... Add other personal information entries ...

    # Education Tab
    DegreeType = tk.StringVar()
    DegreeField = tk.StringVar()
    degreeSubField = tk.StringVar()
    # ... Declare other StringVar or IntVar variables ...

    yearsList = [year for year in range(1950, 2050)]

    # ... Populate Education Tab with labels, entries, comboboxes ...

    # Add Degree Button
    btnSchoolSubmit = tk.Button(tab2, text="Add Degree", command=lambda: addNewDegree(DegreeType.get(), DegreeField.get(), degreeSubField.get(), ...)) # Add other .get() calls
    btnSchoolSubmit.grid(column=..., row=...)

    # ... Other GUI elements ...

    root.mainloop()

# Global Variables
userEducation = []
genericEducation = {
    # ... education dictionary structure ...
}
# ... Other generic structures ...

mainApp()
