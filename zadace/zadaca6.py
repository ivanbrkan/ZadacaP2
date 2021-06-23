def obrnuto(string):
    if len(string) == 0:
        return string
    else:
        return obrnuto(string[1:]) + string[0]


rijec = input("Unesite string koji zelite obrnuti: ")

print(obrnuto(rijec))
