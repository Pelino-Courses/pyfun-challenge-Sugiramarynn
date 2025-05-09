import datetime

def differ_time(start_time, end_time):
        """This is a function tha"""
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
    
