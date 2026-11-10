a = input("Input: ").split()
b = [b.upper() for b in a]
freq = {}
for word in b:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1

print(freq)