letter = 0
word = 1
sentence = 0

text = str(input("text: "))

for i in text:

    if i == " ":
        word += 1
    if i in ["!", "?", "."]:
        sentence += 1

    if i.isalpha():
        letter += 1

grade = round(0.0588 * (100 * letter / word) - 0.296 * (100 * sentence / word) - 15.8)

if grade >= 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print("Grade: ", grade)