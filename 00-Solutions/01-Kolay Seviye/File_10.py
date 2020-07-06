def day_of_Leap_Year(month, year):
    months_Days = {1:31,2:28,3:31,4:30,5:31,6:30,
                   7:31,8:31,9:30,10:31,11:30,12:31}

    if month == 2:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return 29
                return 28
            return 29
        return 28

    return months_Days[month]

m = int(input("Month: "))
y = int(input("Year: "))
print(day_of_Leap_Year(m, y))