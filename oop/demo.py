# Raw string example
a_string = "this is\na string split\t\tand tabbed"
print(a_string)

# Raw string (use this for file paths)
raw_string = r"this is\na string split\t\tand tabbed"
print(raw_string)

# ASCII string (no escape characters)
b_string = "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)

# non-esacped backslash
backslash_string = "this is a backslash \followed by some text"
print(backslash_string)

# escaped backslash
backslash_string = "this is a backslash \\followed by some text"
print(backslash_string)

# escape character error example
# must end the string with an escape backslash if the string ends with a
# backslash, or this will result in error
error_string = r"this string ends with \\"