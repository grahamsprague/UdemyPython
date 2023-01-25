username = input('Username:')

password = input('Password:')

pass_len = len(password)
pass_shade = '*' * pass_len

print(f'{username}, your password {pass_shade} is {pass_len} characters long.')