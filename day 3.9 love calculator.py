print("WELCOME TO LOVE CALCULATOR")
nme1 = input('enter your name : ')
nme2 = input('enter your partners name : ')
name1 = nme1.lower()
name2 = nme2.lower()
count1 = str(name1.count('t') + name1.count('r') + name1.count('u') + name1.count('e') +name2.count('t') +name2.count('r') +name2.count('u') + name2.count('e'))
count2 = str(name1.count('l') + name1.count('o') + name1.count('v') + name1.count('e') +name2.count('l') +name2.count('o') +name2.count('v') + name2.count('e'))
#count1_str = str(count1)
true_love = int(count1 + count2)
if true_love < 10 or true_love > 90 :
    print(f"your score is {true_love}% , you go together like coke and mentos.....")
elif true_love > 10 and true_love < 50 :
    print(f"your score is {true_love}% , you are ok together.....")
else:
    print(f"your score is {true_love}% ,you are good together.....")
