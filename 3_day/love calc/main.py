# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()
score1 = 0
score2 = 0
score_all = 0

# for i in "true":
#     score1 += lower_name1.count(i)
#     score1 += lower_name2.count(i)
#
# for j in "love":
#     score2 += lower_name1.count(j)
#     score2 += lower_name2.count(j)

for i, j in zip("true", "love"):
    score1 += lower_name1.count(i)
    score1 += lower_name2.count(i)
    score2 += lower_name1.count(j)
    score2 += lower_name2.count(j)

score_all = int(str(score1) + str(score2))

if score_all < 10 or score_all > 90:
    print(f"Your score is {score_all}, you go together like coke and mentos")
elif 50 > score_all > 40:
    print(f"Your score is {score_all}, you are alright together.")
else:
    print(f"Your score is {score_all}.")

