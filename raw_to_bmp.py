import numpy as np
from PIL import Image
import os

def raw_to_bmp(input_path, output_path, width, height):
    # Read raw file
    with open(input_path, "rb") as f:
        raw_data = f.read()

    # Convert raw bytes to numpy array
    img_array = np.frombuffer(raw_data, dtype=np.uint8)

    # Expected size for RGB image
    expected_size = width * height * 3

    # Handle size mismatches safely
    if len(img_array) > expected_size:
        print("[INFO] RAW file larger than expected, trimming extra data...")
        img_array = img_array[:expected_size]
    elif len(img_array) < expected_size:
        print("[INFO] RAW file smaller than expected, padding with black...")
        img_array = np.pad(img_array, (0, expected_size - len(img_array)), 
                           mode='constant', constant_values=0)

    # Reshape array into (height, width, RGB)
    img_array = img_array.reshape((height, width, 3))

    # Convert to image and save as BMP
    img = Image.fromarray(img_array)
    img.save(output_path)

    print(f"[SUCCESS] Converted '{os.path.basename(input_path)}' -> '{os.path.basename(output_path)}'")

