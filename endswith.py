#check if the string with a punctutation sign(.):
#the endwith() method returns true if the string ends with the specified value,othereish False

a="hellow =, welcome to my world."
print(a.endswith("."))


a="hellow, welcome to my world"
print(a.endswith("my world"))

txt = "Hello, welcome to my world."

x = txt.endswith("my world.", 5, 11)
print(x)


a="hellow my world"
print(a.endswith("world",10,15))


txt = "Hello, welcome to my world."

x = txt.endswith("to", 14, 17)
print(x)