"""Write a function that validates an e-mail address. An e-mail address is valid if it follows the pattern: "[username]@[sld].[tld]"
(sld stands for second-level domain, like "gmail" or "facebook" or "genius" or w.e., tld stands for top-level domain like "com", "net", "org", and so forth)
username is a sequence consisting of letters, numbers, and/or underscores, no longer than 15 characters.
sld is a sequence consisting of letters, and/or numbers, no longer than 10 characters.
tld is a sequence consisting of letters no longer than 4 characters.

Examples:
validEmail("john@gmail.com") # True
validEmail("!!@@#@foo") # False
validEmail("longlonglonglonglongstring@gmail.com") #False
"""
import string

def isEmail(email):
    array = email.split('@')                    #does the email have '@'
    if len(array) != 2:
        return False                            # if it doesn't return False
    
    username = array[0]
    allowedCharacters = set(string.ascii_lowercase + "_")
    for ch in username:
        if ch not in allowedCharacters:         # is each character in the username a part of the set of allowed ch?
            return False                        # if not return False
    if len(username) > 15:                       # is username longer than 15 ch?
        return False                            # if so return False
    
    second_half = array[1]
    second_half_split = second_half.split('.')  # is '.' present in second half of email
    if len(second_half_split) != 2:              # if only present once it will separate into 2 object set
        return False                            # if not 2 object set, return False
    
    sld = second_half_split[0]
    print(sld)
    allowedCharacters2 = set(string.ascii_lowercase + string.digits)
    for ch in sld:
        if ch not in allowedCharacters2:        # is sld ch in allowedCharacters2 set?
            return False                        # if not return False
    if len(sld) > 10:                           # is sld longer than 10 ch?
        return False                            # if not return False

    tld = second_half_split[1]
    allowedCharacters3 = set(string.ascii_lowercase)
    for ch in tld:
        if ch not in allowedCharacters3:
            return False
    if len(tld) > 4:
        return False
    
    return True
print(isEmail("jdlt.realty@gmail.com"))
print(isEmail("johnt@fuckyouvasia.com"))