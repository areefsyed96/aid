#!/usr/bin/python3
#aid author- bikki kumar sha
#version 1.0
print ("WELCOME TO AID, YOUR CUSTOM WORDLIST GENERATOR !!!")
d1 = input("Enter the first name: ")
d2 = input("Enter the last name: ")
d3 = input("Enter the nick-name: ")
d4 = input("Enter date of birth[DDMMYYYY]: ")
d5 = input("Enter any significant date(wedding aneversary)[DDMMYYYY]: ")
d6 = input("Enter the company name/organization name/shop name: ")
d7 = input("Enter the partner's name: ")
d8 = input("Enter the pet name: ")
#d10 = input("Do you want to enter any additional key-words such as faviorate team/player[y/n]: ")
#print(d1,d2,d3,d4,d5,d6,d7,d8,d9)

#appnding first, second name and nick name with 0-100
print(d1+d2)
print(d2+d1)
print(d1+"_"+d2)
print(d2+"_"+d1)
print(d4)
d41=d4[0:2]
d42=d4[2:4]
d43=d4[4:6]
d44=d4[4:8]

i=0
while(i<=100):
	print(d1+d2+str(i))
	print(d3+d2+str(i))
	print(d2+d1+str(i))
	print(d1+d1+str(i))
	print(d2+d2+str(i))
	print(str(i)+d1+d2)
	i+=1
#apending first,last,nick - names with date of birth
#do use jan feb
print(d3+str(d4))
print(d1+str(d41))
print(d1+str(d42))
print(d1+str(d43))
print(d1+str(d44))
print(d1+d2+str(d4))
print(d2+d1+str(d4))
print(d1+d2+str(d41))
print(d1+d2+str(d42))
print(d1+d2+str(d43))
print(d2+d1+str(d41))
print(d2+d1+str(d42))
print(d2+d1+str(d43))
print(d2+d1+str(d44))
print(d1+"_"+d2+str(d41))
print(d2+"_"+d1+str(d41))
print(d1+"_"+d2+str(d42))
print(d2+"_"+d1+str(d42))
print(d1+"_"+d2+str(d43))
print(d2+"_"+d1+str(d43))
print(d1+"_"+d2+str(d44))
print(d2+"_"+d1+str(d44))

#appending first name, lastname special date

#do use jan feb
d51=d5[0:2]
d52=d5[2:4]
d53=d5[4:6]
d54=d5[4:8]
print(d3+str(d5))
print(d1+str(d51))
print(d1+str(d52))
print(d1+str(d53))
print(d1+str(d54))

#appending firstname,lastname,partner's name
print(d1+d7) 
print(d1+d7+"forever")
print(d1+"and"+d7)
print(d1+"&"+d7+"forever")
print(d1+d7+"alwaysandforever")
print(d1+"love"+d7)
print(d1+"loves"+d7)
print(d1+"heart"+d7)
print(d1+d7) 
print(d1+d7+"forever")
print(d1+"&"+d7)
print(d1+"&"+d7+"forever")
print(d1+d7+"alwaysandforever")
print(d1+d7+"always&forever")
print(d1+"love"+d7)
print(d1+"loves"+d7)
print(d1+"heart"+d7)
print(d7+d1) 
print(d7+d1+"forever")
print(d7+"and"+d1)
print(d7+"&"+d1+"forever")
print(d7+d1+"alwaysandforever")
print(d7+"love"+d1)
print(d7+"loves"+d1)
print(d7+"heart"+d7)
print(d3+d7) 
print(d3+d7+"forever")
print(d3+"&"+d7)
print(d3+"&"+d7+"forever")
print(d3+d7+"always and forever")
print(d3+"love"+d7)
print(d3+"loves"+d7)
print(d3+"heart"+d7)
print("i love you "+d7)
print("iloveyou"+d7)
#append first name,last name,partners name, date of birth and special date


print(d5)
print(d1+d2+d5)
print(d3+d5)
print(d7+d5)
print(d7+d51)
print(d7+d52)
print(d7+d53)
print(d7+d54)
print(d1+d51)
print(d1+d52)
print(d1+d51+d52)
print(d1+d53)
print(d1+d54)

print(d1+d51+d52)
print(d7+d51+d52)
print(d7+d54)
print(d1+d51+d7)
print(d1+d51+d52+d7)
print(d1+d7+d4)
print(d1+d7+d41)
print(d1+d7+d42)
print(d1+d7+d43)
print(d1+d7+d44)
print(d1+d7+d41+d42)
print(d1+d7+d4)
print(d1+d54)
print(d7+d51+d1)
print(d7+d51+d52+d1)
print(d7+d1+d4)
print(d7+d1+d41)
print(d7+d1+d42)
print(d7+d1+d43)
print(d7+d1+d44)
print(d7+d1+d41+d42)
print(d7+d1+d4)

#append company name and first name
print(d6)
print(d1+d6)
print(d2+d6)
print(d6+"rocks")
print("ilove"+d6)
print("i love "+d6)
#append pet name
print(d8)
print(d1+d8)
print(d2+d8)
print(d8+"rocks")
print("ilove"+d8)
print("i love "+d8)
