#!/usr/bin/env python3
import os
import subprocess
import sys

def main():
    # Determine the base directory.
    if getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable)
        # Use system python to avoid recursive call of run.exe.
        python_cmd = "python"
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        python_cmd = sys.executable

    main_script = os.path.join(base_dir, "main.py")
    log_file = os.path.join(base_dir, "log.txt")

    # Check if main.py exists.
    if not os.path.exists(main_script):
        error_msg = f"Error: main.py not found in {base_dir}"
        print(error_msg)
        with open(log_file, "w") as f:
            f.write(error_msg)
        sys.exit(1)

    try:
        # Run main.py and capture output.
        result = subprocess.run(
            [python_cmd, main_script],
            capture_output=True,
            text=True,
            check=True
        )
        msg = f"main.py executed successfully..."
        print(msg)
        # Optionally, print output from main.py.
        print(result.stdout)
    except subprocess.CalledProcessError as err:
        # If an error occurs, write both stdout and stderr to log.txt.
        with open(log_file, "w") as log:
            log.write("Error executing main.py\n")
            log.write(f"Return code: {err.returncode}\n\n")
            log.write("Standard Output:\n")
            log.write(err.stdout or "")
            log.write("\n\nStandard Error:\n")
            log.write(err.stderr or "")
        print("An error occurred while executing main.py. See log.txt for details.")
        sys.exit(err.returncode)


if __name__ == '__main__':
    main()

