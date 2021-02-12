def hours_and_minutes(number):
    """
        Description: Takes an integer and calculates hours and minutes in that integer.
        type(output) : str 
    
    """
    if type(number) == int:
        hours = number // 60
        minutes = number % 60
        
        if hours == 0 and minutes ==0:
            return "0 hours, 0 minutes"
        elif hours ==0 and minutes ==1:
            return str(hours) + " hours, " + str(minutes) + " minute"
        if hours == 0 and minutes > 0:
            return str(hours) + " hours, " + str(minutes) + " minutes"
        
        elif hours == 1 and minutes ==0:
            return str(hours) + " hour, " + "0 minutes" 
        elif hours == 1 and minutes ==1:
            return str(hours) + " hour, " + str(minutes) + " minute"
        elif hours == 1 and minutes > 1:
            return str(hours) + " hour, " + str(minutes) + " minutes"
        
        elif hours > 1 and minutes ==0:
            return str(hours) + " hours, " + str(minutes) + " minutes"
        elif hours > 1 and minutes ==1:
            return str(hours) + " hours, " + str(minutes) + " minute"
        elif hours > 1 and minutes > 1:
            return str(hours) + " hours, " + str(minutes) + " minutes"
    
    else:
        return "Invalid input!"
    