from datetime import datetime,timedelta

def display_current_datetime():
    #Get the current date and time
    current_date = datetime.now()
    #Format the current date and time in "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time:{formatted_date}")

def calculate_future_date():
    #Prompt the user to enter the number of days
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        #Get the current date
        current_date = datetime.now()
        #Calculate the future date by adding the specified number of days
        future_date = current_date + timedelta(days=days_to_add) 
        #Format the future date in "YYYY-MM-DD"
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date:{formatted_future_date}")
    except ValueError:
        print("Please enter a valid integer for the number of days.")
def main():
    #Display the current date and time
    display_current_datetime()
    #Calculate the future date based on user input
    calculate_future_date()

if __name__ == "__main__":
    main()


