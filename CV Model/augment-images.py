from PIL import Image
from pathlib import Path
import os
import PIL
import string
import random
import pyautogui
bird_species = [
    'American Crow',
    'American Goldfinch',
    'American Robin',
    'Black Capped Chickadee',
    'Blue Jay',
    'Brown Headed Cowbird',
    'Common Grackle',
    'Dark Eyed Junco',
    'Downy Woodpecker',
    'European Starling',
    'Hairy Woodpecker',
    'House Finch',
    'House Sparrow',
    'Male Northern Cardinal',
    'Mourning Dove',
    'Purple Finch',
    'Red Bellied Woodpecker',
    'Red Winged Blackbird',
    'Song Sparrow',
    'Tufted Titmouse',
    'White Breasted Nuthatch'
]
bird_species_files = [
    Path(r'C:\Users\kirby\Desktop\BirdUp\EtcFiles\Backyard-Bird-Dataset\train75\American Crow'),
    Path(r'C:\Users\kirby\Desktop\BirdUp\EtcFiles\Backyard-Bird-Dataset\train75\American Goldfinch'),
    Path(r'C:\Users\kirby\Desktop\BirdUp\EtcFiles\Backyard-Bird-Dataset\train75\American Robin'),
    Path(r'C:\Users\kirby\Desktop\BirdUp\EtcFiles\Backyard-Bird-Dataset\train75\Black Capped Chickadee'),
    Path(r'C:\Users\kirby\Desktop\BirdUp\EtcFiles\Backyard-Bird-Dataset\train75\Blue Jay'),
    Path(r'C:\Users\kirby\Desktop\BirdUp\EtcFiles\Backyard-Bird-Dataset\train75\Brown Headed Cowbird'),
    Path(r'C:\Users\kirby\Desktop\BirdUp\EtcFiles\Backyard-Bird-Dataset\train75\Common Grackle'),
    Path(r'C:\Users\kirby\Desktop\BirdUp\EtcFiles\Backyard-Bird-Dataset\train75\Dark Eyed Junco'),
    Path(r'C:\Users\kirby\Desktop\BirdUp\EtcFiles\Backyard-Bird-Dataset\train75\Downy Woodpecker'),
    Path(r'C:\Users\kirby\Desktop\BirdUp\EtcFiles\Backyard-Bird-Dataset\train75\European Starling'),
    Path(r'C:\Users\kirby\Desktop\BirdUp\EtcFiles\Backyard-Bird-Dataset\train75\Hairy Woodpecker'),
    Path(r'C:\Users\kirby\Desktop\BirdUp\EtcFiles\Backyard-Bird-Dataset\train75\House Finch'),
    Path(r'C:\Users\kirby\Desktop\BirdUp\EtcFiles\Backyard-Bird-Dataset\train75\House Sparrow'),
    Path(r'C:\Users\kirby\Desktop\BirdUp\EtcFiles\Backyard-Bird-Dataset\train75\Male Northern Cardinal'),
    Path(r'C:\Users\kirby\Desktop\BirdUp\EtcFiles\Backyard-Bird-Dataset\train75\Mourning Dove'),
    Path(r'C:\Users\kirby\Desktop\BirdUp\EtcFiles\Backyard-Bird-Dataset\train75\Purple Finch'),
    Path(r'C:\Users\kirby\Desktop\BirdUp\EtcFiles\Backyard-Bird-Dataset\train75\Red Bellied Woodpecker'),
    Path(r'C:\Users\kirby\Desktop\BirdUp\EtcFiles\Backyard-Bird-Dataset\train75\Red Winged Blackbird'),
    Path(r'C:\Users\kirby\Desktop\BirdUp\EtcFiles\Backyard-Bird-Dataset\train75\Song Sparrow'),
    Path(r'C:\Users\kirby\Desktop\BirdUp\EtcFiles\Backyard-Bird-Dataset\train75\Tufted Titmouse'),
    Path(r'C:\Users\kirby\Desktop\BirdUp\EtcFiles\Backyard-Bird-Dataset\train75\White Breasted Nuthatch')
]

# =============================================
# this loops through all pictures in a subdir

j = 0

# =============================================

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# for j in range(len(bird_species)):
base_path = str(bird_species_files[j])
for filename in os.listdir(base_path):
    try:
        if ('.jpg') not in filename:
            os.rename(filename, randomString() + '.jpg')
        if ('%') in filename:
            print('BAD FILE NAME\t:' + filename)
            new_filename = os.rename(filename, randomString() + '.jpg')
            print('NEW FILE NAME\t:' + str(new_filename))
    except FileNotFoundError:
        print('ERROR: CANNOT RENAME FILE')
        continue

for filename in os.listdir(base_path):
    try:
        image = Image.open(filename)
        image_rot_90 = image.rotate(90)
        image_rot_90.save('{}_rot_90.jpg'.format(filename[:-4]))
        print('Image rotated 90 degrees')
        image = Image.open(filename)
        image_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
        image_flip.save('{}_flip.jpg'.format(filename[:-4]))
        print('Image flipped successfully')
    except OSError:
        print('ERROR: ROTATE OR FLIP')
        continue

for filename in os.listdir(base_path):
    try:
        image = Image.open(filename)
        greyscale_image = image.convert('L')
        greyscale_image.save('{}_greyscale.jpg'.format(filename[:-4]))
        print('Image greyscaled sucessfully')
    except OSError:
        print('ERROR: GREYSCALE')
        continue

for filename in os.listdir(base_path):
    try:
        image = Image.open(filename)
        image.thumbnail((300, 300))
        image.save(filename)
        print('Image resized successfully')
    except OSError:
        print('ERROR: RESIZING')
        continue

i = 0
### renames all files to gibberish. Its useful, I swear
# for filename in os.listdir(base_path):
#     try:
#         new_filename = randomString() + ".jpg"
#         os.rename(filename, new_filename) 
#         i -= -1
#         print('Image renamed sucessfully')
#     except PermissionError:
#         print('ERROR: NAMING')
#         continue

for filename in os.listdir(base_path):
    try:
        new_filename = bird_species[j] + '_train_' + "__" + str(i) + ".jpg"
        os.rename(filename, new_filename) 
        i -= -1
        print('Image renamed sucessfully')
    except PermissionError:
        print('ERROR: NAMING')
        continue

print("=============================================")
print('Please do {} next'.format(bird_species[j+1]))
print("Change j to {}".format(j+1))
print('=============================================')

pyautogui.moveTo(414, 1125)
pyautogui.click()
pyautogui.write("cd " + '"' + str(bird_species_files[j+1]) + '"')

