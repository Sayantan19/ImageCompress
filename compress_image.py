import numpy as np
from PIL import Image

def compress_image(input_path, output_path):
    # Open the image
    image = Image.open(input_path).convert('L')  # Convert to greyscale

    # Resize the image to a multiple of 8 for simplicity
    width, height = image.size
    width = (width // 8) * 8
    height = (height // 8) * 8
    image = image.resize((width, height))

    # Convert image to a NumPy array for easier manipulation
    img_array = np.array(image)

    # Apply column-wise scanning and optimization
    compressed_array = img_array.transpose().flatten()
    sorted_values = sorted(set(compressed_array))
    optimized_array = [sorted_values.index(value) for value in compressed_array]

    # Convert the optimized array back to the image shape
    optimized_image = np.array(optimized_array).reshape((height, width))

    # Create a new Image object from the optimized image array
    optimized_image = Image.fromarray(optimized_image, mode='L')

    # Save the optimized image
    optimized_image.save(output_path)

# Example usage
input_image_path = r"C:\Users\SHARANYA PAL\OneDrive\Documents\GitHub\image_compression\input_image.jpeg"
output_image_path = r"C:\Users\SHARANYA PAL\OneDrive\Documents\GitHub\image_compression\compressed_image.jpeg"

compress_image(input_image_path, output_image_path)
