from PIL import Image
import numpy as np
from pprint import pprint
import random
import time

color1 = (103, 58, 183) #block
color2 = (255,255,255) #air
color3 = (0, 188, 212) #water

grid = []
grid_height_pattern = []

grid_width = int(input('Enter grid width:'))

if(input('Random heights (y,n)')=='n'):
   for grids in range(grid_width):
      grid_height_pattern.append(int(input(f"Height at grid {grids+1}:")))
else:
   height_limit = int(input('Random Height Limit:'))
   for grids in range(grid_width):
      grid_height_pattern.append(random.randint(1,height_limit))

print(f"Height pattern:{grid_height_pattern}")

start = time.time()

def grid_height_list(x,max):
    result = []
    for i in range(max):
        if (i<x):
            result.append(1)
        else:
            result.append(0)
    return result

def create_grid(height_pattern):
   global grid
   max_grid_height = max(height_pattern)

   for height in height_pattern:
      grid.append(grid_height_list(height,max_grid_height))
        
create_grid(grid_height_pattern)

for grids in grid:
   for pixel in grids:
      if (pixel==1):
         grids[grids.index(pixel)] = color1
      else:
         grids[grids.index(pixel)] = color2

array = np.array(grid, dtype=np.uint8)
grid_image = Image.fromarray(array)
grid_image = grid_image.rotate(90,expand=1)
#grid_image = grid_image.resize((grid_image.size[0]*100, grid_image.size[1]*100))
grid_image.save('Grid.bmp')
grid_image.show()

# Solving
def read_grid(height_pattern):
   global l_read
   global r_read

   l_read = []
   r_read = []
   heighest = 0

   # reading from left
   for l in height_pattern:
      if(l>heighest):
         heighest=l
      l_read.append(heighest)
      
   print(f"L:{l_read}")
   heighest = 0
   # reading from right
   for r in reversed(height_pattern):
      if(r>heighest):
         heighest=r
      r_read.insert(0, heighest)

   print(f"R:{r_read}")

read_grid(grid_height_pattern)

def find_fills(l,r,height):
   global fill_pattern
   fill_pattern = []

   # eqn = min(r,l) - height+1
   for i in range(grid_width):
      x = min(r[i],l[i])-height[i]
      fill_pattern.append(x)
      # filling
      if(x>0):
         for y in range(x):
             grid[i][(height[i]+x)-(y+1)] = color3            

find_fills(l_read,r_read,grid_height_pattern)
print('fill pattern:', fill_pattern)

array = np.array(grid, dtype=np.uint8)
grid_image = Image.fromarray(array)
grid_image = grid_image.rotate(90,expand=1)
#grid_image = grid_image.resize((grid_image.size[0]*100, grid_image.size[1]*100))
grid_image.save('Grid_Filled.bmp')
grid_image.show()

end = time.time()
elapsed = end - start

print(f"Solved in {elapsed}")
input('press any key to exit')
