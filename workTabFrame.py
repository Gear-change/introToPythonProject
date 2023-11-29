import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from commontools2 import create_label_entry, create_combo_set, create_spin_month_year, create_label_text_field, make_list_from_text

def make_list_from_text_2(text_box_in, string_detail_name):
    newList = list()
    intTempNo = 0
    for item in text_box_in.get("1.0", 'end-1c').split('\n'):
        newList.append({
            "isRelevent":True,
            string_detail_name:item,
            "titleNo": intTempNo
        })
        intTempNo += 1
    return newList

def addWorkToList(companyName, companyCity, companyState, OccupationTitlelist, 
                  occupationDetailsList, startYear, startMonth, endYear, endMonth):
    newWork = {
        "companyName":companyName,
        "companyCity":companyCity,
        "companyState":companyState,
        "OccupationTitle":OccupationTitlelist,
        "occupationDetails":occupationDetailsList,
        #is relevent should only make them sorted between them for only this one, the other ones don't print if it is not relevent.
        "isRelevent":True,
        "dateEndYear":endYear,
        "dateEndMonth":endMonth,
        "dateStartYear":startYear,
        "dateStartMonth":startMonth,
    }
    global userWork
    if newWork in userWork:
        #an alert should popup if this work already exists, asking if it should still be added, overwritten or to cancel adding
        newAlert = messagebox(None, title="duplicate skill", detail="duplicate skill detected")
        newAlert.show()
    else:
        userWork.append(newWork)

def WorkFrame(parent, listWork):
    global userWork
    userWork = listWork
    #first the variables and frames
    thisFrame = tk.Frame(parent)
    companyName = tk.StringVar()
    companyCity = tk.StringVar()
    companyState = tk.StringVar()
    occupationTitle = tk.Text()
    occupationDetailsText = tk.Text()
    oDateStartYear = tk.IntVar()
    oDateStartMonth = tk.IntVar()
    oDateEndYear = tk.IntVar()
    oDateEndMonth = tk.IntVar()

    #next the years list and other misc variables

    stateList = [ 'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 
                 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 
                 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 
                 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 
                 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 
                 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 
                 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 
                 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 
                 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
                 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
    yearsList = [year for year in range(1950, 2050)]
    curCol = 0
    curRow = 0

    #next autopopulation values
    companyName.set("Company")
    companyCity.set("City")

    # create fields for entering data here
    newEntry, newLabel = create_label_entry(thisFrame, "Name of company: ", companyName)
    newLabel.grid(column=curCol,row=curRow)
    curCol += 1
    newEntry.grid(column=curCol,row=curRow, columnspan=3)
    curCol = 0
    curRow += 1
    newEntry, newLabel = create_label_entry(thisFrame, "Company's city: ", companyCity)
    newLabel.grid(column=curCol,row=curRow)
    curCol += 1
    newEntry.grid(column=curCol,row=curRow, columnspan=3)
    curCol = 0
    curRow += 1
    newComboBox, newLabel = create_combo_set(thisFrame, "Company's state: ", companyState, stateList)
    newLabel.grid(column=curCol,row=curRow)
    curCol += 1
    newComboBox.grid(column=curCol,row=curRow, columnspan=3)
    curCol = 0
    curRow += 1
    newLabel, newComboBox, newLabel2, newComboBox1 = create_spin_month_year(thisFrame, "When where you hired(month-year): ", oDateStartMonth, oDateStartYear, yearsList)
    newLabel.grid(column=curCol,row=curRow)
    curCol += 1
    newComboBox.grid(column=curCol,row=curRow)
    curCol += 1
    newLabel2.grid(column=curCol,row=curRow)
    curCol += 1
    newComboBox1.grid(column=curCol,row=curRow)
    curCol = 0
    curRow += 1
    newLabel, newComboBox, newLabel2, newComboBox1 = create_spin_month_year(thisFrame, "When where you fired(month-year): ", oDateEndMonth, oDateEndYear, yearsList)
    newLabel.grid(column=curCol,row=curRow)
    curCol += 1
    newComboBox.grid(column=curCol,row=curRow)
    curCol += 1
    newLabel2.grid(column=curCol,row=curRow)
    curCol += 1
    newComboBox1.grid(column=curCol,row=curRow)
    curCol = 0
    curRow += 1
    newLabel, occupationTitle = create_label_text_field(thisFrame, "enter each title you had during your time here:")
    newLabel.grid(column=curCol,row=curRow)
    curCol+=1
    occupationTitle.grid(column=curCol,row=curRow, columnspan=3)
    curCol = 0
    curRow += 1
    newLabel, occupationDetailsText = create_label_text_field(thisFrame, "enter the responsabilities you had at this job: ")
    newLabel.grid(column=curCol,row=curRow)
    curCol+=1
    occupationDetailsText.grid(column=curCol,row=curRow, columnspan=3)
    curCol = 0
    curRow += 1
    btnSubmit = tk.Button(thisFrame, text="Add to Work history", 
                                command=lambda:addWorkToList(
                                    companyName.get(),
                                    companyCity.get(),
                                    companyState.get(),
                                    make_list_from_text_2(occupationTitle, "OccupationTitle"),
                                    make_list_from_text(occupationDetailsText, "OccupationDetail"),
                                    oDateStartYear.get(),
                                    oDateStartMonth.get(),
                                    oDateEndYear.get(),
                                    oDateEndMonth.get()
                                )) # Add other .get() calls
    btnSubmit.grid(column=curCol, row=curRow)
    return thisFrame