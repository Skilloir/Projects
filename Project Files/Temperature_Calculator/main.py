def translate():
    option = input("Would you like to translate Fahrenheit to Celsius or Kelvin? \n")
    if option == "celsius":
        farenH = input("What is the Farenheit Measure? \n")
        FarenH_int = int(farenH)
        celciusOutput = (FarenH_int -32) * 5/9
        roundedCelcius = round(celciusOutput)
        celciusPrint = str(roundedCelcius)
        print(farenH + " Degrees Translated to Celcius is " + celciusPrint)
    elif option == "kelvin":
        kelvInput = input("What is the Farenheit Measure? \n")
        kelv_int = int(kelvInput)
        kelvOutput = (kelv_int - 32) * 5/9 + 273.15
        roundedKelv = round(kelvOutput)
        kelvPrint = str(roundedKelv)
        print(kelvInput + " Degrees translated to Kelvin is " + kelvPrint) 

translate()
