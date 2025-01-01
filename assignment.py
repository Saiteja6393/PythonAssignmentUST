
email = "saiteja@gmail.com"

pos = email.find('@')
print("Position of '@':", pos)

comPos = email[email.find('.com'):]
print("Extracted '.com':", email[-4:])

gmailPos = email[pos + 1:email.find('.')]
print("Extracted 'gmail':", gmailPos)
