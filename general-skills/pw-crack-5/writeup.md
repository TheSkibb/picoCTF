## PW Crack 5

difficulty: easy

---

sol:

iterate through the dictionary trying all of the passwords (check function modified to take in a input)

~~~py
def level_5_pw_check(user_pw):
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")
~~~

filter for the flag by 
~~~bash
py level5.py | grep pico
~~~
