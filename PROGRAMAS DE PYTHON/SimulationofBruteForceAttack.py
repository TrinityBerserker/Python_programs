import itertools
import string
import time
import sys

def brute_force_attack(password, charset, time_limit=1200):
    start_time = time.time()
    attempts = 0
    max_combinations = sum(len(charset) ** length for length in range(1, len(password) + 1))

    for length in range(1, len(password) + 1):
        for guess in itertools.product(charset, repeat=length):
            if time.time() - start_time > time_limit:
                print("\nTime limit exceeded. Attack interrupted.")
                return None
            
            attempts += 1
            guess = ''.join(guess)
            progress = attempts / max_combinations * 100
            sys.stdout.write(f"\rProgress: [{int(progress)}%] {guess}")
            sys.stdout.flush()

            if guess == password:
                end_time = time.time()
                return (guess, attempts, end_time - start_time)

    return None

def main():
    password = input("Enter the password to test: ")
    charset = string.ascii_letters + string.digits + string.punctuation

    print(f"Starting brute force attack on password: {password}")
    result = brute_force_attack(password, charset)

    if result:
        guess, attempts, duration = result
        print(f"\nPassword '{password}' cracked in {attempts} attempts and {duration:.2f} seconds.")
    else:
        print("\nFailed to crack the password.")

if __name__ == "__main__":
    main()
