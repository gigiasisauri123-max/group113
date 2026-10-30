"""```4) დაწერეთ პითონის კოდი რომელიც მომხმარებელს input-ის საშვალებით შეეკითხება და ცვლადში შეინახავს შემდეგ ინფორმაციას:```
- Name  
- Surname  
- Age  
- Location  
- Occupation  
- Hobby  

```ამ ცვლადების საშვალებით კი გამოიტანს ერთ წინადადებას რომელშიც ყველა მიღებული ინფორმაცია იქნება გამოყენებული. 

მაგალითად:

Enter your name: Alex  
Enter your surname: Johnson  
Enter your age: 25  
Enter your location: New York  
Enter your occupation: Engineer  
Enter your hobby: Playing guitar  

Alex Johnson is 25 years old, lives in New York, works as an Engineer, and enjoys Playing guitar.
```"""

name = input("enter your name:")
surname = input("enter your surname:")
age =  input("enter your age:")
location = input("enter your location:")
occupation = input("enter your occupation:")
hobby = input("enter your hobby:")
print(name, surname, "is", age, "years old,live in", location, "he is", occupation, "and enjoys", hobby)