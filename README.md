# heic2png

A Python utility for batch converting HEIC images to PNG format.

## Project Objective

The goal of this project is to provide a simple, automated script to convert multiple `.HEIC` image files into `.png` format. It uses the `pillow` and `pillow-heif` libraries to handle the image processing, reading from a specific input directory and saving the converted files to an output directory.

## Quick Start

Follow these steps to get the converter up and running:

1.  **Install Prerequisites**:
    Ensure you have Python 3.12 or higher installed. This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

2.  **Install Dependencies**:
    ```bash
    uv sync
    ```

3.  **Setup Directories**:
    Create the required input and output directories:
    ```bash
    mkdir -p input/heic
    mkdir -p output/png
    ```

4.  **Run the Script**:
    ```bash
    uv run python main.py
    ```

## Project Structure

The project relies on a specific directory structure for input and output operations:

```text
.
├── input/
│   └── heic/          # Place your .HEIC files here for conversion
├── output/
│   └── png/           # Converted .png files will be saved here
├── main.py            # The main script that performs the conversion
├── pyproject.toml     # Project configuration and dependencies
├── uv.lock            # Lock file for dependencies
└── README.md          # Project documentation
```

## Usage and Configuration

### Configuration
The script uses hardcoded paths for input and output. No external configuration file is required, but you must adhere to the folder structure.
- **Input Folder**: `input/heic/`
- **Output Folder**: `output/png/`

### Running the Conversion
1.  Place your `.HEIC` files into the `input/heic/` folder.
    *   **Important**: The script explicitly looks for files with the **`.HEIC`** extension (case-sensitive). Ensure your files have uppercase extensions or rename them.
2.  Run the script:
    ```bash
    uv run python main.py
    ```
3.  The script will print the status of each file conversion.
4.  Find your converted images in `output/png/`.

## Development

### Requirements
*   Python >= 3.12
*   `uv` (for package management)

### Running Tests
Currently, there are no automated tests. You can verify changes by placing sample `.HEIC` files in the input directory and running the script to ensure they are converted correctly to `.png` in the output directory without errors.

### Contributing
1.  Clone the repository.
2.  Install dependencies using `uv sync`.
3.  Modify `main.py` as needed.
4.  Verify your changes by running the script with test images.
