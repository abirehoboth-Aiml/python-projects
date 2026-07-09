score = 0

print("=== Python Quiz Game ===")

print("\nQuestion 1")
print("What is the capital of India?")
print("a) Chennai")
print("b) Delhi")
print("c) Mumbai")

answer = input("Enter your answer (a/b/c): ").lower()

if answer == "b":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is Delhi.")

print("\nQuestion 2")
print("Which language is used for Machine Learning?")
print("a) Python")
print("b) HTML")
print("c) CSS")

answer = input("Enter your answer (a/b/c): ").lower()

if answer == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is Python.")

print("\nQuestion 3")
print("How many days are there in a week?")
print("a) 5")
print("b) 6")
print("c) 7")

answer = input("Enter your answer (a/b/c): ").lower()

if answer == "c":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is 7.")

print("\nYour Final Score:", score, "/3")
