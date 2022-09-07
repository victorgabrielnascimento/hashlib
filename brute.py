import hashlib

eae = input ("Digite o MD5 hash: ")

for password in open("db.txt", "r").readlines():
    hashed = hashlib.md5(password.strip().encode()).hexdigest()
    if hashed == eae:
        print(f"a senha é {password}")