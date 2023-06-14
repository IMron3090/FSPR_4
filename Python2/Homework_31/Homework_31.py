import sys
from pathlib import Path
from PIL import Image


directory_to_read, directory_to_write = sys.argv[1:]


Path(directory_to_write).mkdir(parents=True, exist_ok=True)


for file_to_convert in Path(directory_to_read).iterdir():
    image = Image.open(file_to_convert)
    
    extension = file_to_convert.suffix
    
    filename = file_to_convert.stem
    
    
    if extension == ".png":
        image.save(Path(directory_to_write, filename + ".jpg"))
    elif extension == ".jpg":
        image.save(Path(directory_to_write, filename + ".png"))

        
# 2


