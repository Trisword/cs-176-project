def monthyearfinder(line):
    listmonthyears = []
    ##yearmonth = open('bestsellers.txt', 'r')
    ##line = yearmonth.readlines()
    month = '-1'
    year = '-1'
    while int(month) not in range(1, 13):
        try:
            month = input("Enter a month (xx): ")
            if int(month) not in range(1, 13):
                print("Invalid input, try again.\n")
            else:
                pass
        except ValueError:
            month = '-1'
            print("Invalid input, try again.\n")
            
    month = '\t' + month + '/'
    while type(year) == str:
        try:
            year = int(input("Enter a year (xxxx): "))  
        except ValueError:
            print("Invalid input, enter numeric data")
            
    for x in line:
        if month in x and str(year) in x:
            y = x.rstrip('\n')
            y = y.split('\t')
            listmonthyears.append(y)
    ##yearmonth.close()
    if listmonthyears == []:
        print("Your search returned an empty string")
    else:
        print(listmonthyears)

if __name__ == '__main__':
    main()
