phoneBook = {}
phoneBook["john"]=11111
phoneBook["jill"]=22222
phoneBook["max"]=33333
phoneBook["alex"]=44444
phoneBook["philip"]=55555
for name, number in phoneBook.items():
    print("phone number of %s is %d" %(name, number))
#del phoneBook[Max]
#phoneBook.pop("jill")
def do_studd_with_number(n):
    print(list1[n])
list1 =[1,2,3,7,2,4]
for i in range(10):
    try:
        do_studd_with_number(i,list1)
    except IndexError:
            do_studd_with_number(0,list1)