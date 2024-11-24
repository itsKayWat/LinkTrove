import json
import os
import subprocess
import sys

# Define the path to the bookmarks file
BOOKMARKS_FILE = 'bookmarks.json'

def load_bookmarks():
    """Load bookmarks from the JSON file."""
    if not os.path.isfile(BOOKMARKS_FILE):
        return {}
    with open(BOOKMARKS_FILE, 'r') as file:
        try:
            bookmarks = json.load(file)
            # Convert keys back to integers
            bookmarks = {int(k): v for k, v in bookmarks.items()}
            return bookmarks
        except json.JSONDecodeError:
            return {}

def save_bookmarks(bookmarks):
    """Save bookmarks to the JSON file."""
    with open(BOOKMARKS_FILE, 'w') as file:
        # Convert keys to strings for JSON compatibility
        bookmarks_str_keys = {str(k): v for k, v in bookmarks.items()}
        json.dump(bookmarks_str_keys, file, indent=4)

def add_bookmark(bookmarks):
    """Add a new bookmark."""
    try:
        bookmark_id = int(input("Enter a number for the bookmark (e.g., 1): "))
        if bookmark_id in bookmarks:
            print(f"Bookmark number {bookmark_id} already exists.")
            return
        bookmark_value = input("Enter the bookmark value (URL, file path, script path, etc.): ")
        bookmarks[bookmark_id] = bookmark_value
        save_bookmarks(bookmarks)
        print(f"Bookmark {bookmark_id} added successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def remove_bookmark(bookmarks):
    """Remove an existing bookmark."""
    try:
        bookmark_id = int(input("Enter the number of the bookmark to remove: "))
        if bookmark_id in bookmarks:
            del bookmarks[bookmark_id]
            save_bookmarks(bookmarks)
            print(f"Bookmark {bookmark_id} removed successfully.")
        else:
            print(f"No bookmark found with number {bookmark_id}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def list_bookmarks(bookmarks):
    """List all bookmarks."""
    if not bookmarks:
        print("No bookmarks saved.")
        return
    print("\nSaved Bookmarks:")
    print("----------------")
    for k in sorted(bookmarks.keys()):
        print(f"{k}: {bookmarks[k]}")
    print("----------------\n")

def load_bookmark(bookmarks):
    """Load a bookmark by its number."""
    try:
        bookmark_id = int(input("Enter the number of the bookmark to load: "))
        if bookmark_id not in bookmarks:
            print(f"No bookmark found with number {bookmark_id}.")
            return
        bookmark = bookmarks[bookmark_id]
        print(f"Loading bookmark {bookmark_id}: {bookmark}")
        
        # Determine the action based on the bookmark's content
        if bookmark.startswith("http://") or bookmark.startswith("https://"):
            # Open URL in the default browser
            import webbrowser
            webbrowser.open(bookmark)
            print(f"Opened URL: {bookmark}")
        elif bookmark.endswith(".py"):
            # Run a Python script
            if os.path.isfile(bookmark):
                subprocess.run([sys.executable, bookmark])
            else:
                print(f"Script file '{bookmark}' does not exist.")
        else:
            # Assume it's a file path; attempt to open it with the default application
            if os.path.isfile(bookmark):
                if sys.platform.startswith('darwin'):
                    subprocess.call(('open', bookmark))
                elif os.name == 'nt':
                    os.startfile(bookmark)
                elif os.name == 'posix':
                    subprocess.call(('xdg-open', bookmark))
                print(f"Opened file: {bookmark}")
            else:
                print(f"File or resource '{bookmark}' does not exist.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def display_menu():
    """Display the main menu."""
    print("\n📑 Python Bookmark System")
    print("------------------------")
    print("1. Add a Bookmark")
    print("2. Remove a Bookmark")
    print("3. List Bookmarks")
    print("4. Load a Bookmark")
    print("5. Exit")
    print("------------------------")

def main():
    """Main function to run the bookmark system."""
    bookmarks = load_bookmarks()
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            add_bookmark(bookmarks)
        elif choice == '2':
            remove_bookmark(bookmarks)
        elif choice == '3':
            list_bookmarks(bookmarks)
        elif choice == '4':
            load_bookmark(bookmarks)
        elif choice == '5':
            print("Exiting the bookmark system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
