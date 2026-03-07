state=input("Enter your statement: ")
VOWEL="aeiou"

new=""
for letter in state:
    if letter.lower() in VOWEL:
        new +=letter
print(f"The vowels in your statement are {len(new)}")