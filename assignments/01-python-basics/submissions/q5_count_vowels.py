sentence = input().lower()
vowel_count = 0

for character in sentence:
    if character in "aeiou":
        vowel_count += 1

print(vowel_count)
