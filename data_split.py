try:
    import os
    import random
    import shutil

    # Define the paths of the 'images' folder and the new folder
    images_folder_path = 'data\\images'
    train_folder_path = 'data\\train\\images'
    test_folder_path = 'data\\test\\images'
    val_folder_path = 'data\\val\\images'

    # Count the total number of images in the 'images' folder
    total_images_count = len(os.listdir(images_folder_path))

    # Calculate the count of images to move to the new folder
    images_test = int(0.125 * total_images_count)
    images_val = int(0.125 * total_images_count)


    # Get a list of all the images in the 'images' folder
    image_names = os.listdir(images_folder_path)

    # Shuffle the image names list to get random images
    random.shuffle(image_names)

    # Move the first 'images_to_move_count' number of images to the new folder
    for i in range(images_test):
        image_path = os.path.join(images_folder_path, image_names[i])
        new_image_path = os.path.join(test_folder_path, image_names[i])
        shutil.move(image_path, new_image_path)

    # Get a list of all the images in the 'images' folder
    image_names = os.listdir(images_folder_path)

    # Shuffle the image names list to get random images
    random.shuffle(image_names)    

    for i in range(images_val):
        image_path = os.path.join(images_folder_path, image_names[i])
        new_image_path = os.path.join(val_folder_path, image_names[i])
        shutil.move(image_path, new_image_path)

    # Loop through the files in the source folder
    for filename in os.listdir(images_folder_path):
        # Check if the file is an image by checking the file extension
        if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
            # Construct the source and destination paths for the image file
            source_path = os.path.join(images_folder_path, filename)
            destination_path = os.path.join(train_folder_path, filename)
            # Move the image file to the destination folder
            shutil.move(source_path, destination_path)
except:
    print("error")


try:
    for folder in ['train' , 'test' , 'val']:
        for file in os.listdir(os.path.join('data' , folder , 'images')):
            filename = file.split('.')[0]+'.json'
            existing_filepath = os.path.join('data' , 'labels' , filename)
            if os.path.exists(existing_filepath):
                new_filepath = os.path.join('data' , folder , 'labels' , filename)
                os.replace(existing_filepath , new_filepath)
except:
    print("error")