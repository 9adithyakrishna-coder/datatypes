import math

# Input angle in degrees
angle_deg = float(input("Enter angle in degrees: "))

# Convert degrees to radians
angle_rad = math.radians(angle_deg)

# Calculate trigonometric values
sin_value = math.sin(angle_rad)
cos_value = math.cos(angle_rad)
tan_value = math.tan(angle_rad)

# Display results
print(f"Angle: {angle_deg}°")
print(f"sin({angle_deg}°) = {sin_value}")
print(f"cos({angle_deg}°) = {cos_value}")
print(f"tan({angle_deg}°) = {tan_value}")