temp = input('Please enter the current temperature:\n')
tempe = int(temp)
if(tempe > 90):
    print("Wear Shorts")

elif(tempe > 70):
    print("Short sleeves are fine")

elif(tempe > 50):
    print("Wear a jacket")

elif(tempe > 32):
    print("Wear a heavy coat")

else:
    print("Stay Inside")    

