import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
from config import CATEGORIES


def get_files_from_directory(directory_path):
    all_items = os.listdir(directory_path)
    return [
        item for item in all_items
        if os.path.isfile(os.path.join(directory_path, item))
    ]


def get_existing_category_folders(base_path):
    all_items = os.listdir(base_path)
    return [
        item for item in all_items
        if os.path.isdir(os.path.join(base_path, item))
           and item in CATEGORIES.keys()
    ]


def create_bordered_button(parent, text, command, **kwargs):
    border_frame = tk.Frame(parent, bg="gray", bd=1)
    button = tk.Button(
        border_frame,
        text=text,
        command=command,
        bg="black",
        fg="white",
        bd=0,
        relief="flat",
        activebackground="black",
        activeforeground="white",
        font=("Arial", 10, "bold"),
        **kwargs
    )
    button.pack(padx=2, pady=2)
    return border_frame


class FileOrganizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FILE ORGANIZER")
        self.root.geometry("600x500")
        self.root.minsize(600, 500)
        self.root.configure(bg="black")

        self.target_path = tk.StringVar(value=os.getcwd())
        self.sort_by_date = tk.BooleanVar(value=True)
        self.is_organizing = False

        self.setup_ui()

    def setup_ui(self):
        self.create_path_selector()
        self.create_options_panel()
        self.create_progress_display()
        self.create_action_buttons()

    def create_path_selector(self):
        path_frame = tk.Frame(self.root, bg="black")
        path_frame.pack(pady=(10, 0), fill="x")

        folder_label = tk.Label(
            path_frame,
            text="Folder to Organize:",
            bg="black",
            fg="white",
            font=("Arial", 10)
        )
        folder_label.pack(anchor="w", padx=20, pady=(10, 0))

        entry_frame = tk.Frame(path_frame, bg="black")
        entry_frame.pack(fill="x", pady=(0, 5), padx=(20, 10))

        self.path_entry = tk.Entry(
            entry_frame,
            textvariable=self.target_path,
            width=50,
            font=("Arial", 10, "normal"),
            bg="black",
            fg="white",
            bd=2,
            relief="solid",
            highlightbackground="gray",
            highlightcolor="gray",
            highlightthickness=3,
            insertbackground="white"
        )
        self.path_entry.pack(side="left", fill="x", expand=True, padx=(0, 5), pady=2)

        browse_button = create_bordered_button(
            entry_frame,
            text="Browse",
            command=self.browse_folder,
            width=10,
            height=1
        )
        browse_button.pack(padx=(5, 10), pady=2)

    def create_options_panel(self):
        options_frame = tk.LabelFrame(
            self.root,
            text="Options",
            bg='black',
            fg='white',
            bd=2,
            relief='solid',
            highlightbackground='gray',
            highlightthickness=3
        )
        options_frame.pack(pady=(10, 0), padx=20, fill="x")

        date_sort_checkbox = tk.Checkbutton(
            options_frame,
            text="Sort files by date within folders",
            variable=self.sort_by_date,
            bg='black',
            fg='white',
            selectcolor='black',
            activebackground='black',
            activeforeground='white',
            highlightbackground='gray',
            highlightthickness=2
        )
        date_sort_checkbox.pack(anchor="w", padx=10, pady=8)

    def create_progress_display(self):
        self.progress_frame = tk.LabelFrame(
            self.root,
            text="Progress",
            bg="black",
            fg="white",
            bd=2,
            relief="solid",
            highlightbackground="gray",
            highlightthickness=3,
            padx=10,
            pady=10
        )
        self.progress_frame.pack(pady=(10, 0), padx=20, fill="both", expand=True)

        self.progress_label = tk.Label(
            self.progress_frame,
            text="Ready to organize...",
            bg="black",
            fg="white",
            font=("Arial", 10)
        )
        self.progress_label.pack(anchor="w")

        self.progress_text = tk.Text(
            self.progress_frame,
            height=10,
            width=50,
            state="disabled",
            bg="black",
            fg="white",
            insertbackground="white",
            selectbackground="#333333",
            selectforeground="white",
            relief="solid",
            bd=2,
            highlightbackground="gray",
            highlightthickness=3,
            font=("Consolas", 10)
        )
        self.progress_text.pack(fill="both", expand=True, pady=(5, 0))

        self.progress_text.tag_configure("success", foreground="#4CAF50")
        self.progress_text.tag_configure("error", foreground="#F44336")
        self.progress_text.tag_configure("warning", foreground="#FF9800")
        self.progress_text.tag_configure("info", foreground="#2196F3")
        self.progress_text.tag_configure("header", foreground="white", font=("Consolas", 10, "bold"))
        self.progress_text.tag_configure("step", foreground="#FFD700")

    def create_action_buttons(self):
        button_frame = tk.Frame(self.root, bg="black")
        button_frame.pack(pady=20)

        start_button = create_bordered_button(
            button_frame,
            text="Start Organization",
            command=self.start_organization,
            width=20
        )
        start_button.pack(side="left", padx=5)

        clear_button = create_bordered_button(
            button_frame,
            text="Clear Log",
            command=self.clear_log,
            width=10
        )
        clear_button.pack(side="left", padx=5)

        exit_button = create_bordered_button(
            button_frame,
            text="Exit",
            command=self.root.quit,
            width=10
        )
        exit_button.pack(side="left", padx=5)

    def browse_folder(self):
        selected_folder = filedialog.askdirectory(title="Select Folder to Organize")
        if selected_folder:
            self.target_path.set(selected_folder)

    def log_message(self, message, tag=None):
        self.progress_text.config(state="normal")
        if tag:
            self.progress_text.insert("end", message + "\n", tag)
        else:
            self.progress_text.insert("end", message + "\n")
        self.progress_text.see("end")
        self.progress_text.config(state="disabled")
        self.root.update()

    def clear_log(self):
        self.progress_text.config(state="normal")
        self.progress_text.delete(1.0, "end")
        self.progress_text.config(state="disabled")
        self.progress_label.config(text="Ready to organize...")

    def start_organization(self):
        if self.is_organizing:
            return

        target_path = self.target_path.get()
        if not self.validate_path(target_path):
            return

        self.is_organizing = True
        self.clear_log()
        self.root.after(10, self.execute_organization, target_path)

    def validate_path(self, path):
        if not os.path.exists(path):
            messagebox.showerror("Error", f"Path does not exist:\n{path}")
            self.is_organizing = False
            return False
        return True

    def execute_organization(self, target_path):
        try:
            self.progress_label.config(text="Organizing...")
            self.log_header(target_path)

            sort_by_date = self.sort_by_date.get()
            used_categories = self.organize_by_category(target_path)

            if sort_by_date:
                self.organize_by_date(target_path)

            self.log_success()

        except Exception as error:
            self.log_error(error)

        finally:
            self.is_organizing = False

    def log_header(self, target_path):
        self.log_message("=" * 50, "header")
        self.log_message(f"ORGANIZING: {target_path}", "header")
        self.log_message("=" * 50, "header")

    def log_success(self):
        self.log_message("\n" + "=" * 50, "success")
        self.log_message("ORGANIZATION COMPLETE! 🎉", "success")
        self.log_message("=" * 50, "success")

        self.progress_label.config(text="Organization Complete!")
        messagebox.showinfo("Success", "File organization completed successfully!")

    def log_error(self, error):
        self.log_message(f"\nERROR: {str(error)}", "error")
        self.progress_label.config(text="Error occurred")
        messagebox.showerror("Error", f"An error occurred:\n{str(error)}")

    def organize_by_category(self, target_path):
        self.log_message("\nSTEP 1: Organizing files by category...", "step")

        all_files = get_files_from_directory(target_path)
        self.log_message(f"Found {len(all_files)} files in main folder", "info")

        used_categories = set()

        for file_name in all_files:
            file_was_categorized = self.categorize_and_move_file(
                target_path, file_name, used_categories
            )

            if not file_was_categorized:
                self.log_message(f"  Skipped: {file_name}", "warning")

        self.log_message(f"\n✅ STEP 1 COMPLETE", "success")
        return used_categories

    def categorize_and_move_file(self, base_path, file_name, used_categories):
        file_path = os.path.join(base_path, file_name)
        file_extension = os.path.splitext(file_name)[1].lower()

        for category_name, allowed_extensions in CATEGORIES.items():
            if file_extension in allowed_extensions:
                self.move_to_category(base_path, file_path, file_name, category_name)
                used_categories.add(category_name)
                return True
        return False

    def move_to_category(self, base_path, file_path, file_name, category_name):
        category_folder = os.path.join(base_path, category_name)
        os.makedirs(category_folder, exist_ok=True)

        destination = os.path.join(category_folder, file_name)
        shutil.move(file_path, destination)

        self.log_message(f"  Moved: {file_name} -> {category_name}/", "info")

    def organize_by_date(self, target_path):
        self.log_message("\n" + "=" * 50, "header")
        self.log_message("STEP 2: Sorting files by date...", "step")
        self.log_message("=" * 50, "header")

        category_folders = get_existing_category_folders(target_path)

        if not category_folders:
            self.log_message("No category folders found to sort by date", "warning")
            return

        self.log_message(f"Found {len(category_folders)} category folders:", "info")
        self.log_message(f"  {', '.join(category_folders)}", "info")

        total_files_sorted = 0
        for category_name in category_folders:
            files_sorted = self.sort_category_by_date(target_path, category_name)
            total_files_sorted += files_sorted

        if total_files_sorted > 0:
            self.log_message(f"\n✅ STEP 2 COMPLETE: Sorted {total_files_sorted} files", "success")
        else:
            self.log_message("\nℹ️  All files were already sorted by date", "info")

    def sort_category_by_date(self, base_path, category_name):
        category_path = os.path.join(base_path, category_name)
        files_in_category = get_files_from_directory(category_path)

        if not files_in_category:
            self.log_message(f"\n{category_name}/: No files found", "warning")
            return 0

        self.log_message(f"\nProcessing {category_name}/ ({len(files_in_category)} files):", "info")

        files_sorted = 0
        for file_name in files_in_category:
            if self.sort_file_by_date(category_path, file_name):
                files_sorted += 1

        if files_sorted > 0:
            self.log_message(f"✅ {category_name}/: Sorted {files_sorted} files", "success")
        else:
            self.log_message(f"ℹ️  {category_name}/: All files already sorted", "info")

        return files_sorted

    def sort_file_by_date(self, category_path, file_name):
        file_path = os.path.join(category_path, file_name)
        timestamp = os.path.getmtime(file_path)
        file_date = datetime.fromtimestamp(timestamp)
        date_folder_name = file_date.strftime("%Y-%m_%B")

        date_folder_path = os.path.join(category_path, date_folder_name)
        os.makedirs(date_folder_path, exist_ok=True)

        destination_path = os.path.join(date_folder_path, file_name)

        if file_path != destination_path:
            shutil.move(file_path, destination_path)
            self.log_message(f"  Sorted: {file_name} -> {date_folder_name}/", "info")
            return True
        return False


def main():
    root = tk.Tk()
    FileOrganizerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()