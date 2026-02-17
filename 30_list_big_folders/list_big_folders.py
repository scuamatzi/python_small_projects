from modules.directory_file_types import file_types
from modules.directory_size import get_directory_size, format_size, format_size_v2
import os


def main():
    """
    This scripts shows:
    - top 5 folders with bigger size
    - file types for those 5 folders
    """

    # Get directory to analyze
    directory = input("\nDirectory to analyze: ").strip()

    subfolders = []

    # Create list of subfolders sizes
    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                folder_size = get_directory_size(item_path)
                subfolders.append((item, folder_size))
    except PermissionError:
        print("Permission denied accessing some subfolders!")
    except Exception as e:
        print(f"Error getting folder sizes!: {e}")

    # Sort subfolders by size
    sorted_subfolders_by_size = sorted(subfolders, key=lambda x: x[1], reverse=True)

    # select top 10 bigger subfolders
    top_folders = sorted_subfolders_by_size[:10]

    # Print top 10 bigger subfolders
    print("\n" + "=" * 60)
    print("  TOP 5 FOLDERS WITH BIGGER SIZES")
    print("=" * 60)

    for folder, size in top_folders:
        print(f"  - {folder:<20}  {format_size_v2(size):>12}")

    # Print top 10 file types for each subfolder
    print("\n" + "=" * 60)
    print("  TOP 10 FILE TYPES FOR EACH SUBFOLDER")
    print("=" * 60)

    # Get file types for each bigger subfolder
    for folder, _ in top_folders:
        print("\n" + "-" * 45)
        print(f"  {folder}")
        print("-" * 45)
        file_types(os.path.join(directory, folder), top_n=10)


if __name__ == "__main__":
    main()
