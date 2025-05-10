import datetime

def differ_time(start_time, end_time):
        """ Compares two datetime strings and prints the time difference.

    Parameters:
    start_time (str): The start time in the format "%Y-%m-%d %H:%M:%S"
    end_time (str): The end time in the format "%Y-%m-%d %H:%M:%S"

    Returns:
    None

    Prints:
    - "Time Left is equal ..." if end_time is after start_time
    - "Time has passed for ..." if end_time is before start_time
    - "It is time" if both times are equal

    Example:
    >>> differ_time("2025-05-10 12:00:00", "2025-05-10 14:00:00")
    Time Left is equal 2:00:00
       """
        try:
            start_time = datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S")
            end_time = datetime.datetime.strptime(y,"%Y-%m-%d %H:%M:%S")
        except:
               print("Invalid Format!!") 
        diff_time = end_time - start_time
        
        if diff_time.total_seconds() > 0 : 
              print (f"Time Left is equal {diff_time}")
        elif diff_time.total_seconds()< 0 :
              print (f"Time has passed for {abs(diff_time)}")
        elif diff_time.total_seconds() == 0 :
              print ("It is time")

x = str(input ("Enter Start time with format:%Y-%m-%d %H:%M:%S :"))
y= str (input ("Enter End time with format:%Y-%m-%d %H:%M:%S :"))
differ_time(x,y)
    
