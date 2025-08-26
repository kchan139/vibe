# Quick Scanner

A script to recursively scan a directory and save the contents of all text files (excluding binaries and files >1MB) into a single output file.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/kchan139/vibe.git
   cd vibe
   ```

2. Make the script executable:

   ```bash
   chmod +x scan.py
   ```

3. Create a symlink in `~/.local/bin` (so you can call `scan` from anywhere):

   ```bash
   ln -s $(pwd)/scan.py ~/.local/bin/scan
   ```

   > Make sure `~/.local/bin` is in your `$PATH` (most Linux/macOS setups already include it).

## Usage

   ```bash
   scan [TARGET_DIRECTORY] [-o OUTPUT_FILE] [--ignore PATTERN]
   ```

## Examples

1. Scan a directory with default output (`scanned_contents.txt`):

   ```bash
   scan ~/my_project/src
   ```

2. Specify a custom output file:

   ```bash
   scan ~/my_project/src -o project_contents.txt
   ```

3. Use custom ignore patterns:

   ```bash
   scan ~/my_project/src --ignore "*.pyc" "test_*" "__pycache__"
   ```

## Options

* `-h, --help`    Show help message
* `-o OUTPUT`     Specify output file (default: `scanned_contents.txt`)
* `--ignore PATTERN`  Additional ignore patterns

## Notes

* Default ignore patterns are specified in `ignore.py`.
* Skips binary files and files larger than 1MB.
* Output includes relative file paths and contents.
* Errors (e.g., unreadable files) are printed to the console.
* Supports glob patterns (`*.ext`, `prefix*`, `*middle*`) and negated patterns (`!pattern`).
