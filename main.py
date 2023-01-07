# Write your code below this line 👇
print("Calculate your BMI")
user_growth = float(input("Set growth: "))
user_weight = float(input("Set weithg: "))
print(f"Your BMI: {(user_growth/(user_weight**2))*1000}\n")

message = '''poniżej 16 - wygłodzenie
16 - 16.99 - wychudzenie
17 - 18.49 - niedowagę
18.5 - 24.99 - wagę prawidłową
25.0 - 29.9 - nadwagę
30.0 - 34.99 - I stopień otyłości
35.0 - 39.99 - II stopień otyłości
powyżej 40.0 - otyłość skrajną'''
print(message)