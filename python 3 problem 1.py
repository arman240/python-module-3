zander_length = float(input("Enter the length of the zander in centimeters: "))

size_limit = 42

if zander_length >= size_limit:
    print("Congratulations! The zander meets the size limit.")
else:
    difference = size_limit - zander_length
    print(f"The zander does not meet the size limit. Please release the fish back into the lake.")
    print(f"It is {difference} centimeters below the size limit.")