from monthStringScript import monthToString
def format_education(userEducation):
    education_str = ""
    education_date_gpa_string = ""
    for edu in userEducation:
        if edu['isRelevent']:
            education_details =  '\n  •  '.join(detail['degreeDetail'] for detail in edu['degreeDetails'] if detail['isRelevent'])
            education_str += f"{edu['degreeType']} in {edu['degreeField']} \n {edu['schoolName']}, {edu['schoolCity']}, {edu['schoolState']} \n  •  Minor: {edu['degreeMinor']}\n  •  {education_details}\n"
            education_date_gpa_string += f"{monthToString(edu['dateEndMonth'])}-{str(edu['dateEndYear'])} \n GPA: {edu['gradeGPA']}\n"
    return education_str, education_date_gpa_string

def format_work_experience_relevent(userWork):
    work_str = ""
    work_date_str = ""
    for work in userWork:
        if work['isRelevent']:
            occupation_titles = '& '.join(title['OccupationTitle'] for title in work['occupationTitles'] if title['isRelevent'])
            occupation_details = '\n  •  '.join(detail['OccupationDetail'] for detail in work['occupationDetails'] if detail['isRelevent'])
            work_str += f"{occupation_titles} \n{work['companyName']}, {work['companyCity']}, {work['companyState']}\n  •  {occupation_details}\n"
            work_date_str += f"{monthToString(work['dateStartMonth'])}-{str(work['dateStartYear'])} to {monthToString(work['dateEndMonth'])}-{str(work['dateEndYear'])}\n"
    return work_str, work_date_str
def format_work_experience_other(userWork):
    work_str = ""
    work_date_str = ""
    for work in userWork:
        if not work['isRelevent']:
            occupation_titles = '& '.join(title['OccupationTitle'] for title in work['occupationTitles'] if title['isRelevent'])
            occupation_details = '\n  •  '.join(detail['OccupationDetail'] for detail in work['occupationDetails'] if detail['isRelevent'])
            work_str += f"{occupation_titles}\t\t{monthToString(work['dateStartMonth'])}-{str(work['dateStartYear'])} to {monthToString(work['dateEndMonth'])}-{str(work['dateEndYear'])} \n{work['companyName']}, {work['companyCity']}, {work['companyState']}\n  •  {occupation_details}\n"
            work_date_str += f"{monthToString(work['dateStartMonth'])}-{str(work['dateStartYear'])} to {monthToString(work['dateEndMonth'])}-{str(work['dateEndYear'])}\n"
    return work_str, work_date_str
