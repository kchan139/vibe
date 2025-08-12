#!/usr/bin/env python3
import os
from datetime import datetime
import argparse

# Default output file path
OUTPUT_FILE = "file_ingest.txt"

# Default directories to ignore
DEFAULT_IGNORE_DIRS = {".git", "node_modules", "venv", "__pycache__", ".env"}


def scan_files(directories, output_file=OUTPUT_FILE, ignore_dirs=None):
    """
    Scan specified directories and write the contents of all files to a text file.

    Args:
        directories (list): List of directory paths to scan
        output_file (str): Path to the output text file
        ignore_dirs (set): Set of directory names to ignore
    """
    if ignore_dirs is None:
        ignore_dirs = DEFAULT_IGNORE_DIRS

    with open(output_file, "w", encoding="utf-8", errors="replace") as f:
        f.write(
            f"File Contents Scan - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        f.write(f"Ignoring directories: {', '.join(sorted(ignore_dirs))}\n\n")

        for directory in directories:
            if not os.path.exists(directory):
                print(f"ERROR: Directory '{directory}' does not exist.")
                continue

            if not os.path.isdir(directory):
                print(f"ERROR: '{directory}' is not a directory.")
                continue

            f.write(f"Scanning files in: {os.path.abspath(directory)}\n")

            # Scan all subdirectories recursively
            for root, dirs, files in os.walk(directory):
                # Remove ignored directories from dirs list to prevent os.walk from entering them
                dirs[:] = [d for d in dirs if d not in ignore_dirs]

                for file in sorted(files):
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, directory)

                    # Skip binary files and very large files
                    if (
                        is_binary_file(file_path)
                        or os.path.getsize(file_path) > 1024 * 1024
                    ):  # Skip files > 1MB
                        continue

                    f.write(f"FILE: {rel_path}\n")

                    try:
                        # Read the file content
                        with open(
                            file_path, "r", encoding="utf-8", errors="replace"
                        ) as file_handle:
                            content = file_handle.read()
                            f.write(content)
                    except Exception as e:
                        f.write(f"[ERROR READING FILE: {rel_path} - {str(e)}]\n")

                    f.write("\n\n")

    print(f"Scan complete. Results saved to {os.path.abspath(output_file)}")


def is_binary_file(file_path):
    """
    Check if a file is binary by reading a small chunk and looking for null bytes.
    """
    try:
        chunk_size = 1024
        with open(file_path, "rb") as f:
            chunk = f.read(chunk_size)
            if b"\x00" in chunk:  # Null bytes indicate binary file
                return True

            # Additional check for non-text characters
            text_chars = bytearray(
                {7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)) - {0x7F}
            )
            return bool(chunk.translate(None, text_chars))
    except Exception:
        return True  # Treat unreadable files as binary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Ingest files from a directory into a text file."
    )
    parser.add_argument("directory", help="Directory to scan and ingest files from")
    parser.add_argument(
        "-o",
        "--output",
        default=OUTPUT_FILE,
        help=f"Output file path (default: {OUTPUT_FILE})",
    )
    parser.add_argument(
        "--ignore",
        nargs="*",
        default=list(DEFAULT_IGNORE_DIRS),
        help=f'Directories to ignore (default: {" ".join(sorted(DEFAULT_IGNORE_DIRS))})',
    )

    args = parser.parse_args()

    # Convert ignore list to set
    ignore_dirs = set(args.ignore) if args.ignore else set()

    scan_files([args.directory], args.output, ignore_dirs)
