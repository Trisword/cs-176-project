def titlefinder(line):
    listtitles = []
    ##titlefind = open('bestsellers.txt', 'r')
    ##line = titlefind.readlines()
    titlename = input("Enter a book title: ")
    
    for x in line:
        z = x.split('\t')
        if titlename.casefold() in z[0].casefold():
            y = x.rstrip('\n')
            y = y.split('\t')
            listtitles.append(y)
    
    ##titlefind.close()
    if all (x in listtitles == ''):
        print("Your search returned an empty list")
    else:
        print(listtitles)
if __name__ == '__main__':
    main()
