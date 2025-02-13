print('1,Keys')
print('2,Values')
print('3,Items')
print('4,Get')
print('5,Setdefault')
print('6,Update')
print('7,Pop')
print('8,Popitem')
print()
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
    case 4:
        value_a=marks.get('ob')
        print('The ob marks is :',value_a)
    case 5:
        add=marks.setdefault('adbms',23)
        print('the add new subject with marks :',add)
        print()
        print(marks)
    case 6:
        marks.update({'ob':23})
        print('The updated marks ',marks)
    case 7:
        marks.pop('fl')
        print('remove the marks',marks)
    case 8:
        marks.popitem()
        print('Remove marks form last ',marks)
    case _:
        print('choice is not matched')
    
