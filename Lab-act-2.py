breakfast = int(input("Entry for breakfast: "))
lunch = int(input("Entry for lunch: "))
snack = int(input("Entry for snack: "))
dinner = int(input("Entry for dinner: "))

title = ("*************************** \n** Daily Calorie Tracker ** \n***************************")
automatic = 'Showing record for Jordi'
text = "Breakfast:\t{} \nLunch:\t{}\nSnack\t{}\nDinner:\t{}" 
calorie = breakfast + lunch + snack + dinner
calorie = str(calorie)

print(title + "\n" + automatic)
print(text.format(breakfast,lunch,snack,dinner))
print("--------------------\nYour total Calorie': " + "\t" + calorie)
print("Jordi Acero" + "\nDate Submitted: Aug 30")