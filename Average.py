average = 0
total = 0
howManyEntered = 0
howMany = 1 
print("How many test scores would you like to average?:")
howMany = input()
howMany = int(howMany)
while (howManyEntered < howMany):
    print("Enter test score:")
    testScore = input()
    testScore = int(testScore)
    total = total + testScore
    howManyEntered = howManyEntered + 1

average = total/howMany
print("The average for the test scores you entered is:")
print(average)
