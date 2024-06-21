import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames = ['a.png', 'b.png']
images = []
common_size = (1000, 1000)  

try:
    for filename in filenames:
        img = Image.open(filename)
        if img.size != common_size:
            img = img.resize(common_size)  
        images.append(np.array(img))  

    iio.imwrite('anuj.gif', images, duration=500, loop=0)
    print("GIF created successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
