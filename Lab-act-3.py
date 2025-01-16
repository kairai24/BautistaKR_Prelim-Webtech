wavelength = int(input("Enter the wavelength in nanometers: "))

if (wavelength >= 380) and (wavelength <= 449):
    color = "Violet"
elif (wavelength >= 450) and (wavelength <= 484):
    color = "Blue"
elif (wavelength >= 485) and (wavelength <= 499):
    color = "Cyan"
elif (wavelength >= 500) and (wavelength <= 564):
    color = "Green"
elif (wavelength >= 565) and (wavelength <= 589):
    color = "Yellow"
elif (wavelength >= 590) and (wavelength <= 624):
    color = "Orange"
elif (wavelength >= 625) and (wavelength <= 750):
    color = "Red"
else:
    color = "not found"

text = "The color corresponding to {} nm is {}"

print(text.format(wavelength,color))
print("Jordi Acero" + "\nDate Submitted: Aug 30") 