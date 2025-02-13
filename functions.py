print('1,Keys')
print('2,Values')
print('3,Items')
print('4,Get')
print('5,Setdefault')
print('6,Update')
print('7,Pop')
print('8,Popitem')

print('Enter the choice you want to saw')
choice=int(input())
print()
marks={'ob':22,'fl':24,'ips':25,'ipp':22,'se':24}
print('the original dictinory',marks)
print()
match choice:

    case 1:
        key=marks.keys()
        print('The keys of marks :',key)
    case 2:
        value=marks.values()
        print('The value of marks :',value)
    case 3:
        item=marks.items()
        print('The item of marks :',item)
    #case 4:
    #case 5:
    #case 6:
    #case 7:
    #case 8:
    case _:
        print('You want to exit')
    
