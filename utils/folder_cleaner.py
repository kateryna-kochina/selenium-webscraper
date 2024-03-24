import logging
import os


def clear_folder(folder_path):
    '''
    Clears all files within a specified folder.

    Args:
        folder_path (str): Path to the folder to be cleared.

    Returns:
        None
    '''
    if os.path.exists(folder_path):  # Check if the folder exists
        # Iterate over files in the folder
        for file_name in os.listdir(folder_path):
            # Get the full file path
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):  # Check if it's a file
                os.remove(file_path)  # Remove the file
        # Log success
        logging.info(f'Folder cleared successfully by path {folder_path}.')
    else:
        # Log if folder does not exist
        logging.info(f'{folder_path} folder does not exist.')
