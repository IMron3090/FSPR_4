import re

title = 'middle Javascript React'

js = {
    'javascript': [
        'javascript',
        'angular',
        'angularjs',
        'react',
        'node js',
        'node.js',
        'nodejs',
    ],
}
mapper_string = "|".join([reg_ex for reg_ex in js['javascript']])
result = re.finditer(mapper_string, title, re.IGNORECASE)
print(next(result))
print(next(result))


regex = r'react|javascript|angular'

test_str = r'middle javascript react'
matches = list(re.findall(regex, test_str, re.MULTILINE))
print(matches)
for match in matches:
    print('match, match.group()')

print(len(matches))

