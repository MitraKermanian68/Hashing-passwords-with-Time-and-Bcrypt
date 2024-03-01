import time
import bcrypt

password = input("Enter password: ").encode('utf-8')

start = time.time()
hashed = bcrypt.hashpw(password, bcrypt.gensalt(rounds=14)) # using for making time for server to hash passwords
end = time.time()

f =end - start

print(f)