inventory ={'laptop': 100, 'desktop': 100, 'printer': 10, 'monitor': 0}
alreadyBorrowed = []
equipment = input('What equipment was taken from inventory? ')
person = input('Who borrowed the equipment? ')
def menu():
   print("Press 1: To add inventory. ")
   print("Press 2: To check inventory. ")
   print("Press q: To quit the program. ")
   return input("What would you like to do? ")
run = menu()
while True:
 if run == '1':
    addInventory = input('Equipment to be added to stock? ')
    amount = int(input('Quantity of equipment to be added to stock? '))
    inventory[addInventory]  = amount
    run = menu()
 elif run == '2':
    for key, value in inventory.items():
       print("{}: {}" .format(key, value))
    run = menu()

 elif run == '3': 
      if equipment in inventory: 
          if person in alreadyBorrowed:
           print('{} Please return the other equipment you checked out first'.format(person))
           run = menu()
          else:
              if inventory[equipment] > 0:
               inventory[equipment] -= 1
               alreadyBorrowed.append(person)
               print("{} borrowed {}".format(person, equipment))
               run = menu()
      else: 
       print('{} did not receive any because we are out of {}'.format(person, equipment)) 
       run = menu()
 elif run == 'q':
    break
 print("The program has ended")     
     

