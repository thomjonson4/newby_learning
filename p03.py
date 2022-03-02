"""#3
For the same validEmail(email) function above, add support for periods in the username,
i.e. "vasia.patov@gmail.com" or "john.thompson@hotmail.com", or "abc.def.ghi@yahoo.com".
There can be no more than three periods total in the username, and periods cannot be consecutive (i.e. "abc..def").
Periods don't count in the username length limit of 15."""

from pydoc import doc
import string

# returns whether each character of the inputString is within the inputSet
def fitsInSet(inputString, inputSet):
    for ch in inputString:
        if ch not in inputSet:
            return False
    return True


# returns whether or not the length of the inputString fits within the bounds
def withinLengthLimit(inputString, lowerBound, upperBound):
    if len(inputString) > upperBound or len(inputString) < lowerBound:
        return False
    return True

    # l = len(inputString)
    # return l <= upperBound and l >= lowerBound








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
        
        if ch == "." and prev == ".":
            return False
        if ch == ".":
            number_of_periods += 1
        if number_of_periods > 3:
            return False

    if len(username) == 0:
        return False
    if len(username) - number_of_periods > 15:                       # is username longer than 15 ch?
        return False   
                  
    if not fitsInSet(username, set("." + string.ascii_lowercase + "_")):
        return False
    
    second_half = array[1]
    if len(second_half) == 0:
        return False
    second_half_split = second_half.split('.')  # is '.' present in second half of email
    if len(second_half_split) != 2:              # if only present once it will separate into 2 object set
        return False                            # if not 2 object set, return False
    
    sld = second_half_split[0]
    if not withinLengthLimit(sld,1,10):
        return False
    if not fitsInSet(sld, set(string.ascii_lowercase + string.digits)):
        return False

    tld = second_half_split[1]
    if not withinLengthLimit(tld,1,4):
        return False
    if not fitsInSet(tld, set(string.ascii_lowercase)):
        return False

    return True

print(isEmail("john..t@gmail.com"))
print(isEmail("john.t.ho.m.pson@gmail.com"))
print(isEmail("johnn.thomp.iiiii@gmail.com"))