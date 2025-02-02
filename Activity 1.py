w=input("Enter a word: ")
ch=input("Enter a character: ")
i=0
count=0
while i<len(w):
    if w[i]==ch:
        count+=1
    i+=1
print("Your character is repeated ",count,end=" time,s in your word")