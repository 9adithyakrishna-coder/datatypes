# Program to check if Rohan can wear light clothes

temperature = float(input("Enter the current temperature in °C: "))

if temperature >= 20:
    print("The weather is warm. Rohan can wear light and soft clothes.")
elif temperature >= 10 and temperature < 20:
    print("It's a bit cool. Rohan should wear a light jacket.")
else:
    print("It's cold. Rohan should wear a jacket or pullover.")