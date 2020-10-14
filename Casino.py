secret = 11

guess = int(input("Ugani številko: "))

if guess == secret:
    print("Yaaaay, zmagali ste!")
else:
    print(str(guess) + " je napačna številka...")
