# "Mumbo Jumbo" by Nem Moonglove
from math import floor, ceil, sqrt
from time import time, sleep
from random import randint
import numpy as np
import PIL.Image
import timeit
import os
import Inverter_of_Truth as inverter
from tkinter import *
import subprocess

# Stopwatch functions for documenting runtime
def start():
    global timer_start
    timer_start = timeit.default_timer()
def stop(readout=True):
    timer_stop = timeit.default_timer()
    if readout == True:
        print('Time:', str(round(timer_stop - timer_start))+'s') 


# List of all characters that will be used for the encryption
basic_characters = inverter.basic_characters

# List of colours that will be used for the encryption
# These must first be removed from an image

'''
The Great Voodo Debug

While in a list format, the <tabooIndex> would have extra [255]s by added to it,
and I could not find out the cause. In function form, the problem has disappeared,
although I would like to know what was causing the problem in the first place.
'''
def tabooIndex():
    return [
        [249, 3, 3], [238, 130, 3], [238, 234, 13], [7, 203, 27], [21, 5, 254], [115, 3, 239], [146, 4, 239], [3, 4, 4], [238, 247, 250], [127, 140, 112], [111, 59, 37],
        [246, 16, 18], [245, 126, 0], [254, 242, 18], [4, 213, 21], [6, 22, 249], [117, 6, 253], [152, 3, 244], [0, 14, 7], [241, 250, 237], [120, 125, 106], [93, 60, 34],
        [252, 10, 20], [231, 119, 5], [251, 252, 17], [1, 208, 61], [5, 9, 232], [136, 12, 250], [152, 28, 218], [5, 22, 13], [254, 246, 253], [112, 117, 134], [122, 48, 26],
        [243, 2, 15], [251, 100, 5], [228, 247, 6], [22, 203, 41], [8, 18, 244], [118, 15, 240], [185, 14, 221], [9, 9, 3], [240, 240, 248], [147, 107, 123], [94, 83, 59],
        [237, 7, 4], [245, 137, 16], [240, 253, 22], [18, 191, 37], [13, 3, 253], [123, 13, 235], [154, 26, 229], [20, 13, 16], [250, 252, 237], [135, 106, 129], [80, 77, 36],
        [243, 15, 22], [243, 145, 19], [247, 240, 16], [20, 195, 44], [4, 6, 239], [110, 7, 254], [187, 3, 219], [12, 2, 4], [237, 251, 238], [143, 140, 147], [111, 45, 33],
        [245, 15, 5], [246, 136, 12], [230, 245, 7], [11, 211, 15], [29, 3, 255], [93, 1, 234], [184, 6, 236], [9, 3, 3], [239, 241, 253], [148, 138, 142], [121, 71, 55],
        [255, 28, 7], [247, 136, 0], [234, 241, 13], [8, 192, 56], [1, 18, 245], [94, 16, 240], [174, 0, 197], [9, 0, 21], [249, 229, 250], [116, 126, 151], [118, 43, 29],
        [238, 12, 12], [242, 128, 12], [239, 242, 18], [23, 194, 43], [11, 2, 236], [105, 4, 234], [162, 0, 193], [11, 2, 14], [250, 253, 239], [149, 108, 134], [114, 55, 56],
        [232, 4, 10], [247, 126, 5], [236, 239, 14], [6, 224, 42], [5, 0, 231], [128, 11, 236], [183, 6, 240], [5, 6, 6], [237, 245, 255], [125, 126, 98], [113, 68, 45],
        [240, 24, 1], [250, 117, 5], [248, 231, 15], [12, 203, 35], [21, 6, 239], [125, 21, 246], [176, 21, 235], [12, 8, 16], [253, 236, 232], [109, 113, 118], [123, 78, 42],
        [235, 13, 13], [252, 143, 19], [242, 235, 11], [3, 228, 61], [20, 15, 252], [131, 6, 244], [155, 20, 220], [19, 15, 2], [250, 255, 242], [121, 116, 126], [82, 55, 30],
        [252, 10, 15], [254, 126, 29], [239, 234, 4], [10, 217, 34], [25, 0, 239], [114, 13, 239], [139, 15, 211], [2, 17, 22], [247, 250, 233], [138, 120, 147], [117, 61, 35],
        [255, 2, 13], [228, 127, 1], [254, 255, 13], [4, 184, 37], [5, 22, 239], [131, 15, 238], [189, 12, 224], [0, 22, 16], [250, 244, 237], [113, 129, 107], [102, 82, 60],
        [244, 13, 2], [252, 137, 9], [240, 244, 19], [24, 203, 48], [4, 24, 251], [115, 14, 249], [162, 31, 222], [16, 7, 13], [229, 254, 243], [147, 133, 120], [83, 67, 36],
        [254, 20, 16], [250, 104, 20], [245, 254, 26], [8, 221, 61], [8, 23, 238], [110, 4, 231], [170, 18, 212], [12, 20, 18], [239, 254, 247], [115, 111, 124], [105, 86, 55],
        [255, 23, 6], [249, 122, 17], [253, 249, 13], [4, 229, 40], [2, 4, 226], [129, 13, 236], [148, 5, 211], [15, 10, 2], [238, 252, 234], [116, 141, 140], [121, 90, 38],
        [239, 12, 21], [243, 127, 3], [248, 252, 0], [9, 206, 53], [5, 2, 229], [124, 18, 241], [178, 27, 227], [8, 21, 12], [227, 252, 249], [114, 138, 103], [108, 70, 43],
        [241, 0, 6], [253, 145, 11], [242, 252, 19], [5, 229, 60], [19, 20, 255], [100, 13, 253], [156, 16, 238], [7, 27, 2], [255, 242, 239], [127, 151, 112], [127, 70, 36],
        [239, 15, 2], [234, 131, 7], [248, 250, 4], [15, 189, 25], [25, 4, 250], [102, 20, 240], [166, 15, 231], [14, 1, 6], [252, 231, 242], [117, 119, 141], [126, 80, 37],
        [232, 2, 8], [254, 106, 3], [252, 246, 21], [8, 228, 44], [18, 4, 240], [123, 9, 229], [139, 13, 222], [9, 1, 2], [243, 250, 243], [120, 145, 149], [95, 79, 18],
        [249, 6, 9], [246, 120, 17], [230, 243, 6], [7, 213, 30], [6, 21, 245], [140, 1, 253], [160, 7, 230], [15, 6, 19], [251, 255, 244], [106, 135, 141], [91, 90, 35],
        [243, 2, 21], [242, 140, 2], [252, 254, 21], [10, 217, 58], [18, 17, 243], [107, 5, 255], [158, 23, 220], [9, 4, 26], [243, 233, 246], [114, 134, 130], [103, 51, 31],
        [240, 5, 0], [243, 115, 9], [248, 236, 4], [0, 191, 20], [20, 1, 253], [94, 1, 254], [152, 6, 230], [2, 24, 12], [247, 240, 244], [137, 119, 114], [120, 58, 25],
        [246, 2, 25], [241, 117, 7], [244, 231, 4], [1, 204, 33], [7, 10, 255], [120, 6, 238], [158, 25, 206], [9, 10, 4], [240, 242, 241], [136, 139, 150], [123, 76, 37],
        [244, 14, 3], [248, 144, 24], [254, 252, 17], [18, 204, 31], [18, 5, 242], [124, 14, 244], [154, 6, 194], [7, 25, 1], [255, 245, 231], [119, 145, 135], [105, 96, 45],
        [255, 16, 5], [241, 152, 0], [252, 227, 2], [16, 232, 31], [23, 16, 248], [107, 12, 228], [143, 10, 203], [18, 14, 8], [231, 243, 247], [131, 141, 147], [97, 63, 59],
        [236, 19, 9], [255, 113, 23], [251, 249, 14], [26, 206, 37], [7, 21, 244], [130, 21, 252], [185, 15, 224], [14, 12, 20], [244, 250, 249], [124, 115, 150], [99, 69, 69],
        [249, 5, 2], [240, 148, 4], [254, 229, 11], [8, 209, 44], [13, 16, 251], [108, 21, 233], [147, 15, 213], [7, 19, 8], [250, 249, 246], [127, 139, 139], [80, 57, 38],
        [245, 5, 7], [244, 139, 1], [252, 247, 15], [16, 197, 39], [10, 0, 229], [102, 15, 242], [151, 6, 204], [2, 5, 11], [238, 247, 254], [117, 127, 130], [109, 72, 56],
        [238, 17, 14], [238, 103, 5], [247, 253, 17], [10, 227, 57], [7, 5, 237], [129, 21, 248], [164, 5, 193], [19, 3, 6], [243, 251, 245], [113, 128, 136], [122, 80, 26],
        [252, 22, 4], [248, 124, 1], [244, 255, 16], [16, 213, 48], [15, 6, 230], [111, 21, 246], [156, 19, 227], [0, 6, 23], [247, 243, 242], [118, 102, 124], [90, 46, 36],
        [237, 17, 8], [235, 126, 10], [250, 248, 17], [10, 196, 17], [2, 4, 237], [106, 4, 247], [181, 20, 230], [17, 10, 7], [248, 241, 242], [120, 126, 131], [87, 80, 46],
        [250, 19, 9], [253, 148, 22], [249, 252, 11], [16, 216, 35], [13, 8, 251], [127, 11, 237], [152, 12, 239], [16, 10, 9], [246, 235, 245], [133, 118, 122], [108, 60, 53],
        [235, 4, 17], [243, 122, 1], [240, 246, 16], [2, 223, 19], [9, 2, 233], [134, 8, 255], [148, 0, 207], [0, 26, 5], [250, 253, 228], [116, 142, 128], [104, 53, 49],
        [240, 11, 8], [245, 112, 22], [231, 246, 9], [20, 226, 47], [10, 24, 250], [99, 16, 241], [170, 10, 199], [24, 8, 7], [239, 254, 231], [124, 108, 133], [107, 83, 27],
        [247, 0, 3], [244, 130, 3], [247, 243, 5], [5, 193, 16], [21, 9, 237], [106, 17, 246], [173, 17, 203], [21, 8, 8], [243, 237, 253], [142, 148, 116], [96, 77, 43],
        [241, 16, 8], [255, 117, 28], [250, 251, 1], [19, 213, 52], [15, 8, 238], [124, 27, 249], [143, 13, 214], [20, 1, 4], [230, 252, 243], [153, 117, 134], [106, 95, 39],
        [245, 4, 9], [236, 124, 18], [242, 239, 17], [14, 223, 59], [13, 4, 245], [113, 18, 252], [171, 3, 237], [14, 1, 5], [233, 248, 241], [146, 123, 149], [113, 57, 56],
        [255, 12, 10], [245, 126, 17], [253, 237, 0], [0, 187, 37], [1, 9, 239], [85, 9, 245], [162, 25, 206], [16, 4, 22], [245, 248, 251], [111, 113, 134], [96, 59, 31],
        [242, 7, 9], [237, 130, 0], [251, 233, 5], [4, 223, 33], [11, 14, 248], [102, 3, 245], [163, 5, 200], [26, 13, 7], [234, 236, 247], [109, 136, 107], [98, 50, 21],
        [253, 12, 17], [255, 147, 22], [235, 250, 17], [7, 203, 56], [0, 5, 248], [92, 2, 234], [184, 0, 235], [17, 7, 19], [254, 229, 252], [154, 134, 134], [107, 64, 59],
        [251, 13, 11], [250, 131, 14], [226, 254, 8], [15, 191, 51], [7, 14, 238], [112, 16, 232], [159, 14, 199], [0, 19, 1], [247, 246, 249], [135, 124, 122], [86, 60, 41],
        [236, 6, 21], [243, 104, 13], [244, 238, 20], [9, 191, 20], [15, 15, 242], [104, 21, 243], [138, 6, 221], [11, 8, 3], [228, 255, 255], [104, 130, 118], [84, 60, 37],
        [253, 16, 7], [248, 142, 9], [252, 246, 7], [4, 229, 45], [25, 2, 248], [91, 3, 247], [172, 7, 224], [0, 7, 19], [245, 227, 252], [125, 141, 103], [114, 90, 47],
        [245, 8, 0], [251, 102, 0], [230, 251, 8], [17, 201, 23], [16, 16, 246], [114, 3, 228], [145, 21, 217], [1, 26, 1], [255, 251, 240], [125, 139, 130], [123, 88, 37],
        [246, 8, 27], [232, 107, 0], [251, 246, 4], [25, 224, 36], [19, 15, 243], [132, 1, 235], [153, 8, 230], [10, 20, 19], [243, 250, 255], [118, 102, 139], [109, 63, 13],
        [228, 8, 4], [241, 123, 18], [240, 240, 15], [26, 215, 36], [1, 21, 235], [113, 16, 237], [189, 11, 221], [26, 9, 4], [246, 244, 237], [146, 122, 132], [121, 90, 48],
        [244, 19, 15], [250, 108, 2], [247, 241, 6], [15, 228, 45], [4, 0, 248], [88, 1, 243], [144, 7, 214], [15, 13, 14], [253, 245, 246], [134, 102, 127], [95, 80, 27],
        [231, 10, 0], [239, 122, 9], [234, 239, 6], [7, 207, 66], [5, 20, 247], [105, 10, 234], [167, 11, 210], [1, 17, 11], [241, 238, 255], [115, 140, 147], [87, 86, 45],
        [255, 12, 1], [244, 133, 22], [247, 246, 18], [11, 204, 22], [23, 1, 252], [103, 9, 238], [164, 16, 241], [2, 23, 9], [252, 233, 251], [146, 136, 143], [110, 59, 69],
        [254, 1, 0], [233, 115, 4], [253, 238, 6], [18, 192, 40], [6, 21, 251], [91, 14, 243], [138, 8, 228], [3, 13, 11], [242, 250, 237], [149, 138, 112], [111, 67, 34],
        [254, 19, 13], [248, 151, 13], [255, 236, 3], [13, 213, 64], [9, 14, 236], [130, 0, 242], [162, 2, 214], [4, 13, 18], [253, 248, 229], [155, 122, 135], [117, 68, 27],
        [238, 20, 12], [242, 109, 11], [231, 252, 13], [7, 219, 28], [2, 18, 252], [138, 2, 244], [185, 5, 223], [6, 8, 24], [251, 247, 252], [110, 124, 141], [91, 72, 65],
        [246, 21, 19], [239, 123, 17], [241, 240, 14], [3, 200, 27], [18, 9, 234], [113, 17, 241], [157, 22, 201], [6, 17, 18], [234, 253, 238], [132, 117, 122], [102, 87, 58],
        [250, 12, 14], [249, 129, 30], [247, 240, 24], [3, 225, 50], [28, 8, 253], [127, 1, 239], [151, 16, 232], [2, 9, 15], [245, 231, 244], [123, 107, 111], [112, 48, 52],
        [248, 23, 6], [255, 122, 6], [247, 241, 25], [12, 212, 58], [5, 24, 249], [131, 14, 249], [148, 15, 225], [23, 7, 9], [242, 255, 233], [108, 128, 113], [99, 47, 37],
        [253, 15, 16], [241, 140, 22], [245, 247, 9], [19, 214, 50], [5, 5, 255], [111, 28, 255], [185, 12, 226], [7, 21, 2], [255, 253, 240], [129, 133, 118], [110, 63, 36],
        [245, 21, 12], [232, 129, 6], [240, 246, 12], [21, 194, 37], [22, 19, 252], [123, 20, 251], [176, 12, 201], [3, 7, 21], [255, 235, 242], [130, 128, 101], [119, 59, 43],
        [247, 20, 17], [242, 129, 0], [255, 226, 3], [15, 222, 23], [15, 1, 249], [86, 14, 249], [179, 10, 203], [0, 22, 1], [230, 254, 241], [129, 150, 132], [97, 56, 61],
        [254, 26, 14], [254, 129, 19], [248, 255, 16], [18, 220, 49], [23, 7, 250], [110, 12, 245], [161, 8, 214], [0, 2, 21], [243, 252, 236], [134, 124, 117], [86, 76, 56],
        [248, 2, 12], [236, 141, 18], [248, 253, 22], [6, 188, 52], [7, 15, 245], [124, 21, 242], [151, 14, 230], [9, 18, 15], [236, 255, 249], [107, 120, 113], [115, 44, 37],

]




def equate(c1, c2):
    solution = sqrt(((c1[0]-c2[0])**2)+((c1[1]-c2[1])**2)+((c1[2]-c2[2])**2))
    return solution

def image_to_list(my_image):
# Create an image array (in list format) from an image
    my_image = PIL.Image.open(my_image)
    my_dot_array = np.asarray(my_image)
    my_dot_list = my_dot_array.tolist()
    return my_dot_list


def list_to_image(my_list, name, save=False, show=False, destination='Output'):
# Reconstuct an image object from an image array (in list format)
# Optionally, save the image as a .png file
    try:
        my_dot_array = np.asarray(my_list, dtype=np.uint8) # <-- Eureka!
    except:
        return None
    my_image = PIL.Image.fromarray(my_dot_array, mode='RGBA')
    if save == True:
        my_image.save(destination+'/'+name+'.png')
    if show == True:
        my_image.show()
    return my_image

'''
### Needs furthur testing ###
def change_extension(target_folder='Input', new_extenion = '.png', remove_original=True):
# Targeting a folder, change all images of one extension to another

    for file in os.listdir(target_folder + '/.')[1:]:
        if file.endswith(new_extenion) == False:
        
            # Isolate the file name and prepare the image
            pathname = os.path.splitext(target_folder+'/'+str(file))[0]
            filename = pathname.split('/')[-1]
            img = PIL.Image.open(target_folder+'/'+str(file))

            # Remove the orginial image, unless specified not to
            if remove_original == True:
                os.remove(target_folder+'/'+file)

            # Save the file as a .png image
            img.save(target_folder+'/'+str(filename)+new_extenion)
'''            

def purge(image_list, base=tabooIndex()):
# Purge from an image all colours that match a chosen list

    def glammerdye(colour, addAlpha=True):
        # Create a subsitute colour for a colour that appears in the Taboo Index
            # Repeat until the new_colour dosen't appear in the Taboo Index
            # Repeat until the colour falls within > 0 and < 255
        while True:
            exceptionFound = False
            new_colour = [colour[0]+randint(-5, 5), colour[1]+randint(-5, 5), colour[2]+randint(-5, 5)]
            if new_colour in tabooIndex():
                exceptionFound = True
            if new_colour[0] < 0 or new_colour[0] > 255 or new_colour[1] < 0 or new_colour[1] > 255 or new_colour[2] < 0 or new_colour[2] > 255:
                exceptionFound = True

            if exceptionFound == False:
                break

        # Add an alpha channel to the RGB colour
        if addAlpha == True and len(new_colour) == 3: #!
            new_colour.append(255)

        return new_colour

    # Iterate through each column and row, repeating for each pixel's data
    for row in range(0, len(image_list)):
        for pixel in range(0, len(image_list[row])):

            # Run analytics on the pixel
            if image_list[row][pixel][0:3] in tabooIndex():
                image_list[row][pixel] = glammerdye(image_list[row][pixel])

    return image_list


def guise(message, shell):
    # Encryt a message into an image using colours on the Taboo Index

    # Parameters:
    #   message('any string')
    #   shell([a list of image array lists])

    def colourize(character, current_colour):
        # Convert a character into a colour in the Taboo Index
        # Select a colour similar to the colour of <current_colour>
        row_length = int(len(tabooIndex()) / 62)
        character_positon = basic_characters.index(character)
        current_colour = current_colour[0:3]

        relevant_row = tabooIndex()[(character_positon*row_length):(character_positon*row_length)+row_length]

        smallest_distance = 442 # <-- 442 is the greates distance that two colour can be apart
        chosen_colour = None
        for tabooIndexColour in relevant_row:
            new_distance = equate(current_colour, tabooIndexColour)
            if new_distance < smallest_distance:
                smallest_distance = new_distance
                chosen_colour = tabooIndexColour
                
        chosen_colour.append(255) # <-- Add alpha channel
        return chosen_colour

    
    # Find total_image_size
    total_image_size = 0
    for i in range(0, len(shell)):
        this_image_size = len(shell[i])*len(shell[i][0])
        total_image_size += this_image_size

    # Ensure that the picture is large enough to fit the message,
    # Also, figure out how spread out the message should be within the image lists
    golden_ratio = floor(total_image_size / len(message))
    if golden_ratio < 1:
        return False

    # Determine the points in which an item from the message string needs to be placed, saved under <list_of_positions>
    last_position = 0
    list_of_positions = []
    for item in range(0, len(message)):
        new_position = last_position + randint(floor(pow(golden_ratio, 4/5)), golden_ratio) # Determine the range of where the pixel will be placed
        list_of_positions.append(new_position)
        last_position = new_position
        # Update Golden Ratio each repetition to ensure that the message will remain evenly distributed
        golden_ratio = floor((total_image_size - new_position) / (len(message) - item))

    # Place the items in <message> into the image lists <shell> using <list_of_positons>, created earlier
    iteration = 0
    for x in range(0, len(shell)):
        for y in range(0, len(shell[x])):
            for z in range(0, len(shell[x][y])):
                iteration += 1
                if iteration == list_of_positions[0]:
                    list_of_positions = list_of_positions[1:]
                    newest_value = message[:1]
                    message = message[1:]
                    shell[x][y][z] = colourize(newest_value, shell[x][y][z])
                    if list_of_positions == []:
                        return shell
    return shell



def sift(all_images, target_folder='Input'):
    # Decrypt an image, or list of images, returning the text hidden within

    # Iterate through each picture, column, and row, repeating for each pixel's data
    my_message = ''
    for image_list in range(0, len(all_images)):
        for row in range(0, len(all_images[image_list])):
            for pixel in range(0, len(all_images[image_list][row])):

                # Run analytics on the pixel
                if all_images[image_list][row][pixel][0:3] in tabooIndex():
                    # Find which chatacter the taboo index colour corrosponds to
                    reference_number = floor((tabooIndex().index(all_images[image_list][row][pixel][0:3]))/11)
                    my_message += basic_characters[reference_number]

    return my_message


# Sort through a list of file names and place them in the correct order
def sort_names(list_of_names):
    
    # Create a sorted list of the identifiers
    sorted_identifiers = []
    try:
        for name in list_of_names:
            sorted_identifiers.append(int(name[name.index('#')+1:name.index('.')]))
    except:
        return False
    sorted_identifiers.sort()

    # Sort the names based on the list <sorted_identifiers>
    sorted_list = []
    while list_of_names != []:
        for item in list_of_names:
            if int(item[item.index('#')+1:item.index('.')]) == sorted_identifiers[0]:
                del sorted_identifiers[0]
                sorted_list.append(item)
                list_of_names.remove(item)
    return sorted_list

    
# Estimate how long the program will take to execute
def time_estimate(image_list):
    total_time = 0
    for each_image in image_list:
        x = len(each_image)
        y = len(each_image[0])
        total_time += x*y
    total_time = total_time/13000
    total_time += (total_time*.1)

    hours = floor(total_time/3600)
    minutes = floor((total_time - hours*3600)/60)
    seconds = ceil(total_time) - (hours*3600) - (minutes*60)
    
    print_sequence = ''
    if hours != 0:
        print_sequence += str(hours)+'h  '
    if minutes != 0:
        print_sequence += str(minutes)+'m  '
    if seconds != 0:
        print_sequence += str(seconds)+'s  '
    return print_sequence

# Remove all characters unfamiliar to the program from the user's input
def scan_input(user_input):
    valid_user_input = ''
    for i in user_input:
        if i in inverter.character_list:
            valid_user_input += i
    return valid_user_input



#####################
# GUI Interface
#####################



def open_folder(target_folder):
    subprocess.call(['open', target_folder])
    
# Copy the contents of the text box to the clipboard
#copy_text = Button(gui, text='Copy', highlightbackground=bg_colour, command=copy).place(x=0, y=0)
def copy_text(text_box):
    contents = text_box.get(1.0, END)[:-1]
    gui.clipboard_clear()
    gui.clipboard_append(contents)
    
def paste_text(text_box):
    contents = gui.clipboard_get()
    text_box.insert(INSERT, contents)
    text_box.update()

def clear_text(text_box):
    text_box.delete(1.0, END)
    
def display_text(message, clear=True):
    if clear == True:
        user_input.delete(1.0, END)
    user_input.insert(INSERT, message)
    user_input.update()

def encrypt_button():
    user_message = user_input.get(1.0, END)[:-1]
    user_key = user_keycode.get(1.0, END)[:-1]
    user_keycode.delete(1.0, END)
    
    # Collect a list of all images for encryption           
    image_list = []
    for file in os.listdir('Input/.'):
        if str(file)[-4:] == '.png':
            new_addition = image_list.append(image_to_list('Input/'+file))

    # Check for exceptions, and remove all irregular characters from the user input and key
    user_message, user_key = scan_input(user_message), scan_input(user_key)
    if user_message == '':
        display_text('!Error: No message detected\nStop trying to break my program ☺')
    elif image_list == []: # <-- Ensure that at least one image is present to continue
        display_text('!Error: No image detected\nEnsure at least (1) .png images are in the Input folder')
        open_folder('Input')
    
    # If everything is good to go...                                     
    else:
        # Tell the user how long the program will take to execute
        display_text('Processing files...\nEstimated processing time remaining: '+str(time_estimate(image_list)))
        # Purge unwanted colours
        for item in image_list:
            purge(item)
        # Begin the Encryption Process
        user_message = inverter.encrypt_text(user_message, mode='encrypt', key=user_key) # <-- Text based encryption used here ###
        updated_image_list = guise(user_message, image_list)
        if updated_image_list == False:
            display_text('!Error: Image too small\n\nEnsure that the total area of your images significantly exceeds the length of your message.')
            return None
        # Save the new images to the Output folder
        image_name = 'Encryption #0'
        for each_image in updated_image_list:
            image_name = image_name[:-1] + str(int(image_name[-1])+1)
            new_image = list_to_image(my_list=each_image, name=image_name, save=True) # <-- new_image= is for testing for return None
            if new_image == None:
                display_text('!Error: Corrupted file type\n\nEnsure that all images were created in the .png format.')
                return None
        display_text('All done!\n\nCheck the Output folder for your new Image(s)!')
        open_folder('Output')

def decrypt_button():
    user_key = user_keycode.get(1.0, END)[:-1]
    user_keycode.delete(1.0, END)
    
    # Collect a list of all images for encryption 
    image_list = []
    for file in os.listdir('Input/.'):
        if str(file)[-4:] == '.png':
            image_list.append('Input/'+file)
    image_list = sort_names(image_list) # <-- After the images have been sorted, convert them into lists
    if image_list == False:
        display_text('!Error: Dumb image names.\n\nEnsure that all images end with #Number.\n\nex. pomegranate#1.png')
        return None
    
    updated_image_list = []
    for each_image in image_list:
        updated_image_list.append(image_to_list(each_image))

    # Check for exceptions
    if updated_image_list == []: # <-- Ensure that at least one image is present to continue
        display_text('!Error: No image detected\nEnsure at least (1) .png images are in the Input folder')
        open_folder('Input')

    # If everything is good to go...
    else:
        # Tell the user how long the program will take to execute, scales with the total area of the images.
        display_text('Unpacking files...\nEstimated processing time remaining: '+str(time_estimate(updated_image_list)))
        
        # Begin the Decryption process and display the uncovered text
        unveiled_message = sift(updated_image_list)
        unveiled_message = inverter.encrypt_text(unveiled_message, mode='decrypt', key=user_key) # <-- Text based encryption used here ###
        if unveiled_message == None:
            display_text('No message found.')
        else:
            display_text(unveiled_message)
                
        

def open_help(querry, dimensions='300x300', total_pages=1, current_page=1):
    global info_window
    global last_querry
    if last_querry == querry:
        info_window.destroy()
        last_querry = None
    else:
        if last_querry != None:
            info_window.destroy()
        last_querry = querry
        info_window = Toplevel()
        info_window.geometry(dimensions+'+'+str(gui.winfo_rootx()+601)+'+'+str(gui.winfo_rooty()-23))
        info_window.config(background='paleturquoise')
        info_window.title('Core Systems Information Terminal')

        # Isolate Text from file
        text = open('Info/'+querry+'.txt')
        contents = text.read()
        tutorial_text = Label(info_window, text=(contents), bg='paleturquoise', font=('Helvetica', 18)).place(x=15, y=10)

        dimensions_divider = dimensions.index('x') # <-- Allow seperation of x and y values
        if total_pages > current_page:
            next_page = Button(info_window, text='-->', highlightbackground='paleturquoise', command=lambda: open_help((querry[:-1]+str(int(querry[-1])+1)), dimensions, total_pages=total_pages, current_page=current_page+1))
            next_page.place(x=int(dimensions[:dimensions_divider])-70, y=int(dimensions[dimensions_divider+1:])-45)
        if current_page > 1:
            previous_page = Button(info_window, text='<--', highlightbackground='paleturquoise', command=lambda: open_help((querry[:-1]+str(int(querry[-1])-1)), dimensions, total_pages=total_pages, current_page=current_page-1))
            previous_page.place(x=10, y=int(dimensions[dimensions_divider+1:])-45)
        

my_font = 'Helvetica'
bg_colour = 'midnightblue'
last_querry = None

gui = Tk()
gui.geometry('600x600+0+0')
gui.title('Mumbo Jumbo - By Nem Moonglove')
gui.config(background=bg_colour)
# Labels
heading = Label(text='Welcome to Mumbo Jumbo!', fg='cornflowerblue', bg=bg_colour, font=(my_font, 35)).place(x=65, y=25)
sub_heading = Label(text='a digital pictographic encryption tool', fg='royalblue', bg=bg_colour, font=(my_font, 20)).place(x=120, y=70)
divider = Label(text='/', fg='dodgerblue', bg=bg_colour, font=(my_font, 32)).place(x=266, y=135)
key_heading = Label(text='Key Input (optional)', fg='dodgerblue', bg=bg_colour, font=(my_font, 18)).place(x=200, y=390)
# Buttons
encrypt_text = Button(gui, text='Encrypt', highlightbackground=bg_colour, command=encrypt_button).place(width=100, x=160, y=140)
decrypt_text = Button(gui, text='Decrypt', highlightbackground=bg_colour, command=decrypt_button).place(width=100, x=290, y=140)
open_input = Button(gui, text='Open Input', highlightbackground=bg_colour, command=lambda: open_folder('Input')).place(x=465, y=490)
open_output = Button(gui, text='Open Output', highlightbackground=bg_colour, command=lambda: open_folder('Output')).place(x=458, y=525)
open_image_library = Button(gui, text='Open Image Library', highlightbackground=bg_colour, command=lambda: open_folder('Image_Library')).place(x=437, y=560)
copyright_info = Button(gui, text='Ⓒ', highlightbackground=bg_colour, command=lambda: open_help('Copyright_info', '480x560')).place(width=30, x=560, y=10)
tutorial_info = Button(gui, text='h', highlightbackground=bg_colour, font=('Times 16 italic'), command=lambda: open_help('Tutorial_info_1', '550x600', total_pages=4, current_page=1)).place(width=30, x=560, y=40)
text_info = Button(gui, text='i', highlightbackground=bg_colour, font=('Times 16 italic'), command=lambda: open_help('Text_info', '400x350')).place(width=25, x=404, y=175)
key_info = Button(gui, text='i', highlightbackground=bg_colour, font=('Times 16 italic'), command=lambda: open_help('Key_info', '350x470')).place(width=25, x=404, y=420)

copy_input = Button(gui, text='Copy', highlightbackground=bg_colour, font=('Times 16 italic'), command=lambda: copy_text(user_input)).place(x=70, y=190)
paste_input = Button(gui, text='Paste', highlightbackground=bg_colour, font=('Times 16 italic'), command=lambda: paste_text(user_input)).place(x=70, y=225)
clear_input = Button(gui, text='Clear', highlightbackground=bg_colour, font=('Times 16 italic'), command=lambda: clear_text(user_input)).place(x=70, y=260)
copy_key = Button(gui, text='Copy', highlightbackground=bg_colour, font=('Times 16 italic'), command=lambda: copy_text(user_keycode)).place(x=170, y=480)
paste_key = Button(gui, text='Paste', highlightbackground=bg_colour, font=('Times 16 italic'), command=lambda: paste_text(user_keycode)).place(x=240, y=480)
clear_key = Button(gui, text='Clear', highlightbackground=bg_colour, font=('Times 16 italic'), command=lambda: clear_text(user_keycode)).place(x=310, y=480)

# Entry Window
user_input = Text(gui, width=20, height=3, bg='lightsteelblue', bd=3, highlightthickness=4, highlightbackground='darkslateblue', highlightcolor='mediumslateblue', relief=RAISED, selectbackground='lightblue', wrap=WORD, font=('Helvetica 14'))
user_input.place(height=200, width=250, x=150, y=175)
user_keycode = Text(gui, width=20, height=3, bg='lightsteelblue', bd=2, highlightthickness=3, highlightbackground='darkslateblue', highlightcolor='mediumslateblue', relief=RAISED, selectbackground='lightblue', wrap=WORD, font=('x', 11))
user_keycode.place(height=50, width=250, x=150, y=420)

gui.mainloop()


