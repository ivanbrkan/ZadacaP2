import re


string= input("unesite e-mail")


regex = "[a-z].[a-z][@][f][p][m][o][z].[s][u][m].[b][a]$"

match = re.findall(regex,string)

if match:
    print("e-mail je validan")
    
else:
    print("e-mail nije validan")


string2 = input("unesite eduId")

regex2 = "[a-z][@][s][u][m].[b][a]$"

match2 = re.findall(regex2,string2)

if match2:
    print("eduId je validan")
    
else:
    print("eduId nije validan")
