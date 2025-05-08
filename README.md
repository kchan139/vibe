# Quick Ingestor

Description:
A script to recursively scan a directory and save the contents of all text files (excluding binaries and files >1MB) into a single output file.

Installation:
1. Save the script as `ingest.py` in your home directory (`~`).
2. Make it executable:
   chmod +x ~/ingest.py

Usage:
./ingest.py [TARGET_DIRECTORY] [-o OUTPUT_FILE]

Examples:
1. Scan a directory with default output (file_ingest.txt):
   ./ingest.py ~/my_project/src

2. Specify a custom output file:
   ./ingest.py ~/my_project/src -o project_contents.txt

Options:
  -h, --help    Show help message
  -o OUTPUT     Specify output file (default: file_ingest.txt)

Notes:
- Skips binary files and files larger than 1MB.
- Output includes relative file paths and contents.
- Errors (e.g., unreadable files) are printed to the console.
