
"""
#1
Write a function that takes a string, and replaces every occurence of "foo" with the string that contains 
the length of the original string.

Examples:
fn("abcfoobar") would return "abc9bar" (the length of the original string is 9).
fn("abcbar") would return "abcbar" (no "foo" to replace)

"""

def change_foo(x):
    return x.replace("foo", str(len(x)))

print(change_foo("abcfoobar"))
print(change_foo("abcbar"))