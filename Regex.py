file = open("regex_test.txt")
pattern_name = re.compile('([A-Z][A-Za-z]+) ([A-Z][A-Za-z]+)')
found_names = pattern_name.findall(data)

for name in data(','):
    match = pattern_name.search(data)
    
    if match:
        print(match.group(1))
    else:
        print("Not a name")


data = file.read()

print(data)

file.close()