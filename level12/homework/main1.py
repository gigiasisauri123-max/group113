#3) შექმენით 5 ცვლადი, რომლებშიც შეინახავთ განსხვავებულ ლოგიკურ და შედარების ოპერაციათა შედეგებს (უნდა იყოს შედარების და ლოგიკური ოპერატორები ერთად მაგალითად temperature > 30 and not cloudy), გვერდზე კომენტარის საშვალებით მიუწერეთ ეს შედეგი (boolean მნიშვნელობა) აიღეთ მრავალფეროვანი კომბინაციები

temperature = 35
cloudy = False

result = temperature > 30 and not cloudy
result1 = temperature < 30 or cloudy
result2 = temperature == 35
result3 = temperature != 35
result4 = temperature >= 30

print(result)
print(result1)
print(result2)
print(result3)
print(result4)