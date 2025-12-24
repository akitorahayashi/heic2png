import os
from PIL import Image
import pillow_heif

def main():
    # Specify the source folder and the output folder
    input_folder = "input/heic/"
    output_folder = "output/png/"

    # Get HEIC files in the source folder
    heic_files = [f for f in os.listdir(input_folder) if f.endswith('.HEIC')]

    for heic_file in heic_files:
        # Create the path for the HEIC file
        heic_path = os.path.join(input_folder, heic_file)
        
        # Create the path for the PNG file
        png_file = os.path.splitext(heic_file)[0] + '.png'
        png_path = os.path.join(output_folder, png_file)
        
        # Convert HEIC file to PNG
        heif_file = pillow_heif.read_heif(heic_path)
        image = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )
        image.save(png_path, 'PNG')
        
        print(f'Converted {heic_file} to {png_file}.')

    print('Conversion completed.')


if __name__ == "__main__":
    main()
