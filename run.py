# runs the main.py file from the same directory
from settings import filepath
import subprocess

subprocess.run(['python', filepath + '/main.py'])