#string methods
#strings are immutable
name="Team  India!"
print(name.upper())
print(name.lower())
print(name.rstrip("!"))
print(name.replace("a","A"))
print(name.split(" "))

intro="introduction to Python"
print(intro.capitalize())
print(intro.center(50))
print(len(intro.center(50)))
print(len(intro))
print(intro.count("o"))

str1="His name is Don He is an honest man"
print(str1.find("is"))
print(str1.endswith("is,4,10"))

str2="let see what happens"
print(str2.isalnum())
print(str2.isalpha())
print(str2.islower())
print(str2.isprintable())
 
str3="  "
print(str3.isspace())

str1="Python is Interpretend Language"
print(str1.startswith("Python"))
print(str1.swapcase())
print(str1.title())

