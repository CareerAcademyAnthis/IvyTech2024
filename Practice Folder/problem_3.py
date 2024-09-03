number = int(input("Enter a number: "))

if number > 0:
    classification = "positive"
elif number < 0:
    classification = "negative"
else:
    classification = "zero"

print(f"The number {number} is {classification}.")