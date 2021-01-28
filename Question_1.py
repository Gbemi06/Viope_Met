number1 = 10.6411
x = "Stringline!"
number1 = int(10.6411)
z = x * 2
print(f"Integer conversion cannot do roundings:", number1)
print(f"Multiplying strings also causes trouble:", z)

# String Slicing
bigstring = "desserts"

print(f"The first 4 characters were: {bigstring[0:4]}")
print(f"The last 4 characters were: {bigstring[-4::]}")
print(f"The string backwards was: {bigstring[::-1]}")