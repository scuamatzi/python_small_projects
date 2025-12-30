import datetime
import subprocess


def run_tree_command(level, filename, path):
    """Execute tree command with specified level and save to file."""

    try:
        # Check if tree command exists
        result = subprocess.run(["tree", "--version"], capture_output=True, text=True)

        # Run tree command with specified level
        cmd = ["tree", "-L", str(level), f"{path}"]
        tree_result = subprocess.run(cmd, capture_output=True, text=True)

        if tree_result.returncode == 0:
            with open(filename, "w") as f:
                f.write(tree_result.stdout)
            print(f"Tree output saved to: {filename}")
            return True
        else:
            print(f"Error running tree command: {tree_result.stderr}")
            return False
    except FileNotFoundError:
        print("  ✗ 'tree' command not found. Please install it first.")
        print("     On Ubuntu/Debian: sudo apt install tree")
        print("     On Fedora/RHEL: sudo dnf install tree")
        print("     On Arch: sudo pacman -S tree")
        return False
    except Exception as e:
        print(f"Error runing tree command: {e}")
        return False


#    try:
#        # Check if tree command exists
#        result = subprocess.run(["tree", "--version"], capture_output=True, text=True)
#
#        # Run tree command with specified level
#        cmd = ["tree", "-L", str(level), f"{path}"]
#        tree_result = subprocess.run(cmd, capture_output=True, text=True)
#
#        if tree_result.returncode == 0:
#            with open(filename, "w") as f:
#                f.write(tree_result.stdout)
#            print(f"  ✓ Tree output saved to: {filename}")
#            return True
#        else:
#            print(f"  ✗ Error running tree command: {tree_result.stderr}")
#            return False
#
#    except FileNotFoundError:
#        print("  ✗ 'tree' command not found. Please install it first.")
#        print("     On Ubuntu/Debian: sudo apt install tree")
#        print("     On Fedora/RHEL: sudo dnf install tree")
#        print("     On Arch: sudo pacman -S tree")
#        return False
#    except Exception as e:
#        print(f"  ✗ Error running tree command: {e}")
#        return False


def main():
    """Executes tree command for levels 1, 2 and 3 and save them in txt files."""
    print("\n" + "=" * 60)
    print("DIRECTORY TREE INFORMATION")
    print("=" * 60)

    filename_prefix = input("Filename for tree results: ").strip().lower()

    if not filename_prefix:
        print("I will use 'tree_output' as filename...\n")
        filename_prefix = "tree_output"

    path = input("Enter path to analyze: ")
    if not path:
        print("Path can not be empty.")
        return

    current_date = datetime.datetime.now().strftime("%Y%m%d")

    # Generate tree filenams
    tree_files = {
        1: f"{filename_prefix}-L1-{current_date}.txt",
        2: f"{filename_prefix}-L2-{current_date}.txt",
        3: f"{filename_prefix}-L3-{current_date}.txt",
    }

    # Generate tree outputs
    print("\nGenerating tree structure outputs...")
    for level, filename in tree_files.items():
        print(f"Level {level}:")
        run_tree_command(level, filename, path)


if __name__ == "__main__":
    main()
