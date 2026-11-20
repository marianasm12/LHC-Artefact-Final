# LHC Artefact Management System

A Python console application developed for the ACCA5036 Scripting and Programming Concepts assessment (WUTSD). The system allows volunteers to manage the LHC artefact collection through a menu containing ten options.

## Features

1. View All Artefacts
2. Add New Artefact
3. Search Artefact by Name
4. Update Artefact Condition
5. Relocate Artefact
6. Record Artefact Notes
7. View Artefacts Requiring Attention
8. Create Collection Summary
9. Remove Artefact
10. Exit System

## Data Storage

The program starts with ten sample artefact records. If an `artefacts.json` file exists, the system attempts to load the previously saved records.

Changes made during a session are stored in memory and saved to `artefacts.json` when the user selects option 10 (Exit System).

If the saved JSON data is invalid, the program displays a warning and continues using the sample records.

The JSON file is stored in the same folder as the Python script.

## Additional Functionality

- Case-insensitive artefact name searches.
- Validation of menu choices and required input fields.
- Prevention of duplicate artefact names.
- Confirmation before removing an artefact.
- Identification of artefacts marked as Damaged or Under Repair.
- Collection summaries showing totals by condition and category.
- Date and time displayed when a collection summary is generated.

## How to Run

**Requirements:**
- Python 3 (tested with Python 3.14).
- No external packages are required.

The program uses three Python standard library modules: `json`, `os` and `datetime`.

Download the Python file or clone the repository, then open a terminal in the folder containing the script.

Run:

```bash
python lhc_artefact_system.py
```

Follow the on-screen menu instructions to manage the artefact collection.

To save changes, select option 10 (Exit System). The program will create or update `artefacts.json` automatically.

## Limitations

The system is designed as a console-based coursework prototype.

Changes are saved when the user exits through option 10. If the program closes unexpectedly before saving, changes made during that session may be lost.

The system currently supports exact artefact name searches rather than partial-name searches.

## Author

Mariana Silva Martins

BSc Applied Computing  
ACCA5036 – Scripting and Programming Concepts
