#შექმენით პროგრამა while ციკლით რომელიც მომხარებელს შეეკითხება pin კოდს (4 ციფრიანი კოდი) იქამდე სანამ არ შემოიყვანს სწორად, საბოლოოდ დაუბეჭდეთ რომ გაიარა ავტორიზაცია და გამოუტანეთ თუ რამდენი ცდა დასჭირდა
pin ="1234"

attempts = 0

user_pin = input("enter your pin code:")

while user_pin != pin:
    attempts = attempts + 1
    user_pin = input("wrong try again:")



print("authorizathion succesful")
print("attemps:" , attempts)
