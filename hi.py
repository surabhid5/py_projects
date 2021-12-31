name = input("hey,what's your name?")
password = input("what's your password?")

print("Hey {},Your password {} is {} characters long",[name,'*'*len(password),len(password)])
