"""შექმენით 5 ცვლადი რომლებშიც შეინახავთ წიგნების თავდაპირველ ფასს, შემდეგ შექმენით ცვლადი რომელშიც შეინახავთ ფასდაკლების ოდენობას, შექმენით ახალი ფასის მქონე წიგნების ცვლადები, რომელთა მნიშვნელობა იქნება ძველ მნიშვნელობას გამოკლებული ახალი, საბოლოოდ კი დაბეჭდეთ ახალი წიგნების ფასები (გამოიყენეთ კარგი მიდგომები: რომ ცვლადის მნიშვნელობის მინიჭებისას შეგიძლიათ სხვა ცვლადის გამოყენება, კოდი ახსენით კომენტარების საშვალებით, ცვლადებს დაარქვით აღმწერი სახელები snake_case-ის სტილში)"""

#წიგნების თავდაპირველი ფასები
book_1_price = 35
book_2_price = 15
book_3_price  = 25
book_4_price = 40
book_5_price = 50

#ფასდაკლება
discount = 10

#ახალი ფასები
new_book_price_1 = book_1_price - discount
new_book_price_2 = book_2_price - discount
new_book_price_3 = book_3_price - discount
new_book_price_4 = book_4_price - discount
new_book_price_5 = book_5_price - discount

#ახალი ფასების დაპრინტვა
print(new_book_price_1)
print(new_book_price_2)
print(new_book_price_3)
print(new_book_price_4)
print(new_book_price_5)
