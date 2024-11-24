# QuickBookmark

QuickBookmark is a Python-based command-line tool designed to help you manage and access your bookmarks effortlessly. Whether you're bookmarking URLs, file paths, or scripts, QuickBookmark provides a simple and efficient way to keep your important resources organized and easily accessible.

## Table of Contents
- [Why QuickBookmark?](#why-quickbookmark)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Example Use Case](#example-use-case)
- [Contributing](#contributing)
- [License](#license)

## Why QuickBookmark?

Managing bookmarks manually can become cumbersome, especially when dealing with multiple types of resources like websites, documents, and scripts. QuickBookmark simplifies this process by providing a unified interface to add, remove, list, and load your bookmarks directly from the terminal.

## Features

- **Add Bookmarks:** Easily add new bookmarks with a unique identifier.
- **Remove Bookmarks:** Remove bookmarks that are no longer needed.
- **List Bookmarks:** View all your saved bookmarks in an organized manner.
- **Load Bookmarks:** Quickly access your bookmarks, whether they are URLs, file paths, or scripts.
- **Persistent Storage:** Bookmarks are saved in a JSON file for persistent storage across sessions.

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/QuickBookmark.git
    ```

2. **Navigate to the Directory:**
    ```bash
    cd QuickBookmark
    ```

3. **Install Required Packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script using Python:







bash
python bookmarks.py

Follow the on-screen menu to add, remove, list, or load bookmarks.

### Menu Options

1. **Add a Bookmark:** Add a new bookmark by providing a unique number and the bookmark value (URL, file path, or script path).
2. **Remove a Bookmark:** Remove an existing bookmark by entering its number.
3. **List Bookmarks:** Display all saved bookmarks.
4. **Load a Bookmark:** Access a bookmark by its number. Depending on the type, it will open in your default browser, execute a script, or open a file.
5. **Exit:** Exit the QuickBookmark application.

## Requirements

Ensure you have Python installed. Install the required packages using the following commands:


