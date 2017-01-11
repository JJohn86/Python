# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

daysofmonths = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def leapyear(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    else:
        return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    numdays = 0
    if year2 == year1:
        if leapyear(year1) == True:
            daysofmonths[2] = 29
        if leapyear(year2) == False:
            daysofmonths[2] = 28
        return numdays + sum(daysofmonths[month1 : month2]) - day1 + day2
    numdays = 0
    
    while year1 < year2:
        if leapyear(year1) == True:
            daysofmonths[2] = 29
        if leapyear(year1) == False: 
            daysofmonths[2] = 28
        numdays = numdays + sum(daysofmonths[month1 : 13])
        month1 = 1
        year1 = year1 + 1
        if year1 == year2:
            break
    if year2 == year1:
        if leapyear(year2) == True:
            daysofmonths[2] = 29
        if leapyear(year1) == False: 
            daysofmonths[2] = 28
        return numdays + sum(daysofmonths[month1:month2]) + day2 - day1




    



# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
