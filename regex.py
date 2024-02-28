#1
import re

txt = input()
x = re.search("ab*", txt)
if x:
    print("Yes")
else:
    print("No")

#2
import re
def match_pattern(string):
    pattern = r'ab{2,3}'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False
test_string = input()
print(f"{test_string}: {match_pattern(test_string)}")

#3
import re

txt = input()
x = re.search("[a-z]+_[a-z]+|[a-z]+_|_[a-z]+", txt)
print(x)

#4
import re

txt = input()
x = re.search("[A-Z]{1}[a-z]+", txt)
print(x)

#5
import re

txt = input()
x = re.search("a.*b$", txt)
if x:
    print("Yes")
else:
    print("No")

#6
import re

txt = input()
x = re.sub("[ ,.]", ":", txt)
print(x)

#7
import re
txt = input()
def snake_to_camel(s):
        return ''.join(x.capitalize() or '_' for x in s.split('_'))
print(snake_to_camel(txt))

#8
import re
def split_at_uppercase(string):
    split_string = re.findall('[A-Z][^A-Z]*', string)
    return split_string
test_string = input()
result = split_at_uppercase(test_string)
print("Original string:", test_string)
print("Split string at uppercase letters:", result)

#9
import re
def insert_spaces(string):
    modified_string = re.sub(r'(?<!^)(?=[A-Z])', ' ', string)
    return modified_string
test_string = input()
result = insert_spaces(test_string)
print("Original string:", test_string)
print("Modified string with spaces:", result)

#10
import re
def camel_to_snake(camel):
    snakecase = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel).lower()
    return snakecase
camelstr = input()
snakestr = camel_to_snake(camelstr)
print(snakestr)