#შექმენით while ციკლი რომელიც გამოიტანს
#40-იდან 20-მდე რიცხვებს
#სანამ პაროლი სწორი იქნება

num1 = 40
while num1 >= 20:
    print(num1)
    num1 -=1

password = input("enter your password")

while password != "1234":
    print("password is wrong")
    password = (input("try again"))

print("sworia")