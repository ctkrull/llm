import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        valid_file_path = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs      
        if not valid_file_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_file.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ['python', target_file]
        if args:
            command.extend(args)

        CompletedProcess = subprocess.run(command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30)
        
        output = ""

        if CompletedProcess.returncode != 0:
            output += f"Process exited with code {CompletedProcess.returncode}\n"
        if CompletedProcess.stdout:
            output += f"STDOUT:\n{CompletedProcess.stdout}"
        if CompletedProcess.stderr:
            output += f"STDERR:\n{CompletedProcess.stderr}"
        if not output:
            output = "No output produced."

        return output

    except Exception as e:
        return f"Error: executing Python file: {e}"