import os
from PIL import Image
import hashlib

counter = 0
namesAndHashes = []

print()

# Get all images in the current dir
extensions = ('.jpeg', '.jpg', '.png', '.gif', '.bmp') # Define the extension of image files
current_dir = os.getcwd() # Get the current directory
for filename in os.listdir(current_dir): # Loop over all files in the directory
    if filename.endswith(extensions): # Check if the file is an image
        
        counter = counter + 1

        # hash image
        with Image.open(filename) as im:
            binary_data = im.tobytes() # Convert the image to a binary string
            hash_object = hashlib.sha256() # Create a new SHA-256 hash object     
            hash_object.update(binary_data) # Update the hash object with the binary data
            image_hash = hash_object.hexdigest() # Get the hexadecimal representation of the hash

            # Add to array
            namesAndHashes.append([filename, image_hash])

# Sort array
namesAndHashes.sort(key=lambda namesAndHashes:namesAndHashes[1]) 

# print the whole list
print('Checking these ' + str(counter) + ' images:')
for i in range(0, counter):
    print('   ➡️  ' + namesAndHashes[i][0])
print()

# Compare hashes
prevIsDifferent = False # true means that the prev loop iteration found a double
for i in range(0, counter-1): # counter-1 because I check with the next image, and the next image of the last image doesn't exist

    if prevIsDifferent == False:

        if namesAndHashes[i][1] == namesAndHashes[i+1][1]:
            print('❌ ' + namesAndHashes[i][1] + ' ➡️  ' + namesAndHashes[i][0])
            prevIsDifferent = True
        else:
            print('🟢 ' + namesAndHashes[i][1])
            prevIsDifferent = False
    
    else:
        print('❌ ' + namesAndHashes[i][1] + ' ➡️  ' + namesAndHashes[i][0])

# the last image was already checked in the loop
lastItem = counter - 1
if prevIsDifferent == False:
    print('❌ ' + namesAndHashes[lastItem][1] + ' ➡️  ' + namesAndHashes[lastItem][0])
else:
    print('🟢 ' + namesAndHashes[lastItem][1])

print()