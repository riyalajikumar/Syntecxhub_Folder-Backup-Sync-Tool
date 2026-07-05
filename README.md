## Folder Backup & Synchronization Tool

A professional Python application developed to automate folder backup and synchronization. The tool securely copies files and folders from a source directory to a destination directory while maintaining folder structure, creating logs, and preventing data loss.

---

##  Project Overview

The Folder Backup & Synchronization Tool is designed to simplify the process of backing up important files. It automatically copies folders from a selected source location to a backup location and maintains synchronization between them.

The project is useful for students, professionals, offices, and anyone who wants to keep important files safe by creating regular backups.

---

## Features

-  Automatic Folder Backup
- Folder Synchronization
-  Backup Log Generation
-  Date & Time Stamping
-  Automatic Folder Creation
-  Error Handling
-  Console Status Messages
-  User-Friendly Command Line Interface
-  Secure File Copying
-  Easy to Maintain and Extend

---

##  Technologies Used

- Python 3.x
- OS Module
- shutil Module
- datetime Module
- logging Module
- hashlib Module
- filecmp Module

---

##  Project Structure

```
Folder Backup & Synchronization Tool
│
├── folder_backup.py
├── Folder Backup.pdf
├── README.md
├── LICENSE

```

---

## Hardware Requirements

- Processor : Intel Core i3 or above
- RAM : 4 GB or above
- Hard Disk : 500 MB Free Space
- Operating System : Windows 10 / Windows 11

---

## Software Requirements

- Python 3.10 or later
- Visual Studio Code
- Git
- GitHub
- Windows Command Prompt / PowerShell

---

##  Installation

1. Clone the repository

```
git clone https://github.com/riyalajikumar/Syntecxhub_Folder-Backup-Sync-Tool.git
```

2. Open the project folder.

3. Run the Python program.

```
python folder_backup.py
```

---

##  Usage

1. Execute the program.
2. Enter the source folder path.
3. Enter the destination folder path.
4. The program copies all files and folders.
5. Backup completion status is displayed.
6. A log file is generated for future reference.

---

##  Sample Output

```
========================================================
        FOLDER BACKUP & SYNCHRONIZATION TOOL
========================================================

Enter Source Folder Path :
C:\Users\Riya\Documents\SourceFolder

Enter Destination Folder Path :
D:\Backup

Creating Backup...

Copying Files...

Backup Completed Successfully!

Backup Location :
D:\Backup\Backup_2026-07-05_18-25-40

Total Files Copied : 3

Total Folders Copied : 1

Log File Created Successfully.

Thank You for Using Folder Backup Tool.
========================================================
```

---

##  Testing

The application was tested using different source folders containing documents, images, PDF files, and nested folders. All files were copied successfully without data corruption. Invalid folder paths were also tested, and appropriate error messages were displayed.

---

## Advantages

- Fast and reliable backup
- Prevents accidental data loss
- Easy to use
- Lightweight application
- Portable
- No external database required
- Automatic folder creation
- Generates backup logs

---

## Limitations

- Command-line interface only
- Manual folder selection
- Local storage only
- No cloud synchronization
- No graphical user interface

---

##  Future Enhancements

- Graphical User Interface (GUI)
- Cloud Backup Support
- Automatic Scheduled Backup
- Email Notifications
- Incremental Backup
- Password Protection
- Backup Compression
- Restore Functionality

---

##  Author

**Riya Lajikumar**

B.Tech Computer Science Engineering

Python Internship Project

2026

---

## License

This project is licensed under the **MIT License**.

---

##  Acknowledgement

This project was developed as part of a Python Internship to understand file handling, folder synchronization, backup automation, logging, and software development using Python.
