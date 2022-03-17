print("Alegeti operatia:")
print("\t+ : Adunare")
print("\t- : Scadere")
print("\t* : Inmultire")
print("\t/ : Impartire")

operatia = input("Operatia aleasa este: ")

while operatia:
    if operatia == "quit":
        break
    elif operatia == '+':
        num1 = int(input("introduceti primul nr: "))
        num2 = int(input("introduceti al doilea nr: "))
        result = num1 + num2
        print("Rezultatul operatiei: " + str(num1) + " + " + str(num2) + " = " + str(result))
        operatia =input("Alegeti alta operatie: ")
    elif operatia == '-':
        num1 = int(input("introduceti primul nr: "))
        num2 = int(input("introduceti al doilea nr: "))
        result = num1 - num2
        print("Rezultatul operatiei: " + str(num1) + " - " + str(num2) + " = " + str(result))
        operatia =input("Alegeti alta operatie: ")
    elif operatia == '*':
        num1 = int(input("introduceti primul nr: "))
        num2 = int(input("introduceti al doilea nr: "))
        result = num1 * num2
        print("Rezultatul operatiei: " + str(num1) + " * " + str(num2) + " = " + str(result))
        operatia =input("Alegeti alta operatie: ")
    elif operatia == '/':
        num1 = int(input("introduceti primul nr: "))
        num2 = int(input("introduceti al doilea nr: "))
        if num2 == 0:
            print("Eroare nu se poate imparti la 0")
        else:
            result = num1 / num2
            print("Rezultatul operatiei: " + str(num1) + " / " + str(num2) + " = " + str(result))
            operatia =input("Alegeti alta operatie: ")
    else:
        print("Aceasta nu este o operatie!")
        operatia = input("Alegeti alta operatie: ")

print("--------------")
print("La revedere !!")
