from monthStringScript import monthToString
def format_education(userEducation):
    education_str = "Education\n"
    for edu in userEducation:
        if edu['isRelevent']:
            education_details =  '\n  •  '.join(detail['degreeDetail'] for detail in edu['degreeDetails'] if detail['isRelevent'])
            education_str += f"{edu['degreeType']} in {edu['degreeField']} \n {edu['schoolName']}, {edu['schoolCity']}, {edu['schoolState']} \t \t GPA: {edu['gradeGPA']}\n  •  Minor: {edu['degreeMinor']}\n  •  {education_details}\n"
    return education_str

def format_work_experience_relevent(userWork):
    work_str = "Experience\n"
    for work in userWork:
        if work['isRelevent']:
            occupation_titles = '& '.join(title['OccupationTitle'] for title in work['occupationTitles'] if title['isRelevent'])
            occupation_details = '\n  •  '.join(detail['OccupationDetail'] for detail in work['occupationDetails'] if detail['isRelevent'])
            work_str += f"{occupation_titles}\t\t{monthToString(work['dateStartMonth'])}-{str(work['dateStartYear'])} to {monthToString(work['dateEndMonth'])}-{str(work['dateEndYear'])} \n{work['companyName']}, {work['companyCity']}, {work['companyState']}\n  •  {occupation_details}\n"
    return work_str
def format_work_experience_other(userWork):
    work_str = "Experience\n"
    for work in userWork:
        if not work['isRelevent']:
            occupation_titles = '& '.join(title['OccupationTitle'] for title in work['occupationTitles'] if title['isRelevent'])
            occupation_details = '\n  •  '.join(detail['OccupationDetail'] for detail in work['occupationDetails'] if detail['isRelevent'])
            work_str += f"{occupation_titles}\t\t{monthToString(work['dateStartMonth'])}-{str(work['dateStartYear'])} to {monthToString(work['dateEndMonth'])}-{str(work['dateEndYear'])} \n{work['companyName']}, {work['companyCity']}, {work['companyState']}\n  •  {occupation_details}\n"
    return work_str