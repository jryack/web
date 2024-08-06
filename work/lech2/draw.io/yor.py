cel = float(input('Enter temperature in Celsius:'))


#kuypp = float(input('Enter your weight in meters:'))

farenheit = (cel * 9/5) + 32
kelvin  = cel +273.15
print(" Temperature in Farenheit is",format(farenheit, '.2f'), "fahrenheit")
print(" Temperature in Kelvin is",format(kelvin, '.2f'), "Kelvin")