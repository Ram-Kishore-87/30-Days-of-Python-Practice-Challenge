'''Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.'''

years = int(input("Enter number of years you have lived: "))

total_seconds = years * 365 * 24 * 60 * 60

print(f"You have lived for {total_seconds} seconds.")