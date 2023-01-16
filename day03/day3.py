#prompt is "glitch art"

from skimage.io import imread
from block_distortion import animate_image, write_frames_to_gif

input_image = imread("earth.jpg") 
gif = animate_image(input_image, splits=2000, frames=100)
write_frames_to_gif("./glitched_earth.gif", gif, duration=100)