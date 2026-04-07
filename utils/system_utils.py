import os
import sys
import subprocess

def delete_script():
    try:
        os.remove(sys.argv[0])
        print("Script deleted successfully.")
    except Exception as e:
        print(f"Error deleting script: {e}")

def run_main_script():
    try:
        subprocess.run(['python', 'main.py'], check=True)
    except Exception as e:
        print(f"Error running main.py: {e}")
