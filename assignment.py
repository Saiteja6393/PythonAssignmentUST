
email = "ilearniexcel@gmail.com"

pos = email.find('@')
print("Position of '@':", pos)

comPosition = email[-4:]
print("Extracted '.com':", comPosition)

gmailPosition = email[pos + 1:email.find('.')]
print("Extracted 'gmail':", gmailPosition)
