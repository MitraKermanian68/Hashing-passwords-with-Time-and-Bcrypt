import bcrypt


password = input("Enter password: ").encode('utf-8')#b'SecretPassword7946'
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)
# username = request.form.get('username') #Or email address
# password = request.form.get('password').encode('utf-8')

#Look user up in DB using username

if bcrypt.checkpw(password,hashed):
    print("It matches")
    # return redirect(url_for('user_profile'))
else:
    print("Didn't match")
    # flash('Invalid credentials', 'warning')
    # return redirect(url_for('login'))



