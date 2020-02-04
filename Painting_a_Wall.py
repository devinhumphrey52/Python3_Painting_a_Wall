import math

# Dictionary of paint colors and cost per gallon
paintColors = {
   'red': 35,
   'blue': 25,
   'green': 23
}
#User Inputs values, a calculation for area occurs, and prints the output
wallHeight = float(input('Enter wall height (feet): \n'))
wallWidth = float(input('Enter wall width (feet): \n'))
wallArea = float(wallWidth * wallHeight)
print('Wall area:',wallArea, 'square feet')

#Calculates paint needed to paint the wall and prints the output
paint_In_gallons = (wallArea / 350)
print('Paint needed:',paint_In_gallons, 'gallons')

#Calculates paint cans needed and prints the output
gallon_cans = math.ceil(wallArea / 350)
print('Cans needed:', gallon_cans, 'can(s)')
print('')

#Allows the user to choose a color to paint with and calculates the associated cost
wall_color = (input('Choose a color to paint the wall: \n'))
paint_cost = gallon_cans * paintColors[wall_color]
print('Cost of purchasing', wall_color, 'paint:', end = '')
print(' %s%d' % ('$',paint_cost))
