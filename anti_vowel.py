#! python3

def anti_vowel(text):
    vowels =['a','A','e','E','i','I','o','O','u','U']
    ans = []
    for i in text:
        if i not in vowels:
            ans.append(i)
            

    ans = ''.join(ans)
    return ans




word = input('Enter a phrase to have vowels removed: ')
print(anti_vowel(word))
                
            
