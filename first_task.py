
hello = "Hello "
world = ' world'
one = 1
two = 2
its_true = True
user_name = input("Your name is: ")
# print(hello + world)
# print(one + two)
# print(hello + str(two))
# print(type(one))
print(len(user_name))
print(len(user_name) <= 4)

if len(user_name) <= 4:
    print(f"Its greeting for {user_name}. \n{hello} {user_name}")
else:
    print(f"Its greeting for {user_name}. \nDear mr. {user_name} {hello}!")
