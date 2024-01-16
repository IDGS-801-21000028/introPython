print("Suma de numeros: ")
num1 = int(input("Dame n1: "))
num2 = int(input("Dame n2: "))

if num1 > num2 :
  print(f"El numero {num1} es mayor que {num2}")
else:
  print(f"El numero {num2} es mayor que {num1}")
  
print(f"{'-'*10} Pedir una edad {'-'*10}")
edad = int(input("Ingresa tu edad: "))
if edad > 18:
  print("Eres mayor de edad.")
elif edad == 17:
  print("Casi eres mayor de edad")
else:
  print("No eres mayor de edad.")
