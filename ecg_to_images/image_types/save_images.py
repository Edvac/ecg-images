import logging
import os


def save_image(img, folder_name, filename):
    """Create directories for each patient and store their's image files"""

    if not os.path.isdir(folder_name):
        try:
            # Check if the a patient's directory exists
            os.makedirs(folder_name)
        except OSError:
            if not os.path.isdir(folder_name):
                logging.getLogger().exception("The directory for file: " + filename + " Already exists: ", OSError)
                raise

    img.save(folder_name + "/" + filename + ".png")
    print("Saving image for patient: " + filename)

def get_absolute_file_names(directory_name):
    list = [os.path.join(directory_name, f) for f in os.listdir(directory_name) if f.endswith('.txt')]
    return [os.path.join(directory_name, f) for f in os.listdir(directory_name) if f.endswith('.txt')]

