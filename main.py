import numpy as np
from pynput.mouse import Button, Controller
from scipy.interpolate import UnivariateSpline
from pairing import pair, depair
import matplotlib.pyplot as plt

pointer_tracker_is_on = True
mouse = Controller()

pointer_coord = []
encoded_coord = []
decoded_coord = []

while pointer_tracker_is_on:
    # Append mouse positions to coordinate list
    pointer_coord.append(mouse.position)
    # Eliminate repeating values from coordinate list
    pointer_coord = list(dict.fromkeys(pointer_coord))
    # Break loop once there are 100 (fiddle with this number) unique values
    if len(pointer_coord) == 100:
        print("Raw Coordinates: {}".format(pointer_coord))
        break

print("Exited from while loop")

# Encode the coordinate values so that the spline function can be run on the data
for n in pointer_coord:
    encoded_coord.append(pair(int(round(n[0])), int(round(n[1]))))
    if len(encoded_coord) == 100:
        break
print("Encoded Coordinates: {}".format(encoded_coord))

x = np.linspace(0, len(encoded_coord), 100)
spl = UnivariateSpline(x, encoded_coord)
xs = np.linspace(min(encoded_coord), max(encoded_coord), 500)
spl.set_smoothing_factor(0.2)

# Show decoded coordinates to test accuracy
# Some data loss since it does not include values after the decimal point. Will be solved in future commits.
for n in encoded_coord:
    decoded_coord.append(depair(n))
    if len(decoded_coord) == 100:
        break
print("Decoded Coordinates: {}".format(decoded_coord))

# Move mouse cursor to the appropriate calculated values
# for n in decoded_coord:
#     mouse.position = n

# The number of data points must be larger than the spline degree k (3) in order for the univariate spline to work properly
# Remember, "the implementation of the spline requires that x be increasing."