#grid_rgb

from PIL import Image

def mean_img_rgb(grid):
    
    width,height =  grid.size
    scale = width*height
    
    red = []
    green = []
    blue = []

    for i in range(width):
        for j in range(height):
            r,g,b = grid.getpixel((i,j))

            red.append(r)
            green.append(g)
            blue.append(b)
            
    sum_red = round(sum(red)/scale)
    sum_green = round(sum(green)/scale)
    sum_blue = round(sum(blue)/scale)
            
    mean_main = sum_red,sum_green,sum_blue

    return mean_main



piece = Image.open("./pic/test.png")
print(mean_img_rgb(piece))