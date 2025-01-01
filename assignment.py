
email = "ilearniexcel@gmail.com"

pos = email.find('@')
print("Position of '@':", pos)

dot_com = email[email.find('.com'):]
print("Extracted '.com':", email[-4:])

domain_name = email[pos + 1:email.find('.')]
print("Extracted 'gmail':", domain_name)
