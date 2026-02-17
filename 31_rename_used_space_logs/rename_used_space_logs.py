import os
import re


def rename_files(target_directory):
    """
    Rename files from format: space_31-12-2025--22-10
    to format: space_20251231-22-10

    Args:
        directory: Directory containing the files (default: current directory)
    """

    # Compile regex pattern to match the filename format
    pattern = re.compile(r"^(space_)(\d{2})-(\d{2})-(\d{4})--(\d{2}-\d{2})(\.[^.]+)?$")

    #  Get all files in the directory
    for filename in os.listdir(target_directory):
        filepath = os.path.join(target_directory, filename)

        # Skip if it's a directory
        if os.path.isdir(filepath):
            continue

        # Try to match the pattern
        match = pattern.match(filename)

        if match:
            # Extract parts from the filename
            prefix = match.group(1)  # "space_"
            day = match.group(2)  # "31"
            month = match.group(3)  # "12"
            year = match.group(4)  # "2025"
            time_part = match.group(5)  # "22-10"
            extension = match.group(6) or ""  # File extension (if any)

            # Create new filename
            new_filename = f"{prefix}{year}{month}{day}-{time_part}{extension}"

            # Construct full paths
            old_path = os.path.join(target_directory, filename)
            new_path = os.path.join(target_directory, new_filename)

            # Rename the file

            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_filename}")
            except OSError as e:
                print(f"Error renaming {filename}: {e}")
        else:
            # Skip files that don't match the pattern
            print(f"Skipped, doesn't match pattern: {filename}")


if __name__ == "__main__":
    target_directory = input("\nEnter directory with logs: ").strip()

    print(f"Processing files in: {target_directory}")

    rename_files(target_directory)

    print("Done!")
