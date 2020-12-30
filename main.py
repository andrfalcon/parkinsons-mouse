import numpy as np
from pynput.mouse import Button, Controller

mouse = Controller()

coordinate_index = np.linspace(0, 3, 3)
coordinates = []
x_coordinates = []
y_coordinates = []

smoother_is_on = True

while smoother_is_on:
  if len(coordinates) == 3:
    for i in range(0, len(coordinates)):
      x_coordinates.append(coordinates[i][0])
      y_coordinates.append(coordinates[i][1])

    mx, bx = np.polyfit(coordinate_index, x_coordinates, 1)
    my, by = np.polyfit(coordinate_index, y_coordinates, 1)

    for i in range(0, len(coordinate_index)):
      mouse.position = (mx * coordinate_index[i] + bx, my * coordinate_index[i] + by)

    coordinates.clear()
    x_coordinates.clear()
    y_coordinates.clear()

  elif len(coordinates) < 3:
    coordinates.append(mouse.position)
    coordinates = list(dict.fromkeys(coordinates))
