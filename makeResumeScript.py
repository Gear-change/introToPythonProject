from fpdf import *
from tkinter.filedialog import asksaveasfile, askopenfile
import m2akeresumescript as m2
from a2345 import sort_skills

def BoolDecimal(string):
    """
    Checks if a string contains the bullet character '•'.
    
    Args:
        string (str): The string to check.
    
    Returns:
        bool: True if the string contains '•', False otherwise.
    """
    try:
        return '•' in string
    except:
        return False

def getStringHeightNeeded(width, fontSize):
    """
    Calculates the height needed for a string to fit within a given width and font size.
    
    Args:
        width (int): The width of the string.
        fontSize (int): The size of the font.
    
    Returns:
        int: The height needed for the string.
    """
    pageArea = 521
    stringLengthInt = width
    tempint = 0
    while stringLengthInt > 0:
        stringLengthInt -= pageArea
        tempint += 1
    return tempint * (fontSize + 2)

def formatPhoneNumber(userPhone):
    """
    Formats a phone number for display.
    
    Args:
        userPhone (str): The phone number to format.
    
    Returns:
        str: The formatted phone number.
    """
    userPhoneLen = len(userPhone) - 1
    listUserIndecies = [userPhoneLen - x for x in range(0, 11)]
    userPhoneFormatted = ""
    for index in range(0, len(userPhone)):
        if index < listUserIndecies[10]:
            userPhoneFormatted += userPhone[index]
        elif index == listUserIndecies[9]:
            userPhoneFormatted += "(" + userPhone[index]
        elif index == listUserIndecies[8]:
            userPhoneFormatted += userPhone[index]
        elif index == listUserIndecies[7]:
            userPhoneFormatted += userPhone[index]
        elif index == listUserIndecies[6]:
            userPhoneFormatted += ")" + userPhone[index]
        elif index == listUserIndecies[5]:
            userPhoneFormatted += userPhone[index]
        elif index == listUserIndecies[4]:
            userPhoneFormatted += userPhone[index]
        elif index == listUserIndecies[3]:
            userPhoneFormatted += "-" + userPhone[index]
        else:
            userPhoneFormatted += userPhone[index]
    return userPhoneFormatted

def makeText(*args):
    """
    Generates a text-based resume from the provided user data and saves it to a file.
    
    Args:
        *args: The user data and settings.
    """
    rFrame, userFileName, userDesc, firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects, userCatagories = args
    listToPrint = []
    
    # Format user name and contact information
    middleLetter = next((letter for letter in middleInitial if letter.isalpha()), "").capitalize()
    userFullName = " ".join((firstName, middleLetter, lastName))
    contactLine = " ".join([formatPhoneNumber(userPhone), userEmail, userLinkedin, userGithub])
    listToPrint.extend([userFullName, contactLine, "hr Break Here", "Objective:", userDesc])
    
    # Format education section
    educationStr, educationDateStr = m2.format_education(userEducation)
    if educationStr:
        listToPrint.append("Education:")
        appendFormattedSection(listToPrint, educationStr, educationDateStr)
    
    # Format projects section
    projectStr, projectDateStr = m2.format_Projects(userProjects)
    if projectStr:
        listToPrint.append("Projects:")
        appendFormattedSection(listToPrint, projectStr, projectDateStr)
    
    # Format relevant work experience section
    workStr, workDateStr = m2.format_work_experience_relevent(userWork)
    if workStr:
        listToPrint.append("Relevant Work Experience:")
        appendFormattedSection(listToPrint, workStr, workDateStr)
    
    # Format skills section
    skillYearList = sort_skills(userSkills)
    if skillYearList:
        listToPrint.append("Skills:")
        for numlist, catagory in enumerate(userCatagories):
            yearString = catagory.get("skillCatagory")
            listToPrint.append(yearString)
            newString = formatSkills(skillYearList[numlist])
            listToPrint.extend([newString, ""])
    
    # Format additional work experience section
    workStr, workDateStr = m2.format_work_experience_other(userWork)
    if workStr:
        listToPrint.append("Additional Experience:")
        appendFormattedSection(listToPrint, workStr, workDateStr)
    
    # Save to file
    string_to_save = "\n".join(listToPrint)
    with asksaveasfile(filetypes=[('Text Document', '*.txt'), ('All Files', "*.*")], defaultextension='.txt') as file:
        if file:
            file.write(string_to_save)
    rFrame.destroy()

def appendFormattedSection(listToPrint, sectionStr, dateStr):
    """
    Appends a formatted section to the print list.
    
    Args:
        listToPrint (list): The list to append to.
        sectionStr (str): The section string.
        dateStr (str): The date string.
    """
    sectionStrList = sectionStr.split("\n")
    dateStrList = dateStr.split("\n")
    tempInt1, tempInt2 = 0, 0
    while tempInt1 < len(sectionStrList) - 1:
        newTextString = sectionStrList[tempInt1] + "/t"
        tempInt1 += 1
        if len(sectionStrList) == tempInt1:
            break
        newTextString += dateStrList[tempInt2]
        listToPrint.append(newTextString)
        newTextString = ""
        tempInt2 += 1
        newTextString = sectionStrList[tempInt1] + "/t"
        tempInt1 += 1
        newTextString += dateStrList[tempInt2]
        listToPrint.append(newTextString)
        tempInt2 += 1
        curDetail = sectionStrList[tempInt1]
        while len(sectionStrList) - 1 != tempInt1 and BoolDecimal(curDetail):
            listToPrint.append(curDetail)
            tempInt1 += 1
            curDetail = sectionStrList[tempInt1]
        listToPrint.append("")
        if len(sectionStrList) - 1 <= tempInt1:
            break

def formatSkills(skillList):
    """
    Formats the skills list into a string.
    
    Args:
        skillList (list): The list of skills.
    
    Returns:
        str: The formatted skills string.
    """
    if len(skillList) == 2:
        return ", and ".join(skillList)
    elif len(skillList) == 1:
        return skillList[0]
    elif len(skillList) <= 0:
        return ""
    else:
        return "/t" + ", ".join(skillList[:-1]) + ", and " + skillList[-1]

def makeResume(*args):
    """
    Generates a PDF resume from the provided user data.
    
    Args:
        *args: The user data and settings.
    """
    rFrame, userFileName, userDesc, firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects, userCatagories = args
    
    # Sanitize the file name
    for char in ['.', '\\', '/', ':', '|', '<', '>', '*', '?', '"', '\'']:
        userFileName = userFileName.replace(char, '_')
    userFileName += ".pdf"

    # Format user name and contact information
    middleLetter = next((letter for letter in middleInitial if letter.isalpha()), "").capitalize()
    userPhoneFormatted = formatPhoneNumber(userPhone)
    userFullName = " ".join((firstName, middleLetter, lastName))
    contactLine = " ".join([userPhoneFormatted, userEmail, userLinkedin, userGithub])
    
    # Initialize PDF settings
    marginX = 45.36
    marginYTop = 45.36
    marginYBottom = 45.36
    pdf = FPDF(orientation="portrait", unit="pt", format="letter")
    pdf.add_page("P", "letter")
    pdf.add_font("Cambria", fname="C:\Windows\Fonts\\cambria.ttc")
    pdf.add_font("Cambria", "B", fname="C:\Windows\Fonts\\cambriab.ttf")
    pdf.add_font("Calibri", "B", fname="C:\Windows\Fonts\\calibrib.ttf")
    pdf.set_margins(marginX, marginYTop, marginX)

    # Add user name and contact information
    pdf.set_font("Cambria", "B", 16)
    pdf.multi_cell(0, 16, userFullName, new_x=XPos.LEFT, new_y=YPos.NEXT)
    
    pdf.set_font("Cambria", "", 11)
    pdf.multi_cell(0, 11, contactLine, new_x=XPos.LEFT, new_y=YPos.NEXT)
    
    # Add horizontal rule
    pdf.image("hrBreak.png", x=None, y=None, w=pdf.epw, h=0, type="", link="", title="Horizontal Rule", alt_text=None, is_mask=True)
    pdf.cell(0, 5, "", new_x=XPos.LEFT, new_y=YPos.NEXT)

    # Add objective section
    pdf.set_font("Calibri", "BU", 14)
    pdf.multi_cell(0, 14, "Objective:", new_x=XPos.LEFT, new_y=YPos.NEXT)
    
    pdf.set_font("Cambria", "", 11)
    pdf.multi_cell(0, 11, userDesc, new_x=XPos.LEFT, new_y=YPos.NEXT)
    
    # Add education section
    educationStr, educationDateStr = m2.format_education(userEducation)
    educationStrList = educationStr.split("\n")
    educationDateStrList = educationDateStr.split("\n")
    
    if educationStrList:
        pdf.set_font("Calibri", "BU", 14)
        pdf.multi_cell(0, 14, "Education", new_x=XPos.LEFT, new_y=YPos.NEXT)

    tempInt1, tempInt2 = 0, 0
    while tempInt1 < len(educationStrList) - 1:
        pdf.set_font("Calibri", "B", 11)
        pdf.cell(0, 11, educationStrList[tempInt1], new_x=XPos.LEFT)
        tempInt1 += 1
        if tempInt1 == len(educationStrList):
            break
        
        pdf.multi_cell(0, 11, educationDateStrList[tempInt2], new_x=XPos.LEFT, new_y=YPos.NEXT, align=Align.R)
        tempInt2 += 1
        
        pdf.set_font("Cambria", "", 11)
        pdf.cell(0, 11, educationStrList[tempInt1], new_x=XPos.LEFT)
        tempInt1 += 1
        
        pdf.multi_cell(0, 11, educationDateStrList[tempInt2], new_x=XPos.LEFT, new_y=YPos.NEXT, align=Align.R)
        tempInt2 += 1
        
        curDetail = educationStrList[tempInt1]
        while tempInt1 < len(educationStrList) - 1 and BoolDecimal(curDetail):
            pdf.multi_cell(0, 11, curDetail, new_x=XPos.LEFT, new_y=YPos.NEXT)
            tempInt1 += 1
            curDetail = educationStrList[tempInt1]
        pdf.multi_cell(0, 11, "\t", new_x=XPos.LEFT, new_y=YPos.NEXT)
        if tempInt1 >= len(educationStrList) - 1:
            break
    
    # Add projects section
    projectStr, projectDateStr = m2.format_Projects(userProjects)
    projectStrList = projectStr.split("\n")
    dateProjectStrList = projectDateStr.split("\n")
    
    if dateProjectStrList:
        pdf.set_font("Calibri", "BU", 14)
        pdf.multi_cell(0, 14, "Projects:", new_x=XPos.LEFT, new_y=YPos.NEXT)
        pdf.set_font("Calibri", "B", 11)

    tempInt1 = 0
    for project in dateProjectStrList:
        pdf.multi_cell(0, 11, projectStrList[tempInt1], new_x=XPos.LEFT, new_y=YPos.TOP)
        tempInt1 += 1
        if tempInt1 >= len(projectStrList):
            break

        pdf.multi_cell(0, 11, project, align=Align.R, new_x=XPos.LEFT, new_y=YPos.NEXT)
        
        pdf.set_font("Cambria", "", 11)
        curDetail = projectStrList[tempInt1]
        while tempInt1 < len(projectStrList) - 1 and BoolDecimal(curDetail):
            pdf.multi_cell(0, 11, curDetail, new_x=XPos.LEFT, new_y=YPos.NEXT)
            tempInt1 += 1
            if tempInt1 >= len(projectStrList):
                break
            curDetail = projectStrList[tempInt1]
        pdf.multi_cell(0, 11, "\t", new_x=XPos.LEFT, new_y=YPos.NEXT)
    # Add relevant work experience section
    workStr, workDateStr = m2.format_work_experience_relevent(userWork)
    listWorkStr = workStr.split("\n")
    listDateWorkStr = workDateStr.split("\n")
    tempInt1 = 0
    
    if listDateWorkStr:
        pdf.set_font("Calibri", "BU", 14)
        pdf.multi_cell(0, 14, "Relevant Work Experience", new_x=XPos.LEFT, new_y=YPos.NEXT)

    for workDate in listDateWorkStr:
        pdf.set_font("Cambria", "B", 11)
        pdf.cell(0, 11, listWorkStr[tempInt1], new_x=XPos.LEFT)
        tempInt1 += 1
        if tempInt1 >= len(listWorkStr):
            break
        
        pdf.cell(0, 11, workDate, new_x=XPos.LEFT, new_y=YPos.NEXT, align=Align.R)
        pdf.set_font("Cambria", "", 11)
        pdf.multi_cell(0, 11, listWorkStr[tempInt1], new_x=XPos.LEFT, new_y=YPos.NEXT)
        tempInt1 += 1
        if tempInt1 >= len(listWorkStr):
            break
        
        curDetail = listWorkStr[tempInt1]
        while BoolDecimal(curDetail):
            pdf.multi_cell(0, 11, curDetail, new_x=XPos.LEFT, new_y=YPos.NEXT)
            tempInt1 += 1
            if tempInt1 >= len(listWorkStr):
                break
            curDetail = listWorkStr[tempInt1]
        pdf.multi_cell(0, 11, "\t", new_x=XPos.LEFT, new_y=YPos.NEXT)
        if tempInt1 >= len(listWorkStr):
            break
    
    # Add skills section
    skillYearList = sort_skills(userSkills)
    if skillYearList:
        pdf.set_font("Calibri", "BU", 11)
        pdf.multi_cell(0, 11, "Skills", new_x=XPos.LEFT, new_y=YPos.NEXT)
        pdf.set_font("Cambria", "", 11)
    
    for numlist in range(len(skillYearList)):
        catagory = userCatagories[numlist]
        yearString = catagory["skillCatagory"]
        pdf.multi_cell(0, 11, yearString, new_x=XPos.RMARGIN - 350, new_y=YPos.NEXT, align=Align.L)
        
        if len(skillYearList[numlist]) == 2:
            newString = ", and ".join(skillYearList[numlist])
        elif len(skillYearList[numlist]) == 1:
            newString = skillYearList[numlist][0]
        elif len(skillYearList[numlist]) <= 0:
            continue
        else:
            newString = formatSkills(skillYearList[numlist])
        
        pdf.multi_cell(350, 11, newString, new_x=XPos.RMARGIN, new_y=YPos.LAST, align=Align.R)

        # Add linking dots
        linkingString = ""
        endX = pdf.get_x()
        pdf.set_x(pdf.l_margin)
        areaX = int(endX) - int(pdf.l_margin)
        numberFullStop = areaX * 3.4 / 8
        tempFullstopCount = 0
        while tempFullstopCount < numberFullStop:
            linkingString += "."
            tempFullstopCount += 1
        pdf.cell(0, 11, linkingString, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.multi_cell(0, 11, "\t", new_x=XPos.LEFT, new_y=YPos.NEXT)
    
    # Add additional experience section
    pdf.set_font("Calibri", "BU", 11)
    workStr, workDateStr = m2.format_work_experience_other(userWork)
    listWorkStr = workStr.split("\n")
    listDateWorkStr = workDateStr.split("\n")
    tempInt1 = 0
    
    if listWorkStr and workStr:
        pdf.multi_cell(0, 11, "Additional Experience", new_x=XPos.LEFT, new_y=YPos.NEXT)
    
    for workDate in listDateWorkStr:
        pdf.set_font("Cambria", "B", 11)
        pdf.multi_cell(0, 11, listWorkStr[tempInt1], new_x=XPos.LEFT)
        tempInt1 += 1
        if tempInt1 >= len(listWorkStr):
            break
        
        pdf.multi_cell(0, 11, workDate, new_x=XPos.LEFT, new_y=YPos.NEXT, align=Align.R)
        pdf.set_font("Cambria", "", 11)
        pdf.multi_cell(0, 11, listWorkStr[tempInt1], new_x=XPos.LEFT, new_y=YPos.NEXT)
        tempInt1 += 1
        if tempInt1 >= len(listWorkStr):
            break
        
        curDetail = listWorkStr[tempInt1]
        while tempInt1 < len(listWorkStr) - 1 and BoolDecimal(curDetail):
            pdf.multi_cell(0, 11, curDetail, new_x=XPos.LEFT, new_y=YPos.NEXT)
            tempInt1 += 1
            if tempInt1 >= len(listWorkStr):
                break
            curDetail = listWorkStr[tempInt1]
        pdf.multi_cell(0, 11, "\t", new_x=XPos.LEFT, new_y=YPos.LAST)
    
    # Save the PDF
    outputLocStr = "Output\\" + userFileName
    outputLocStr = outputLocStr.replace(" ", "")
    pdf.output(name=outputLocStr)
    rFrame.destroy()
