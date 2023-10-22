gender = input("Enter your biological gender (male or female): ").strip().lower()
hemoglobin_value = float(input("Enter your hemoglobin value in g/l: "))
normal_ranges = {
    "male": (134, 167),
    "female": (117, 155)
}
if gender in normal_ranges:
    min_range, max_range = normal_ranges[gender]
    if min_range <= hemoglobin_value <= max_range:
        status = "normal"
    elif hemoglobin_value < min_range:
        status = "low"
    else:
        status = "high"
    print(f"Your hemoglobin level is {status}.")
else:
    print("Invalid gender. Please enter 'male' or 'female'.")
