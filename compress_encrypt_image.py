import numpy as np
from PIL import Image
from scipy.fft import *

# Compression
def transform_coding(image):
    # Perform Discrete Cosine Transform (DCT) on the image
    transformed_image = dctn(image, norm='ortho')

    return transformed_image

def quantization(image):
    # Perform quantization on the transformed image
    # Replace this with the actual quantization implementation
    quantized_image = image

    np.savetxt('quantized_values.txt', quantized_image, fmt='%d')
    return quantized_image

def entropy_coding(image):
    # Perform entropy coding (e.g., Huffman coding, arithmetic coding)
    # Replace this with the actual entropy coding implementation
    encoded_image = image

    return encoded_image

def compression(image):
    # Convert image to NumPy array
    img_array = np.array(image)

    # Perform compression steps
    transformed_image = transform_coding(img_array)
    quantized_image = quantization(transformed_image)
    encoded_image = entropy_coding(quantized_image)

    return encoded_image

# Encryption
def aes_encryption(image):
    # Implement AES encryption algorithm
    cipher_key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # Example cipher key

    def sub_bytes(position):
        # Replace this with sub_bytes() implementation
        return position

    def shift_element_rows(position):
        # Replace this with shift_element_rows() implementation
        return position
    
    def sub_bytes(position):
        # Replace this with actual sub_bytes() implementation
        return position

    # Replace the following AES encryption algorithm steps with the actual implementation
    def cipher(input_bytes, output_bytes, cipher_key):
        byte_position = [0] * 10
        position = byte_position.copy()

        position = np.logical_xor(position, cipher_key[0])
        for p in range(1, len(cipher_key) - 1):
            position = sub_bytes(position)
            position = shift_element_rows(position)
            position = mix_element_columns(position)
            position = np.logical_xor(position, cipher_key[p])
        
        position = sub_bytes(position)
        position = shift_element_rows(position)
        position = np.logical_xor(position, cipher_key[-1])

        return position

    encrypted_image = cipher(image, image.copy(), cipher_key)

    return encrypted_image

def xor_encryption(image):
    # Implement XOR encryption algorithm
    # Replace this with the actual XOR encryption implementation
    encrypted_image = image

    return encrypted_image

# Column-wise scanning and optimization
def column_wise_scanning(image):
    # Perform column-wise scanning and optimization
    # Replace this with the actual column-wise scanning and optimization implementation
    optimized_image = image

    return optimized_image

# Example usage
input_image_path = "Coach.jpg"
output_image_path_1 = "compressed_encrypted_image_aes.jpeg"
output_image_path_2 = "compressed_encrypted_image_xor.jpeg"



# Load input image
image = Image.open(input_image_path).convert('L')  # Convert to greyscale

# Compression
compressed_image = compression(image)

# Encryption (choose either AES or XOR encryption)
encrypted_image_1 = aes_encryption(compressed_image)
# encrypted_image = xor_encryption(compressed_image)
encrypted_image_2 = xor_encryption(compressed_image)

# Column-wise scanning and optimization
optimized_image_1 = column_wise_scanning(encrypted_image_1)
optimized_image_2 = column_wise_scanning(encrypted_image_2)

# Create a new Image object from the optimized image array
output_image_aes = Image.fromarray(optimized_image_1, mode='L')
output_image_xor = Image.fromarray(optimized_image_2, mode='L')

np.savetxt('output_values_aes.txt', optimized_image_1, fmt='%d')
np.savetxt('output_values_xor.txt', optimized_image_2, fmt='%d')

# Save the compressed, encrypted, and optimized image
output_image_aes.save(output_image_path_1)
output_image_xor.save(output_image_path_2)
