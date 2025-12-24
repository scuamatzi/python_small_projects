import os


def clean_space_before_prefix():
    extension = input("Write the extension: ")

    if not extension:
        print("No extension entered, exiting...")
        return

    current_dir = os.path.dirname(os.path.abspath(__file__))

    all_files = [f for f in os.listdir(current_dir) if os.path.isfile(f)]
    files_to_work = [f for f in all_files if f.endswith(f".{extension}")]

    for filename in files_to_work:
        if f" .{extension}" in filename:
            new_filename = filename.replace(f" .{extension}", f".{extension}")

            if os.path.exists(new_filename):
                print(f"Skipping '{filename}' -> '{new_filename}' already exists!")
                continue

            try:
                os.rename(filename, new_filename)
                print(f"Renamed: {filename} -> {new_filename}")
            except Exception as e:
                print(f"Error renaming '{filename}': {e}")


def main():
    print("\nThis script cleans the space before extension like:")
    print("audio .mp3 -> audio.mp3")
    print("\nThis proccess can not be undone.")

    confirmation = input("Continue? (y/n): ").strip().lower()

    if confirmation in ["y", "yes"]:
        clean_space_before_prefix()
    else:
        print("Cancelled!")


if __name__ == "__main__":
    main()
