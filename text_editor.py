import os
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter

class TextEditor:
    def __init__(self):
        self.file_name = None
        self.text = ""

    def create_new_file(self):
        self.file_name = input("Enter a file name: ")
        self.text = ""

    def open_file(self):
        self.file_name = input("Enter a file name: ")
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                self.text = file.read()
        else:
            print("File not found.")

    def edit_text(self):
        print("Current text:")
        lexer = get_lexer_by_name("python")  # assume Python syntax for now
        formatter = TerminalFormatter()
        highlighted_text = highlight(self.text, lexer, formatter)
        print(highlighted_text)
        self.text = input("Enter new text: ")

    def save_changes(self):
        if self.file_name:
            with open(self.file_name, "w") as file:
                file.write(self.text)
            print("Changes saved.")
        else:
            print("No file open.")

    def run(self):
        while True:
            print("\nText Editor Menu:")
            print("1. Create new file")
            print("2. Open file")
            print("3. Edit text")
            print("4. Save changes")
            print("5. Quit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_new_file()
            elif choice == "2":
                self.open_file()
            elif choice == "3":
                self.edit_text()
            elif choice == "4":
                self.save_changes()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    editor = TextEditor()
    editor.run()