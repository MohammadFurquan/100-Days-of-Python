print("Day 13: 12/09/2023")

# STRING METHODS
a = "Furquan"
print(len(a))
print(a.upper()) # creates new copy string is immutable
print(a.lower())

b = "      Furquan    "
print(b.lstrip())
print(b.rstrip())

c = "!!!!Furquan!!!!!!!!!!!!!!!"
print(c.strip("!"))

d = "Furquan Faizi"
print(d.replace("Furquan","Faizi"))

e = "This is my new string"
print(e.split())

f = "introduction to python"
print(f.capitalize())

g = "introduction to python"
print(len(g))
print(len(g.center(50)))

h = "furquan faizi faizi furquan faizi"
print(h.count("furquan"))

i = "Welcome to the Console !!!"
print(i.endswith("to",4,10))

j = "He's name is john. He is an honest man."
print(j.find("is"))

k = "WelcomeToTheConsole"
print(k.index("To"))

l = "Welcome to Python's World"
print(l.isalnum())

m = "Welcome to Python's World"
print(l.isalpha())

n = "Welcome to Python's World"
print(l.isalnum())

o = "Welcome to Python's World"
print(l.islower())

p = "We wish you a Happy Birthday\n"
print(p.isprintable()) #\n is non printable so it will return False

q = "Welcome to Python's World"
print(q.isspace())

r = "World Health Organization"
print(r.istitle())

s = "Python is a Interpreted Language"
print(s.startswith("Python"))

t = "Python is a Interpreted Language"
print(t.startswith("Python"))


