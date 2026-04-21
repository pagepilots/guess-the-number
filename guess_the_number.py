import random

def guess_the_number():
    print("=== GUESS THE NUMBER ===")
    print("im thinking of a number between 1 and 100")
    
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            guess = input(f"attempt {attempts + 1}/{max_attempts} - your guess: ")
            guess = int(guess)
            
            if guess < 1 or guess > 100:
                print("dude. between 1 and 100. read the instructions.")
                continue
                
            attempts += 1
            
            if guess < secret:
                print("too low, go up")
            elif guess > secret:
                print("too high, come down")
            else:
                print(f"wow you got it in {attempts} tries. not bad.")
                return
                
        except ValueError:
            print("thats not a number. are you okay?")
    
    print(f"you lost lol. the number was {secret}. better luck next time.")

if __name__ == "__main__":
    guess_the_number()
