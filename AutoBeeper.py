

"""

left: The x-coordinate of the left edge of the rectangular region, measured in pixels from the left edge of the screen.
top: The y-coordinate of the top edge of the rectangular region, measured in pixels from the top edge of the screen.
right: The x-coordinate of the right edge of the rectangular region, measured in pixels from the left edge of the screen.
bottom: The y-coordinate of the bottom edge of the rectangular region, measured in pixels from the top edge of the screen.

"""


from PIL import ImageGrab
import winsound
import time
import win32api
import win32con


# get the screen dimensions
width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

# get the screen proportions and window positions
height_inches = 7.5
width_inches = 13.29

height_y_inches = 2.44
width_y_inches = 0.87

height_x_inches = 0.41
width_x_inches = 13.29

total_height_pixels = 1080
total_width_pixels = 1920

sCale_H = total_height_pixels/height_inches
sCale_W = total_width_pixels/width_inches

H_y = sCale_H*height_y_inches
W_y = sCale_W*width_y_inches

H_x = sCale_H*height_x_inches
W_x = sCale_W*width_x_inches

Top = H_y - H_x
Bottom = H_y
Left = W_x - W_y
Right = W_x





#Set up the song
half = 1000
quarter = 500
doteighth = 375
eighth = 250
sixteenth = 125

f3 = 349
g3 = 392
a3 = 440
bflat3 = 466
c4 = 523
d4 = 587
eflat4 = 622
e4 = 659
f4 = 698
g4 = 784
a4 = 880

def song(DummyInputBecauseICantCode):
    #winsound.Beep(g3, sixteenth)
    #winsound.Beep(f3, quarter)
    #winsound.Beep(f3, eighth)
    winsound.Beep(g3, quarter)
    winsound.Beep(c4, quarter)
    winsound.Beep(e4, quarter)
    winsound.Beep(g3, quarter)
    
    


# define the region of pixels to monitor
monitor_region = (Left, Top, Right, Bottom)  # left, top, right, bottom


# Initialize the color of the region to monitor
prev_color = None

# Loop indefinitely
while True:
    # Capture a screenshot of the screen
    screen = ImageGrab.grab()

    # Crop the screenshot to the desired region
    region = screen.crop(monitor_region)

    # Get the average color of the pixels in the region
    avg_color = tuple(map(int, region.resize((1, 1)).getpixel((0, 0))))

    # Check if the color of the region has changed
    if avg_color != prev_color:
        # Play a beep sound
        song(1)
        # Update the previous color
        prev_color = avg_color

    # Wait for a short period before checking the screen again

    time.sleep(0.01)
