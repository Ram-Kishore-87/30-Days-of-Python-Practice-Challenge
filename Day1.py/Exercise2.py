'''Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120'''


# Prompt the user to enter hours and rate per hour
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))

# Calculate total weekly earning
weekly_earning = hours * rate_per_hour

# Display the result
print(f"Your weekly earning is {weekly_earning}")