#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

import math

# Points definition
x1, y1 = 2, 2
x2, y2 = 6, 10

# Calculate slope
slope = (y2 - y1) / (x2 - x1)

# Calculate Euclidean distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Output results
print(f"Slope (m): {slope}")
print(f"Euclidean Distance: {distance:.4f}")