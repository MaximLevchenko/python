def main():
    days = ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday']
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
    years = []
    for i in range(1901, 2001):
        years.append(i)
    list_of_days = []
    list_of_first_of_month_days = []
    is_first_of_month = True
    for year in years:
        for month in months:
            is_first_of_month = True
            for day in range(days_in_month(month, year)):
                if is_first_of_month:
                    list_of_first_of_month_days.append(days[0])
                    is_first_of_month = False
                list_of_days.append(days[0])
                days.append(days.pop(0))
    count = 0
    for i in list_of_first_of_month_days:
        if i == 'Sunday':
            count += 1
    print(len((list_of_days)))
    print(count)


def days_in_month(month, year):
    days_of_31 = ['Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec']
    days_of_30 = ['Apr', 'Jun', 'Sept', 'Nov']
    days_of_28 = ['Feb']
    if month in days_of_31:
        return 31
    elif month in days_of_30:
        return 30
    elif month in days_of_28:
        if year % 100 == 0:
            return 28
        elif year % 400 == 0:
            return 29
        elif year % 4 == 0:
            return 29
        else:
            return 28


main()
