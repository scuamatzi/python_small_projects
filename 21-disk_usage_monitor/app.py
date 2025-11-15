import shutil
from typing import Dict


def get_disk_usage(path: str = "/") -> Dict[str, str]:
    """
    Get disk usage statistics for the given path.

    Args:
        path (str): Directory path to check. Default root (/)

    Returns:
        dict: Total, used and free space in human-readable format.
    """
    print(path)

    total, used, free = shutil.disk_usage(path)

    def format_size(size: int) -> str:
        for unit in ["B", "KB", "MB", "GB", "TB"]:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024
        return f"{size:.2f} PB"

    return {
        "total": format_size(total),
        "used": format_size(used),
        "free": format_size(free),
    }


if __name__ == "__main__":
    stats = get_disk_usage(".")
    print("Disk usage: ", stats)
