import os
from datetime import datetime

fecha_actual = datetime.now()
fecha_formateada = fecha_actual.strftime("%Y%m%d")


def rename_files(directory="archivos", old_text="Nuevo", new_text=fecha_formateada):
    """
    Rename multiple files in a directory old_text -> new_text
    """
    for filename in os.listdir(directory):
        if old_text in filename:
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, filename.replace(old_text, new_text))
            os.rename(old_file, new_file)
            print(
                f"File renamed: {filename} -> {filename.replace(old_text, new_text)} "
            )


if __name__ == "__main__":
    rename_files(old_text="Nuevo", new_text="test")
