# Main function to handle input, calculation, and result display
def main():
    print("Triathlon Award Calculator")

    # Try to collect input for each event time. If invalid input is given, exit the program.
    try:
        swim_time = int(input("Enter swimming time (minutes): "))
        cycling_time = int(input("Enter cycling time (minutes): "))
        running_time = int(input("Enter running time (minutes): "))
    except ValueError:
        print("Invalid input. Please enter whole numbers only.")
        return  # Stop execution if the input isn't valid

    # Compute the total time taken for the triathlon
    total_time = swim_time + cycling_time + running_time

    # Display the calculated total time
    print(f"\nTotal time taken for the triathlon: {total_time} minutes")

    # Determine which award corresponds to the total time
    if total_time <= 100:
        award = "Provincial colours"
    elif total_time <= 105:
        award = "Provincial half colours"
    elif total_time <= 110:
        award = "Provincial scroll"
    else:
        award = "No award"

    # Output the final award result
    print(f"Award: {award}")

# Ensures the main function only runs when this script is executed directly
if __name__ == "__main__":
    main()

    
