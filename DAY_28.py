print("Day 28: 24/09/2023")

# F-STRING

letter = "Hey! My name is {} and i am from {}"
country = "India"
name = "Harry"

print(letter.format(name,country))
print(letter.format(country,name))


print(f"Hey! My name is {name} and I am from {country}")
print(f"Hey! My name is {{name}} and I am from {{country}}")

txt = "For only {price:.2f} dollars"
print(txt.format(price=49.099999))


price = 40.099999
txt = f"For only {price:.2f} dollars"
print(txt)


print(f"{2*30}")
print(type(f"{2*30}"))
