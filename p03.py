"""#3
For the same validEmail(email) function above, add support for periods in the username,
i.e. "vasia.patov@gmail.com" or "john.thompson@hotmail.com", or "abc.def.ghi@yahoo.com".
There can be no more than three periods total in the username, and periods cannot be consecutive (i.e. "abc..def").
Periods don't count in the username length limit of 15."""

import string

def isEmail(email):
    array = email.split('@')                    #does the email have '@'
    if len(array) != 2:
        return False                            # if it doesn't return False

    username = array[0]
    number_of_periods = 0
    for i in range(len(username)):
        if i == 0:
            continue
        ch = username[i]
        prev = username[i-1]

        # prev = username[i-1] if i > 0 else "B"
        # variable = expression if condition else other_expression

        # if val > 5:
        #     som = "a"
        # else:
        #     som = "b"

        # som = "a" if val > 5 else "b"
        
        if ch == "." and prev == ".":
            return False
        if ch == ".":
            number_of_periods += 1
        if number_of_periods > 3:
            return False



    # for ch in username:
    #     if ch == ".":
    #         number_of_periods += 1
    #     if number_of_periods > 3:
    #         return False


    if len(username) == 0:
        return False
    allowedCharacters = set("." + string.ascii_lowercase + "_")
    for ch in username:
        if ch not in allowedCharacters:         # is each character in the username a part of the set of allowed ch?
            return False                        # if not return False
    if len(username) - number_of_periods > 15:                       # is username longer than 15 ch?
        return False                            # if so return False
    
    second_half = array[1]
    if len(second_half) == 0:
        return False
    second_half_split = second_half.split('.')  # is '.' present in second half of email
    if len(second_half_split) != 2:              # if only present once it will separate into 2 object set
        return False                            # if not 2 object set, return False
    
    sld = second_half_split[0]
    if len(sld) == 0:
        return False
    allowedCharacters2 = set(string.ascii_lowercase + string.digits)
    for ch in sld:
        if ch not in allowedCharacters2:        # is sld ch in allowedCharacters2 set?
            return False                        # if not return False
    if len(sld) > 10:                           # is sld longer than 10 ch?
        return False                            # if not return False

    tld = second_half_split[1]
    if len(tld) == 0:
        return False
    allowedCharacters3 = set(string.ascii_lowercase)
    for ch in tld:
        if ch not in allowedCharacters3:
            return False
    if len(tld) > 4:
        return False
    
    return True

print(isEmail("john..t@gmail.com"))
print(isEmail("john.t.ho.m.pson@gmail.com"))
print(isEmail("johnn.thomp.iiiii@gmail.com"))