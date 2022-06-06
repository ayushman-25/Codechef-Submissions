st1 = input()
freq = {} 
for i in st1:
    if ord(i) >= 97 and ord(i) <= 122:
        if i in freq: 
            freq[i] += 1
        else: 
            freq[i] = 1    
r = "".join(str(key) + str(value) for key, value in freq.items())
print(r)