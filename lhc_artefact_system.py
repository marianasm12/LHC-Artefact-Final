"""LHC Artefact Management System - ACCA5036 coursework prototype.

Records are stored in memory while the program runs.
"""

# Sample records so the collection is not empty when the program starts.
# Functions change this list without reassigning it.
artefacts = [
    {
        "name": "Capoeira Berimbau",
        "category": "Musical Instrument",
        "location": "Room M1",
        "condition": "Good",
        "notes": "",
    },
    {
        "name": "Brazilian Clay Pot",
        "category": "Household Object",
        "location": "Storage Room A",
        "condition": "Good",
        "notes": "",
    },
    {
        "name": "African Djembe Drum",
        "category": "Musical Instrument",
        "location": "Room M1",
        "condition": "Damaged",
        "notes": "Torn drum skin; needs replacing before display.",
    },
    {
        "name": "Victorian Pocket Watch",
        "category": "Historical Object",
        "location": "Display Cabinet A",
        "condition": "Good",
        "notes": "",
    },
    {
        "name": "Traditional Wooden Mask",
        "category": "Cultural Object",
        "location": "Display Cabinet B",
        "condition": "Under Repair",
        "notes": "Crack on the left side; sent for restoration.",
    },
    {
        "name": "Antique Brass Compass",
        "category": "Historical Object",
        "location": "Storage Room B",
        "condition": "Good",
        "notes": "",
    },
    {
        "name": "Japanese Folding Fan",
        "category": "Cultural Object",
        "location": "Display Cabinet C",
        "condition": "Good",
        "notes": "",
    },
    {
        "name": "Handmade Ceramic Vase",
        
        "category": "Household Object",
        "location": "Storage Room A",
        "condition": "Damaged",
        "notes": "Small chip on the rim; handle with care.",
    },
    {
        "name": "Traditional Woven Basket",
        "category": "Cultural Object",
        "location": "Display Cabinet B",
        "condition": "Good",
        "notes": "",
    },
    {
        "name": "Vintage Typewriter",
        "category": "Historical Object",
        "location": "Storage Room B",
        "condition": "Under Repair",
        "notes": "",
    },
]


def view_all_artefacts():
    """Display every artefact, or a message if the collection is empty."""
    print("\n--- All Artefacts ---")
    if not artefacts:
        print("No artefacts recorded.")
    else:
        for artefact in artefacts:
            print("Name:", artefact["name"])
            print("Category:", artefact["category"])
            print("Location:", artefact["location"])
            print("Condition:", artefact["condition"])
            print("Notes:", artefact["notes"])
            print("------------------------")


def add_new_artefact():
    """Validate details and add one new artefact to the collection."""
    print("\n--- Add New Artefact ---")
    name = input("Enter artefact name: ").strip()
    if not name:
        print("Artefact name cannot be empty.")
    else:
        # Compare names without case differences to prevent duplicate records.
        duplicate_found = False
        for item in artefacts:
            if item["name"].lower() == name.lower():
                duplicate_found = True
                break
        if duplicate_found:
            print("Artefact already exists.")
        else:
            category = input("Enter category: ").strip()
            if not category:
                print("Category cannot be empty.")
            else:
                location = input("Enter location: ").strip()
                if not location:
                    print("Location cannot be empty.")
                else:
                    print("1. Good")
                    print("2. Damaged")
                    print("3. Under Repair")
                    condition_choice = input("Select condition (1-3): ").strip()
                    if condition_choice == "1":
                        condition = "Good"
                    elif condition_choice == "2":
                        condition = "Damaged"
                    elif condition_choice == "3":
                        condition = "Under Repair"
                    else:
                        print("Invalid condition.")
                    if condition_choice in ("1", "2", "3"):
                        artefact = {
                            "name": name,
                            "category": category,
                            "location": location,
                            "condition": condition,
                            "notes": "",
                        }
                        artefacts.append(artefact)
                        print("Artefact added successfully.")


def search_artefact_by_name():
    """Find an artefact by its full name, ignoring letter case."""
    print("\n--- Search Artefact ---")
    # Match the full name while ignoring spaces at the ends and letter case.
    search_name = input("Enter artefact name: ").strip().lower()
    if not search_name:
        print("Artefact name cannot be empty.")
    else:
        found = False
        for artefact in artefacts:
            if artefact["name"].lower() == search_name:
                print("Name:", artefact["name"])
                print("Category:", artefact["category"])
                print("Location:", artefact["location"])
                print("Condition:", artefact["condition"])
                print("Notes:", artefact["notes"])
                found = True
                break
        if not found:
            print("Artefact not found.")


def update_artefact_condition():
    """Change the condition of an existing artefact."""
    print("\n--- Update Artefact Condition ---")
    search_name = input("Enter artefact name: ").strip().lower()
    if not search_name:
        print("Artefact name cannot be empty.")
    else:
        found = False
        for artefact in artefacts:
            if artefact["name"].lower() == search_name:
                found = True
                print("Current condition:", artefact["condition"])
                print("1. Good")
                print("2. Damaged")
                print("3. Under Repair")
                condition_choice = input("Select new condition (1-3): ").strip()
                if condition_choice == "1":
                    artefact["condition"] = "Good"
                elif condition_choice == "2":
                    artefact["condition"] = "Damaged"
                elif condition_choice == "3":
                    artefact["condition"] = "Under Repair"
                else:
                    print("Invalid condition.")
                if condition_choice in ("1", "2", "3"):
                    print("Condition updated successfully.")
                break
        if not found:
            print("Artefact not found.")


def relocate_artefact():
    """Update the location of an existing artefact."""
    print("\n--- Relocate Artefact ---")
    search_name = input("Enter artefact name: ").strip().lower()
    if not search_name:
        print("Artefact name cannot be empty.")
    else:
        found = False
        for artefact in artefacts:
            if artefact["name"].lower() == search_name:
                found = True
                print("Current location:", artefact["location"])
                new_location = input("Enter new location: ").strip()
                if not new_location:
                    print("Location cannot be empty.")
                else:
                    artefact["location"] = new_location
                    print("Artefact relocated successfully.")
                break
        if not found:
            print("Artefact not found.")


def record_artefact_notes():
    """Add or replace notes for an existing artefact."""
    print("\n--- Record Artefact Notes ---")
    search_name = input("Enter artefact name: ").strip().lower()
    if not search_name:
        print("Artefact name cannot be empty.")
    else:
        found = False
        for artefact in artefacts:
            if artefact["name"].lower() == search_name:
                found = True
                print("Current notes:", artefact["notes"])
                new_notes = input("Enter new notes: ").strip()
                if not new_notes:
                    print("Notes cannot be empty.")
                else:
                    artefact["notes"] = new_notes
                    print("Artefact notes updated successfully.")
                break
        if not found:
            print("Artefact not found.")


def create_collection_summary():
    """Count artefacts by condition and category."""
    print("\n--- Collection Summary ---")
    if not artefacts:
        print("No artefacts recorded.")
    else:
        total = 0
        good_count = 0
        damaged_count = 0
        repair_count = 0
        # Category names are grouped without case differences.
        category_counts = {}
        for artefact in artefacts:
            total += 1
            if artefact["condition"] == "Good":
                good_count += 1
            elif artefact["condition"] == "Damaged":
                damaged_count += 1
            elif artefact["condition"] == "Under Repair":
                repair_count += 1
            category = artefact["category"].lower()
            if category in category_counts:
                category_counts[category] += 1
            else:
                category_counts[category] = 1
        print("Total artefacts:", total)
        print("Good:", good_count)
        print("Damaged:", damaged_count)
        print("Under Repair:", repair_count)
        print("--- Artefacts by Category ---")
        for category in category_counts:
            print(category, ": ", category_counts[category], sep="")


def remove_artefact():
    """Remove an artefact only after confirmation."""
    print("\n--- Remove Artefact ---")
    search_name = input("Enter artefact name: ").strip().lower()
    if not search_name:
        print("Artefact name cannot be empty.")
    else:
        found = False
        for artefact in artefacts:
            if artefact["name"].lower() == search_name:
                found = True
                print("Artefact found:", artefact["name"])
                print("Are you sure you want to remove this artefact? (Y/N)")
                confirmation = input("Confirmation: ").strip().upper()
                if confirmation == "Y":
                    # Removal changes the list; the search loop stops immediately afterwards.
                    artefacts.remove(artefact)
                    print("Artefact removed successfully.")
                elif confirmation == "N":
                    print("Removal cancelled.")
                else:
                    print("Invalid confirmation. Removal cancelled.")
                # The matching artefact has been handled; no further search is needed.
                break
        if not found:
            print("Artefact not found.")


def view_artefacts_requiring_attention():
    """Show artefacts that are damaged or under repair."""
    print("\n--- Artefacts Requiring Attention ---")
    found = False
    for artefact in artefacts:
        if artefact["condition"] == "Damaged" or artefact["condition"] == "Under Repair":
            print("Name:", artefact["name"])
            print("Category:", artefact["category"])
            print("Location:", artefact["location"])
            print("Condition:", artefact["condition"])
            print("Notes:", artefact["notes"])
            print("------------------------")
            found = True
    if not found:
        print("No artefacts require attention.")


def exit_system():
    """Display the exit message."""
    print("Exiting system. Goodbye!")


# Main program: one function for each menu option
while True:
    print("\n--- LHC Artefact Management System ---")
    print("1. View All Artefacts")
    print("2. Add New Artefact")
    print("3. Search Artefact by Name")
    print("4. Update Artefact Condition")
    print("5. Relocate Artefact")
    print("6. Record Artefact Notes")
    print("7. View Artefacts Requiring Attention")
    print("8. Create Collection Summary")
    print("9. Remove Artefact")
    print("10. Exit System")
    choice_text = input("Enter your choice (1-10): ").strip()
    # Validate before int() so text and decimal inputs do not cause ValueError.
    if not choice_text.isdecimal():
        print("Please enter a whole number.")
    else:
        choice = int(choice_text)
        if choice == 1:
            view_all_artefacts()
        elif choice == 2:
            add_new_artefact()
        elif choice == 3:
            search_artefact_by_name()
        elif choice == 4:
            update_artefact_condition()
        elif choice == 5:
            relocate_artefact()
        elif choice == 6:
            record_artefact_notes()
        elif choice == 7:
            view_artefacts_requiring_attention()
        elif choice == 8:
            create_collection_summary()
        elif choice == 9:
            remove_artefact()
        elif choice == 10:
            exit_system()
            break
        else:
            print("Invalid option. Please enter 1-10.")
        if 1 <= choice <= 9:
            input("Press Enter to return to menu.")
