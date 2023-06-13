# Program with inputs and calcuations
# June 13, 2023
# CTI-110 P1HW2 - Travel Expense
# Walter Jara

print('This program calculates and displays travel expenses\n')
budg=int(input('Enter Budget: '))
dest=str(input('Enter your travel destination: '))
gas=int(input('How much do you think you will spend on gas? '))
accom=int(input('Approximately, how much will you need for accomodation/hotel? '))
food=int(input('Last, how much do you need for food? '))
exp=gas+accom+food
remain=budg-exp
print()
print('------------Travel Expenses------------')
print('Location:',dest)
print('Initial Budget:',budg,'\n')
print('Fuel:', gas)
print('Accomodation:',accom)
print('Food:',food,'\n')
print('Remaining Balance:',remain)
              

