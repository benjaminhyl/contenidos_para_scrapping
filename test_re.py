import re
# s = 'GeeksforGeeks: A computer science portal for geeks'

# match = re.search(r'portal', s)

# print('Start Index:', match.start())
# print('End Index:', match)

# string = "The quick brown fox jumps over the lazy dog"
# pattern = "[a-m]"
# result = re.findall(pattern, string)

# print(result)

regex = r'^The'
strings = ['The quick brown fox', 'The lazy dog', 'A quick brown fox']
for string in strings:
    if re.match(regex, string):
        print(f'Matched: {string}')
    else:
        print(f"Not matched: {string}")

#Creo que r antes del string ignora caracteres especiales y los lee como un string
regex_B = r"\s"
string_B = " my geek prize"
if re.match(regex_B, string_B):
    print(string_B)
