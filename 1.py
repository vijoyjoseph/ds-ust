x =input('Enter a word:  ')a

rev = x[::-1]

if rev == x :
    print('Palindrome')
else:
    print('Not palindrome!')

cnt1 = 0
cnt2 = 0

str1 = "Next, let’s create a Redux store to hold our application’s state.In the src directory, create a new file called store.js.Inside this file, import the configureStore function from @reduxjs/toolkit and your todoSliced educer. Then, use configureStore to create the Redux store."

str2 = str1.split() 

vowels = ['a','e','i','o','u']

for x in str1: 
    if x in vowels:
        cnt1 += 1
    else:
        cnt2 +=1

print('Vowel count = ',cnt1)
print('Non vowel = ',cnt2)
print(str2, len(str2))