#Write your code below this row 👇
print("Welcome to the Even Total-er! \n")
print("This totals all even numbers from 1 to 100 \n")
total = 0

for num in range(2, 101, 2):
    #if num % 2 == 0:
        total += num
print(f"The total for all even numbers is: {total}")
