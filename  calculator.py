import time
print ("<----->BMI & BMR CALCULATOR<----->")
print ("    ")
print ("•••■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
Name = str(input("•••Enter your name        :- "))
age = int(input("•••Enter your age         :- "))
wrong_input = ("⛔⛔⛔WRONG INPUT⛔⛔⛔")
if age >= 120 :
    print(wrong_input)
    age = (wrong_input)
    quit()
elif age <= 1 :
    print(wrong_input)
    age = (wrong_input)
    quit()
elif age < 0 :
    print(wrong_input)
    age = (wrong_input)
    quit()
    
height = float(input("•••Enter your height(m))  :- " ))
if height >= 5 :
    print (wrong_input)
    height = (wrong_input)
    quit()
elif height <= .5 :
    print (wrong_input)
    height = (wrong_input)
    quit()
elif height <= 0 :
    print (wrong_input)
    height = (wrong_input)
    quit()
weight = float(input("•••Enter your weight(kg)  :- "))
if weight >= 2000 :
    print (wrong_input)
    weight = (wrong_input)
    quit()
elif weight <= 20 :
    print (wrong_input)
    weight = (wrong_input)
    quit()
elif weight < 0 :
    print (wrong_input)
    weight = (wrong_input)
    quit()

    
    
# bmi

bmi = weight / height ** 2



gender = ("""
°°°°°°°°°°°Select your gender :- 
                 [1] Male
                 [2] Female
                 """)
print (gender)
gender_input = int(input("•••Your gender is (1 or 2) :- "))
activity_level = ("""
°°°°°°°°°°°°Select your Activity Level :-
                  [1] Sedentary Lifestyle:
                      little or no exercise
                  [2] Slighty Active Lifestlye:
                      Exercise 1-3 times/week
                  [3] Moderately Active Lifestyle:
                      Exercise 4-5 times/week
                  [4] Active Lifestyle:
                      Daily exercise or intense exercise 
                      3-4 times/week
                  [5] Very Active Lifestyle:
                       Intense exercise 6-7 times/week
                           """)
print (activity_level)
activity_input = int(input("•••Enter your activity level:- "))
print ("•••■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print ("   ")
#equation_is_start_now
if gender_input == 1 :
    gender = ("Male")
    bmr_male = (66 + (13.7 * weight) + (5 * height) - (6.8 * age))
    bmr = bmr_male
elif gender_input == 2 :
    gender = ("Female")
    bmr_female = (655 + (9.6 * weight) + (1.8 * height) - (4.7 * age))
    bmr = bmr_female
else :
    print (wrong_input)
    quit()
print ("  ")
if activity_input == 1 :
     activity = ("Sedentary Lifestyle")
     calorie = bmr * 1.2 
elif activity_input == 2 :
     activity = ("Slighty Active Lifestlye")
     calorie = bmr * 1.375
elif activity_input == 3 :
     activity = ("Moderately Active Lifestyle")
     calorie = bmr * 1.55
elif activity_input == 4 :
     activity = ("Active Lifestyle")
     calorie = bmr * 1.725
elif activity_input == 5 :
     activity = ("Very Active Lifestyle")
     calorie = bmr * 1.9
else :
     print ("   ")
print ("Processing.......")
time.sleep(1)
print ("  ")

print ("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print ("     ")
print ("<▪︎▪︎▪︎>Review Your Information<▪︎▪︎▪︎>")
print ("    ")
print ("--------Name   : " + str(Name))
print ("--------Age    : " + str(age) + (" Year"))
print ("--------Height : " + str(height) + (" meter"))
print ("--------Weight : " + str(weight) + (" kg"))
print ("--------Gender : " + str(gender))
print ("------Activity : " + str(activity))
print ("     ")
print ("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print ("     ")
print ("           Hi " + str(Name) + str(",") + " your bmi is " + str(bmi) + " and based on your bmr result\n             you need " + str(calorie) + " calorie everyday")
print ("    ")
print ("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
time.sleep(1)
if bmi < 18.5 :
    print ("           You are underweight.Because your weight is " + str(weight) + str(" ") + " that is too low .  :(")
    print ("""
    
              Here are some healthy ways to gain weight 
              when you're underweight:
              ◑ Eat more frequently. When you're underweight,
               you may feel full faster. ...
              ◑ Choose nutrient-rich foods. ...
              ◑ Try smoothies and shakes. ...
              ◑ Watch when you drink. ...
              ◑ Make every bite count. ...
              ◑ Top it off. ...
              ◑ Have an occasional treat. ...
              ◑ Exercise.
              """)
elif bmi >= 18.5 and bmi <= 24.9 :
    print ("        CONGRATULATIONS!!" + str("You are totally fit."))
elif bmi >= 25 and bmi <= 29.9 :
    print ("OH NO!!! " + "you are overweight")
    print ("""
              Treatment for Overweight & Obesity
              ◑ Healthy eating plan and regular physical activity.
              ◑ Changing your habits.
              ◑ Weight-management programs.
              ◑ Weight-loss medicines.
              ◑ Weight-loss devices.
              ◑ Bariatric surgery.
              ◑ Special diets.
              """)
elif bmi >= 30 :
    print ("Oh no!!!🥺" + " you are obese.")
    print ("""
               Treatment for Overweight & Obesity
              ◑ Healthy eating plan and regular physical activity.
              ◑ Changing your habits.
              ◑ Weight-management programs.
              ◑ Weight-loss medicines.
              ◑ Weight-loss devices.
              ◑ Bariatric surgery.
              ◑ Special diets.
              """)
else :
    print ("   ")
print ("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")  
time.sleep(1)
print ("    ")
print ("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
print ("--------FINAL RESULT")
print ("--------BMI            = " + str(bmi))
print ("--------BMR            = " + str(bmr))
print ("--------Calorie Needed = " + str(calorie))
print ("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")