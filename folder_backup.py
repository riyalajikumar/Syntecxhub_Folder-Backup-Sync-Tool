import os
import shutil
import logging
import filecmp

from pathlib import Path
from datetime import datetime



logging.basicConfig(
    filename="backup_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


FILES_COPIED = 0
FILES_UPDATED = 0
FILES_SKIPPED = 0



def display_header():
    print("=" * 60)
    print("     FOLDER BACKUP & SYNCHRONIZATION TOOL")
    print("=" * 60)



def get_folder_path(message):

    while True:

        path = input(message).strip('"')

        if os.path.exists(path):
            return path

        print("\nFolder not found.")
        print("Please enter a valid folder.\n")



def create_backup_folder(destination):

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    backup_folder = os.path.join(
        destination,
        "Backup_" + timestamp
    )

    os.makedirs(backup_folder, exist_ok=True)

    return backup_folder



def get_folder_size(folder):

    total = 0

    for root, dirs, files in os.walk(folder):

        for file in files:

            file_path = os.path.join(root, file)

            if os.path.exists(file_path):
                total += os.path.getsize(file_path)

    return total




def convert_size(size):

    for unit in ['Bytes', 'KB', 'MB', 'GB', 'TB']:

        if size < 1024:
            return f"{size:.2f} {unit}"

        size /= 1024

    return f"{size:.2f} PB"



def copy_file(source_file, destination_file):

    global FILES_COPIED

    os.makedirs(
        os.path.dirname(destination_file),
        exist_ok=True
    )

    shutil.copy2(source_file, destination_file)

    FILES_COPIED += 1

    logging.info(f"Copied : {source_file}")


def update_file(source_file, destination_file):

    global FILES_UPDATED

    shutil.copy2(source_file, destination_file)

    FILES_UPDATED += 1

    logging.info(f"Updated : {source_file}")


def skip_file():

    global FILES_SKIPPED

    FILES_SKIPPED += 1


def print_statistics(folder):

    print("\n")
    print("=" * 60)
    print("BACKUP SUMMARY")
    print("=" * 60)

    print(f"Files Copied     : {FILES_COPIED}")
    print(f"Files Updated    : {FILES_UPDATED}")
    print(f"Files Skipped    : {FILES_SKIPPED}")

    size = convert_size(get_folder_size(folder))

    print(f"Backup Size      : {size}")

    print("=" * 60)


def backup_folder(source, destination):

    print("\nCreating Backup...\n")

    logging.info("Backup Started")

    for root, dirs, files in os.walk(source):

        relative = os.path.relpath(root, source)

        destination_root = os.path.join(
            destination,
            relative
        )

        os.makedirs(destination_root, exist_ok=True)

        for file in files:

            source_file = os.path.join(root, file)

            destination_file = os.path.join(
                destination_root,
                file
            )

            copy_file(source_file, destination_file)

    logging.info("Backup Completed")

    print("\nBackup Completed Successfully.\n")

  

def synchronize_folder(source, destination):

    print("\nSynchronizing Files...\n")

    logging.info("Synchronization Started")

    for root, dirs, files in os.walk(source):

        relative = os.path.relpath(root, source)

        destination_root = os.path.join(destination, relative)

        os.makedirs(destination_root, exist_ok=True)

        for file in files:

            source_file = os.path.join(root, file)
            destination_file = os.path.join(destination_root, file)

            # File does not exist in destination
            if not os.path.exists(destination_file):
                copy_file(source_file, destination_file)
                continue

            try:
                # Compare files
                if not filecmp.cmp(source_file, destination_file, shallow=False):
                    update_file(source_file, destination_file)
                else:
                    skip_file()

            except Exception:
                update_file(source_file, destination_file)

    logging.info("Synchronization Completed")

    print("\nSynchronization Completed Successfully.\n")



def display_backup_information(source, backup):

    print("=" * 60)
    print("BACKUP INFORMATION")
    print("=" * 60)

    print(f"Source Folder      : {source}")
    print(f"Backup Folder      : {backup}")

    size = convert_size(get_folder_size(source))

    print(f"Source Size        : {size}")

    print("=" * 60)


def verify_backup(source, destination):

    print("\nVerifying Backup...\n")

    mismatch = False

    comparison = filecmp.dircmp(source, destination)

    if comparison.left_only:
        mismatch = True

    if comparison.diff_files:
        mismatch = True

    if comparison.right_only:
        mismatch = True

    if mismatch:
        print("Verification : WARNING")
        print("Some files may not be synchronized correctly.\n")
        logging.warning("Verification completed with differences.")
    else:
        print("Verification : SUCCESS")
        print("Backup verified successfully.\n")
        logging.info("Backup verified successfully.")


def completion_message():

    print("=" * 60)
    print("BACKUP PROCESS COMPLETED SUCCESSFULLY")
    print("=" * 60)

    print("\nLog File Created : backup_log.txt")

    print("\nThank you for using")
    print("Folder Backup & Synchronization Tool")

    print("=" * 60)


def execute_backup(source, destination):

    try:

        backup_folder(source, destination)

        synchronize_folder(source, destination)

        verify_backup(source, destination)

        print_statistics(destination)

        completion_message()

    except PermissionError:

        print("\nPermission Denied.")
        logging.error("Permission Denied")

    except FileNotFoundError:

        print("\nFolder Not Found.")
        logging.error("Folder Not Found")

    except Exception as error:

        print("\nUnexpected Error:")
        print(error)

        logging.exception(error)


def main():

    display_header()

    print("\nEnter the required folder paths.\n")

    source_folder = get_folder_path(
        "Enter Source Folder Path : "
    )

    destination_parent = input(
        "Enter Destination Folder Path : "
    ).strip('"')

    if destination_parent == "":
        print("\nDestination folder cannot be empty.")
        return

    os.makedirs(destination_parent, exist_ok=True)

    backup_folder_path = create_backup_folder(destination_parent)


    display_backup_information(
        source_folder,
        backup_folder_path
    )

    print("\nStarting Backup...\n")

    execute_backup(
        source_folder,
        backup_folder_path
    )

    print("\nProgram Finished Successfully.")



if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print("\n\nProgram Cancelled by User.")

        logging.warning("Program Cancelled")

    except Exception as error:

        print("\nUnexpected Error:")
        print(error)

        logging.exception(error)