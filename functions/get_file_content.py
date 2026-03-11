from config import MAX_CHAR_LIMIT
import os

def get_file_content(working_directory, file_path):

    try:
        working_dir_abs = os.path.abspath(working_directory)
        if not os.path.isdir(working_dir_abs):
            raise ValueError(f'Error: "{working_directory}" is not a directory')

        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_dir:
            raise ValueError(f'Error: Cannot list "{file_path}" as it is outside the permitted working directory')
    
        if not os.path.isfile(target_file):
            raise ValueError(f'Error: File not found or is not a regular file: "{file_path}"')

        with open(target_file, 'r') as f:
            content = f.read(MAX_CHAR_LIMIT)
            if f.read(1):  # Check if there's more content beyond the limit
                content += f'[...file "{file_path}" truncated at {MAX_CHAR_LIMIT} characters...]'
            
            if not content:
                raise ValueError(f'Error: File "{file_path}" is empty or could not be read')

            return content

    except Exception as e:
        return str(e)