#22) შექმენით პროგრამა რომელიც მომხმარებელს შეეკითხება პაროლს სანამ ის არ შემოიყვანს goabest123-ს

password ="goabest123"
user=input("enter your password:")

while user != password:
    user = input("try again:")
    print("correct")