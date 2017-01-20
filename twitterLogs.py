import time
def parse_time(timeInput):

    # get rid of bracket
    timeInput = timeInput.lstrip('[')
    
    # # sepparate date and time
    # dateAndTime = time.split(':', 1)
    # date, time = dateAndTime[0], dateAndTime[1]
    
    # date = date[::-1]

    # # get rid of seconds
    # time = time[:-3]
    time_object = time.strptime(timeInput, "%d/%b/%Y:%H:%M")
    return time.strftime('%Y-%m-%dT%H:%M',time_object)


    print time_object



if __name__ == "__main__":
    test = "[27/Sep/2016:05:22:00"[:-3]
    print parse_time(test)



# endpoints= defaultdict(lambda: (defaultdict(lambda: [0,0]) ) ) 