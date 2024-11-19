from monthStringScript import monthToString

def format_education(userEducation):
    """
    Formats the education details for the resume.
    
    Args:
        userEducation (list): List of education details.
    
    Returns:
        tuple: Formatted education string and education date GPA string.
    """
    education_str = ""
    education_date_gpa_string = ""
    
    for edu in userEducation:
        if edu['isRelevent']:
            education_details = '\n  •  '.join(detail['degreeDetail'] for detail in edu['degreeDetails'] if detail['isRelevent'])
            education_str += f"{edu['degreeType']} in {edu['degreeField']} \n {edu['schoolName']}, {edu['schoolCity']}, {edu['schoolState']} \n  •  Minor: {edu['degreeMinor']}\n  •  {education_details}\n"
            education_date_gpa_string += f"{monthToString(edu['dateEndMonth'])} {str(edu['dateEndYear'])} \n GPA: {edu['gradeGPA']}\n"
    
    return education_str, education_date_gpa_string

def format_work_experience_relevent(userWork):
    """
    Formats the relevant work experience details for the resume.
    
    Args:
        userWork (list): List of work experience details.
    
    Returns:
        tuple: Formatted work string and work date string for relevant experiences.
    """
    work_str = ""
    work_date_str = ""
    
    for work in userWork:
        if work['isRelevent']:
            occupation_titles = ' & '.join(title['OccupationTitle'] for title in work['OccupationTitle'] if title['isRelevent'])
            occupation_details = '\n  •  '.join(detail['OccupationDetail'] for detail in work['occupationDetails'] if detail['isRelevent'])
            work_str += f"{occupation_titles} \n{work['companyName']}, {work['companyCity']}, {work['companyState']}\n  •  {occupation_details}\n"
            work_date_str += f"{monthToString(work['dateStartMonth'])} {str(work['dateStartYear'])} - {monthToString(work['dateEndMonth'])} {str(work['dateEndYear'])}\n"
    
    return work_str, work_date_str

def format_work_experience_other(userWork):
    """
    Formats the non-relevant work experience details for the resume.
    
    Args:
        userWork (list): List of work experience details.
    
    Returns:
        tuple: Formatted work string and work date string for non-relevant experiences.
    """
    work_str = ""
    work_date_str = ""
    
    for work in userWork:
        if not work['isRelevent']:
            occupation_titles = ' & '.join(title['OccupationTitle'] for title in work['OccupationTitle'] if title['isRelevent'])
            occupation_details = '\n  •  '.join(detail['OccupationDetail'] for detail in work['occupationDetails'] if detail['isRelevent'])
            work_str += f"{occupation_titles}\t\t{monthToString(work['dateStartMonth'])}-{str(work['dateStartYear'])} to {monthToString(work['dateEndMonth'])}-{str(work['dateEndYear'])} \n{work['companyName']}, {work['companyCity']}, {work['companyState']}\n  •  {occupation_details}\n"
            work_date_str += f"{monthToString(work['dateStartMonth'])} {str(work['dateStartYear'])} - {monthToString(work['dateEndMonth'])} {str(work['dateEndYear'])}\n"
    
    return work_str, work_date_str

def format_Projects(userProject):
    """
    Formats the project details for the resume.
    
    Args:
        userProject (list): List of project details.
    
    Returns:
        tuple: Formatted project string and project date string.
    """
    projects_str = ""
    project_date_str = ""
    
    for project in userProject:
        if project['isRelevent']:
            project_details = '\n  •  '.join(detail['projectDetail'] for detail in project['projectDetails'] if detail['isRelevent'])
            project_date_str += f"{monthToString(project['month'])} {str(project['year'])}\n"
            if project['hasEvent']:
                projects_str += f"{project['projectName']} for {project['eventName']} \n  •  {project_details}\n"
            else:
                projects_str += f"{project['projectName']}\n  •  {project_details}\n"
    
    return projects_str, project_date_str
