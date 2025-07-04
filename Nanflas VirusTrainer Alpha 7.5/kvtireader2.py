import base64
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class KVTIEditor(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=BOTH, expand=YES)

        # UI elements
        self.file_path = tk.StringVar()
        self.entries = {}
        self.data = {}  # Store the data of the current file
        self.has_file = False

        # Set a minimum size for the window
        master.geometry("800x600")

        # Welcome message label
        self.welcome_label = ttk.Label(self, text="Welcome to KVTI Editor!", font=("Helvetica", 16))
        self.welcome_label.pack(anchor='center', pady=20)

        # Menu
        menubar = tk.Menu(master)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open .kvti", command=self.open_kvti)
        file_menu.add_command(label="Open .kvtie", command=self.open_kvtie)
        file_menu.add_command(label="Save .kvti", command=self.save_kvti)
        file_menu.add_command(label="Save .kvtie", command=self.save_kvtie)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        master.config(menu=menubar)

        # Add a button to add a new key-value pair (initially hidden)
        self.add_pair_button = ttk.Button(self, text="Add Key-Value Pair", command=self.add_new_pair)
        self.update_add_pair_button_visibility()

        # Add a button to insert image/document (initially hidden)
        self.insert_media_button = ttk.Button(self, text="Insert Image/Document", command=self.insert_media)
        self.update_insert_media_button_visibility()

        # Create a frame for the key-value pairs
        self.pair_frame = ttk.Frame(self)
        self.pair_frame.pack(fill=BOTH, expand=YES, padx=10, pady=10)

    def update_add_pair_button_visibility(self):
        """Show or hide the 'Add Key-Value Pair' button based on whether a file is open."""
        if self.has_file:
            self.add_pair_button.pack(anchor='w', padx=10, pady=(10, 0))
        else:
            self.add_pair_button.pack_forget()

    def update_insert_media_button_visibility(self):
        """Show or hide the 'Insert Image/Document' button based on whether a file is open."""
        if self.has_file:
            self.insert_media_button.pack(anchor='w', padx=10, pady=(10, 0))
        else:
            self.insert_media_button.pack_forget()

    def new_file(self):
        """Initialize a new empty KVTI file structure and show the 'Add Key-Value Pair' and 'Insert Media' buttons."""
        self.data.clear()
        self.update_list_items(self.data)
        self.has_file = True
        self.welcome_label.pack_forget()  # Hide welcome message
        self.update_add_pair_button_visibility()
        self.update_insert_media_button_visibility()

    def parse_kvti_content(self, content):
        data = {}
        lines = [line.strip() for line in content.splitlines() if line.strip()]
        for line in lines:
            if '=' in line:
                try:
                    key, value = line.split('=', 1)
                    value = value.strip('[]')  # Remove brackets from the value
                    if value.startswith('base64:'):
                        value = value[7:]  # Remove 'base64:' prefix
                    data[key.strip()] = value.strip() if value.strip() else ''
                except Exception as e:
                    messagebox.showerror("Parse Error", f"Error parsing line: {line}\n{str(e)}")
        return data

    def format_kvti_content(self, data):
        content = ''
        for key, value in data.items():
            if value.startswith('base64:'):
                value = f'base64:{value}'
            content += f'{key}=[{value}]\n'
        return content

    def update_list_items(self, data):
        for widget in self.pair_frame.winfo_children():
            widget.destroy()

        for key, value in data.items():
            entry_frame = ttk.Frame(self.pair_frame)
            entry_frame.pack(fill=X, pady=5)

            key_entry = ttk.Entry(entry_frame)
            key_entry.insert(0, key)
            key_entry.grid(row=0, column=0, padx=2, pady=2, sticky='ew')
            self.entries[f'{key}_key'] = key_entry

            value_entry = ttk.Entry(entry_frame)
            value_entry.insert(0, value)
            value_entry.grid(row=0, column=1, padx=2, pady=2, sticky='ew')
            self.entries[f'{key}_value'] = value_entry

            if value.startswith('base64:'):
                save_as_button = ttk.Button(entry_frame, text='Save As', command=lambda k=key: self.save_base64_to_file(k))
                save_as_button.grid(row=0, column=2, padx=2, pady=2)

            remove_button = ttk.Button(entry_frame, text='-', command=lambda k=key: self.remove_pair(k))
            remove_button.grid(row=0, column=3, padx=2, pady=2)

            # Bind changes to entries to update data dictionary
            key_entry.bind('<FocusOut>', lambda event, k=key: self.update_data_from_entries(k))
            value_entry.bind('<FocusOut>', lambda event, k=key: self.update_data_from_entries(k))

    def update_data_from_entries(self, key):
        """Update the data dictionary when entries are changed."""
        key_entry = self.entries.get(f'{key}_key')
        value_entry = self.entries.get(f'{key}_value')
        if key_entry and value_entry:
            new_key = key_entry.get().strip()
            new_value = value_entry.get().strip()
            if new_key != key:
                del self.data[key]
                key = new_key
            self.data[key] = new_value

    def add_new_pair(self):
        """Prompt user to enter a new key-value pair."""
        key_name = simpledialog.askstring("Input", "Enter new key name:")
        value_name = simpledialog.askstring("Input", "Enter value for the key:", initialvalue="")
        if key_name and key_name not in self.data:
            self.data[key_name] = value_name if value_name else ''
            self.update_list_items(self.data)

    def insert_media(self):
        """Prompt user to select an image/document file and insert it into the data dictionary."""
        file_path = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
        if file_path:
            with open(file_path, 'rb') as file:
                media_data = base64.b64encode(file.read()).decode('utf-8')
                key_name = simpledialog.askstring("Input", "Enter key name for the media file:")
                if key_name and key_name not in self.data:
                    self.data[key_name] = f'base64:{media_data}'
                    self.update_list_items(self.data)

    def save_base64_to_file(self, key):
        """Save the Base64 encoded data back to its original file format."""
        value = self.data.get(key)
        if value and value.startswith('base64:'):
            file_path = filedialog.asksaveasfilename(defaultextension=".file", filetypes=[("All files", "*.*")])
            if file_path:
                try:
                    decoded_data = base64.b64decode(value[7:])
                    with open(file_path, 'wb') as file:
                        file.write(decoded_data)
                    messagebox.showinfo("Success", "File saved successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save file: {str(e)}")

    def remove_pair(self, key):
        del self.data[key]
        self.update_list_items(self.data)

    def open_kvti(self):
        path = filedialog.askopenfilename(filetypes=[("KVTI files", "*.kvti")])
        if path:
            with open(path, 'r') as file:
                content = file.read()
                self.data = self.parse_kvti_content(content)
                self.has_file = True
                self.welcome_label.pack_forget()  # Hide welcome message
                self.update_list_items(self.data)
                self.update_add_pair_button_visibility()
                self.update_insert_media_button_visibility()

    def open_kvtie(self):
        path = filedialog.askopenfilename(filetypes=[("KVtie files", "*.kvtie")])
        if path:
            with open(path, 'rb') as file:
                encrypted_content = file.read()
                try:
                    decrypted_content = base64.b64decode(encrypted_content).decode('utf-8')
                    self.data = self.parse_kvti_content(decrypted_content)
                    self.has_file = True
                    self.welcome_label.pack_forget()  # Hide welcome message
                    self.update_list_items(self.data)
                    self.update_add_pair_button_visibility()
                    self.update_insert_media_button_visibility()
                except Exception as e:
                    messagebox.showerror("Error", str(e))

    def save_kvti(self):
        content = self.format_kvti_content(self.data)
        path = filedialog.asksaveasfilename(defaultextension=".kvti", filetypes=[("KVTI files", "*.kvti")])
        if path:
            with open(path, 'w') as file:
                file.write(content)

    def save_kvtie(self):
        content = self.format_kvti_content(self.data)
        encrypted_content = base64.b64encode(content.encode('utf-8'))
        path = filedialog.asksaveasfilename(defaultextension=".kvtie", filetypes=[("KVtie files", "*.kvtie")])
        if path:
            with open(path, 'wb') as file:
                file.write(encrypted_content)

if __name__ == "__main__":
    app = ttk.Window("KVTI Editor", "litera")
    editor = KVTIEditor(app)
    app.mainloop()