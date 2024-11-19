def monthToString(monthInt):
    """
    Converts an integer representation of a month to its string name.
    
    Args:
        monthInt (int): The integer representation of the month (1-12).
    
    Returns:
        str: The string name of the month.
    """
    monthString = None
    match monthInt:
        case 1:
            monthString = "January"
        case 2:
            monthString = "February"
        case 3:
            monthString = "March"
        case 4:
            monthString = "April"
        case 5:
            monthString = "May"
        case 6:
            monthString = "June"
        case 7:
            monthString = "July"
        case 8:
            monthString = "August"
        case 9:
            monthString = "September"
        case 10:
            monthString = "October"
        case 11:
            monthString = "November"
        case 12:
            monthString = "December"
        case _:
            monthString = "If you are seeing this, blame Justin"
    return monthString
