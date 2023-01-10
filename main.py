# Write your code below this line 👇

def calculate_bmi():
  print("Calculate your BMI")
  user_growth = float(input("Set growth: "))
  user_weight = float(input("Set weithg: "))
  user_bmi = float(user_growth/(user_weight**2))*1000
  print(f"Your BMI: {user_bmi}\n")
  return user_bmi

def show_message():
  message = '''poniżej 16 - wygłodzenie
  16 - 16.99 - wychudzenie
  17 - 18.49 - niedowagę
  18.5 - 24.99 - wagę prawidłową
  25.0 - 29.9 - nadwagę
  30.0 - 34.99 - I stopień otyłości
  35.0 - 39.99 - II stopień otyłości
  powyżej 40.0 - otyłość skrajną'''
  print(f"\n {message} \n")
  return message

def check_bmi(bmi):
  if bmi < 16:
    print("wyglodzenie")
  elif bmi >= 16.0 and bmi < 17.0:
    print("wychodzenie")
  elif bmi >= 17.0 and bmi < 18.5:
    print("niedowaga")
  elif bmi >= 18.5 and bmi < 25.0:
    print("waga prawidłowa")
  elif bmi >= 25.0 and bmi < 30.0:
    print("nadwaga")
  elif bmi >= 30.0 and bmi < 35.0:
    print("I stopien otylosci")
  elif bmi >= 35.0 and bmi < 40.0:
    print("II stopien otylosci")
  else:
    print("Skrajna otylosc. Gdy wchodzisz na wage widzisz \
    komunikat prosze wchodzic pojedynczo !!!")
  

bmi = calculate_bmi()
show_message()
check_bmi(bmi)
