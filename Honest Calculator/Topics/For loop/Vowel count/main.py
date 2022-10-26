string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

count = 0
for i in string:
    if i in vowels:
        count += 1

print(count)
