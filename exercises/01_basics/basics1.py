name = input("What's your name? ") # Input with text allows to ask for an input
birthYear = int(input("What year were you born? ")) #Input however is only text so have to convert to int

age = 2026 - birthYear

print(f"Hi {name} based on my calculations you're {age} years old correct?")