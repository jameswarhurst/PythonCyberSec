import requests
import hashlib

password = input("\nProvide your password to have this tested: ")

rating = 0
special_chars = ["!", "@", "#", "£"]
nums = ["0","1","2","3","4","5","6","7","8","9"]

occurance = False

#Test function
def special_test(variable, array):
    return variable in array

#Checks PW len
if (len(password)) > 9:
    rating = rating + 1

#Checks for special chars
for value in special_chars:
    if value in password and not occurance:
        rating += 1
        occurrence = True
        break

#Checks for nums
for value in nums:
    if value in password and not occurance:
        rating += 1
        occurrence = True
        break

#Checks for caps
for char in password:
    if char.isupper():
        rating += 1
        break

#Checkers for lowercase
for char in password:
    if char.islower():
        rating += 1 
        break

#Checks for sequential nums/chars aka repition
def is_sequential(string):
    for i in range(len(string) - 2):
        if (
            ord(string[i]) + 1 == ord(string[i+1])
            and ord(string[i]) + 2 == ord(string[i+2])
        ):
            return True
    return False

if is_sequential(password):
    rating -= 1

# Hash pw to SHA-1 split up pre & suffix 
hashed_pw = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
prefix = hashed_pw[:5]
suffix = hashed_pw[5:]

# Make a GET request to the "Have I Been Pwned" API
api_url = f"https://api.pwnedpasswords.com/range/{prefix}"
response = requests.get(api_url)

# Check if the password hash suffix is present in the API response
found = False
if response.status_code == 200:
    hashes = response.text.splitlines()
    for h in hashes:
        if h.startswith(suffix):
            found = True
            break

# Print the result
if found:
    print("Password HAS been found in a data breach!")
else:
    print("\nPassword HASN'T been found in a data breach.\n")

print("Your passwords rating out of 10 is:",rating*2, "\n")

# How can we test strength of password?
# Over 9 characters is good - DONE
# Does it contain special characters - DONE
# Does it contain numbers - DONE
# Does it contain capitals and non caps - DONE
# Letters aren't sequential etc - DONE
# Haveibeenpwnd API??? - DONE 

#The way we can do this is assign each key feature a scale rating, eg. 7 features, 10/7 = weighting of each feature which will then do the scale of password strenght 