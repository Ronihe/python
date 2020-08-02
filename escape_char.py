a = "I'm"
print(len(a))
for i in range(len(a)):
    print(i, a[i])
for i in a:
    print(i == "\'", i)

single = 'I am single quotes'
double = "I am double quotes"
print(single)
print(double)

# Escape Characters
# We need to escape characters with a backslash for special symbols to make characters that can’t be put into a string without escaping.
# \' — single-quote
# \" — double quote
# \t — tab
# \n — newline
# \\ — backslash

#Raw string: denote r before string literal. It ignores all escape characters and print the backslash that appears in the string
raw = r'Jane\'s cat'
for char in raw:
    print("char-", char)
print("raw--", raw)

# multi string with triple quotes
letter = '''Dear Jane,
How are you doing?
Sincerely,
Bob'''
print(letter[909:1188])

# replace a string
money = "$113,678,333,"
money = money.replace(",", "", 2)
print(money)

accented_string = strs = [
    "hell°", "hello", "tromsø", "boy", "stävänger", "ölut", "world"
]
import re
regex = r"(\w|\s)*"
#print(matches)
for i in accented_string:
    matches = re.finditer(regex, i, re.DOTALL)
    print(i.encode('utf-8'))
    for idx, m in enumerate(matches):
        print("idx-", idx)
        print("m--", m.group())

#join
join_str = "".join("")

ascii = r""
for i in range(128):
    cha = chr(i)
    if i <= 80:
        #cha = "\\" + chr(i)
        cha = str(cha.encode('utf-8'))

    print(cha)
    ascii += cha

print("start", ascii, len(ascii), chr(0))