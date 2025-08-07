length3 = input("When was the last time you projected your cramps onto Weasel? (Ex: 02/17/2025) ")
month3, day3, year3 = length3.split("/")
month3 = int(month3)
day3 = int(day3)
year3 = int(year3)
length3Time = 0

length2 = input("What about the one before? ")
month2, day2, year2 = length2.split("/")
month2 = int(month2)
day2 = int(day2)
year2 = int(year2)
length2Time = 0

length1 = input("And the one before that? ")
month1, day1, year1 = length1.split("/")
month1 = int(month1)
day1 = int(day1)
year1 = int(year1)
length1Time = 0

length0 = input("And finally, the one before that: ")
month0, day0, year0 = length0.split("/")
month0 = int(month0)
day0 = int(day0)
year0 = int(year0)
length0Time = 0

def monthFinder3(length3Time, year):
    is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    if month3 == 1:
        length3Time += day3
    elif month3 == 2:
        length3Time += 31
        length3Time += day3
    elif month3 == 3:
        length3Time += 60 if is_leap else 59
        length3Time += day3
    elif month3 == 4:
        length3Time += 91 if is_leap else 90
        length3Time += day3
    elif month3 == 5:
        length3Time += 121 if is_leap else 120
        length3Time += day3
    elif month3 == 6:
        length3Time += 152 if is_leap else 151
        length3Time += day3
    elif month3 == 7:
        length3Time += 182 if is_leap else 181
        length3Time += day3
    elif month3 == 8:
        length3Time += 213 if is_leap else 212
        length3Time += day3
    elif month3 == 9:
        length3Time += 244 if is_leap else 243
        length3Time += day3
    elif month3 == 10:
        length3Time += 274 if is_leap else 273
        length3Time += day3
    elif month3 == 11:
        length3Time += 305 if is_leap else 304
        length3Time += day3
    elif month3 == 12:
        length3Time += 335 if is_leap else 334
        length3Time += day3
    return length3Time

def monthFinder2(length2Time, year):
    is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    if month2 == 1:
        length2Time += day2
    elif month2 == 2:
        length2Time += 31
        length2Time += day2
    elif month2 == 3:
        length2Time += 60 if is_leap else 59
        length2Time += day2
    elif month2 == 4:
        length2Time += 91 if is_leap else 90
        length2Time += day2
    elif month2 == 5:
        length2Time += 121 if is_leap else 120
        length2Time += day2
    elif month2 == 6:
        length2Time += 152 if is_leap else 151
        length2Time += day2
    elif month2 == 7:
        length2Time += 182 if is_leap else 181
        length2Time += day2
    elif month2 == 8:
        length2Time += 213 if is_leap else 212
        length2Time += day2
    elif month2 == 9:
        length2Time += 244 if is_leap else 243
        length2Time += day2
    elif month2 == 10:
        length2Time += 274 if is_leap else 273
        length2Time += day2
    elif month2 == 11:
        length2Time += 305 if is_leap else 304
        length2Time += day2
    elif month2 == 12:
        length2Time += 335 if is_leap else 334
        length2Time += day2
    return length2Time

def monthFinder1(length1Time, year):
    is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    if month1 == 1:
        length1Time += day1
    elif month1 == 2:
        length1Time += 31
        length1Time += day1
    elif month1 == 3:
        length1Time += 60 if is_leap else 59
        length1Time += day1
    elif month1 == 4:
        length1Time += 91 if is_leap else 90
        length1Time += day1
    elif month1 == 5:
        length1Time += 121 if is_leap else 120
        length1Time += day1
    elif month1 == 6:
        length1Time += 152 if is_leap else 151
        length1Time += day1
    elif month1 == 7:
        length1Time += 182 if is_leap else 181
        length1Time += day1
    elif month1 == 8:
        length1Time += 213 if is_leap else 212
        length1Time += day1
    elif month1 == 9:
        length1Time += 244 if is_leap else 243
        length1Time += day1
    elif month1 == 10:
        length1Time += 274 if is_leap else 273
        length1Time += day1
    elif month1 == 11:
        length1Time += 305 if is_leap else 304
        length1Time += day1
    elif month1 == 12:
        length1Time += 335 if is_leap else 334
        length1Time += day1
    return length1Time

def monthFinder0(length0Time, year):
    is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    if month0 == 1:
        length0Time += day0
    elif month0 == 2:
        length0Time += 31
        length0Time += day0
    elif month0 == 3:
        length0Time += 60 if is_leap else 59
        length0Time += day0
    elif month0 == 4:
        length0Time += 91 if is_leap else 90
        length0Time += day0
    elif month0 == 5:
        length0Time += 121 if is_leap else 120
        length0Time += day0
    elif month0 == 6:
        length0Time += 152 if is_leap else 151
        length0Time += day0
    elif month0 == 7:
        length0Time += 182 if is_leap else 181
        length0Time += day0
    elif month0 == 8:
        length0Time += 213 if is_leap else 212
        length0Time += day0
    elif month0 == 9:
        length0Time += 244 if is_leap else 243
        length0Time += day0
    elif month0 == 10:
        length0Time += 274 if is_leap else 273
        length0Time += day0
    elif month0 == 11:
        length0Time += 305 if is_leap else 304
        length0Time += day0
    elif month0 == 12:
        length0Time += 335 if is_leap else 334
        length0Time += day0
    return length0Time

length3Time = monthFinder3(length3Time, year3)
length2Time = monthFinder2(length2Time, year2)
length1Time = monthFinder1(length1Time, year1)
length0Time = monthFinder0(length0Time, year0)

if year3 == year2:
    distance32 = length3Time-length2Time
elif year3 > year2:
    if year2 % 4 == 0 and (year2 % 100 != 0 or year2 % 400 == 0):
        distance32 = (length3Time + 366) - length2Time
    else:
        distance32 = (length3Time + 365) - length2Time
else:
    distance32 = length3Time - length2Time

if year2 == year1:
    distance21 = length2Time-length1Time
elif year2 > year1:
    if year1 % 4 == 0 and (year1 % 100 != 0 or year1 % 400 == 0):
        distance21 = (length2Time + 366) - length1Time
    else:
        distance21 = (length2Time + 365) - length1Time
else:
    distance21 = length2Time - length1Time

if year1 == year0:
    distance10 = length1Time-length0Time
elif year1 > year0:
    if year0 % 4 == 0 and (year0 % 100 != 0 or year0 % 400 == 0):
        distance10 = (length1Time + 366) - length0Time
    else:
        distance10 = (length1Time + 365) - length0Time
else:
    distance10 = length1Time - length0Time

total = distance32+distance21+distance10
average = total/3

print("The average is", int(average))
next = length3Time+average

nextYear = year3+1

if next > 365:
    next -= 365
    print(f"Project your next one to Weasel on 1/{int(next)}/{int(nextYear)}")
elif next > 334:
    next -= 334
    print(f"Project your next one to Weasel on 12/{int(next)}")
elif next > 304:
    next -= 304
    print(f"Project your next one to Weasel on 11/{int(next)}")
elif next > 273:
    next -= 273
    print(f"Project your next one to Weasel on 10/{int(next)}")
elif next > 243:
    next -= 243
    print(f"Project your next one to Weasel on 09/{int(next)}")
elif next > 212:
    next -= 212
    print(f"Project your next one to Weasel on 08/{int(next)}")
elif next > 181:
    next -= 181
    print(f"Project your next one to Weasel on 07/{int(next)}")
elif next > 151:
    next -= 151
    print(f"Project your next one to Weasel on 06/{int(next)}")
elif next > 120:
    next -= 120
    print(f"Project your next one to Weasel on 05/{int(next)}")
elif next > 90:
    next -= 90
    print(f"Project your next one to Weasel on 04/{int(next)}")
elif next > 59:
    next -= 59
    print(f"Project your next one to Weasel on 03/{int(next)}")
elif next > 31:
    next -= 31
    print(f"Project your next one to Weasel on 02/{int(next)}")