import base64
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter import ttk
import ttkbootstrap as ttkb

class KVTIEditor(ttkb.Window):
    def __init__(self):
        super().__init__()
        self.title("KVTI 文件编辑器")
        self.geometry('800x600')

        # UI Elements
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets for the application."""
        frame = ttkb.Frame(self, padding=10)
        frame.pack(fill=tk.BOTH, expand=tk.YES)

        # Treeview for displaying KVTI data
        columns = ('key', 'value')
        self.tree = ttkb.Treeview(frame, columns=columns, show='headings')
        self.tree.heading('key', text='键')
        self.tree.heading('value', text='值')
        self.tree.grid(row=0, column=0, sticky=tk.NSEW)
        self.tree.bind("<Double-1>", self.edit_entry)  # Bind double-click event

        # Add scrollbars to treeview
        vsb = ttkb.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        vsb.grid(row=0, column=1, sticky='ns')
        self.tree.configure(yscrollcommand=vsb.set)

        # Buttons for actions
        button_frame = ttkb.Frame(frame)
        button_frame.grid(row=1, column=0, pady=5, sticky=tk.EW)

        ttkb.Button(button_frame, text="打开", command=self.open_file).grid(row=0, column=0, padx=5)
        ttkb.Button(button_frame, text="保存", command=self.save_file).grid(row=0, column=1, padx=5)
        ttkb.Button(button_frame, text="添加条目", command=self.add_entry).grid(row=0, column=2, padx=5)
        ttkb.Button(button_frame, text="删除条目", command=self.remove_entry).grid(row=0, column=3, padx=5)
        ttkb.Button(button_frame, text="导入文件", command=self.import_file).grid(row=0, column=4, padx=5)
        ttkb.Button(button_frame, text="导出文件", command=self.export_file).grid(row=0, column=5, padx=5)

        # Configure grid weights so that treeview can expand
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

    def open_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("KVTI files", "*.kvti"), ("KVTIE files", "*.kvtie")])
        if not filepath:
            return

        with open(filepath, "r") as file:
            content = file.read()
            if filepath.endswith('.kvtie'):
                content = base64.b64decode(content).decode()
            data = self.parse_kvti_content(content)

            for item in self.tree.get_children():
                self.tree.delete(item)

            for key, value in data.items():
                self.tree.insert('', tk.END, values=(key, value))

    def save_file(self):
        filepath = filedialog.asksaveasfilename(defaultextension="kvti", filetypes=[("KVTI files", "*.kvti"), ("KVTIE files", "*.kvtie")])
        if not filepath:
            return

        data = {}
        for item in self.tree.get_children():
            key, value = self.tree.item(item)['values']
            try:
                # Attempt to decode as base64
                base64.b64decode(value.encode())
            except Exception:
                # If it fails, assume it's a string
                pass
            data[key] = value

        content = self.generate_kvti_content(data)
        if filepath.endswith('.kvtie'):
            content = base64.b64encode(content.encode()).decode()

        with open(filepath, "w") as file:
            file.write(content)

        messagebox.showinfo("保存成功", f"文件已保存到 {filepath}")

    def parse_kvti_content(self, content):
        """Parse the KVTI formatted content into a dictionary."""
        lines = content.strip().split('\n')
        data = {}
        for line in lines:
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()[1:-1]  # Remove brackets
                data[key] = value
        return data

    def generate_kvti_content(self, data):
        """Generate KVTI formatted content from a dictionary."""
        lines = []
        for key, value in data.items():
            lines.append(f"{key}=[{value}]")
        return "\n".join(lines)

    def add_entry(self):
        new_key = simpledialog.askstring("输入", "请输入键：")
        new_value = simpledialog.askstring("输入", "请输入值：")
        if new_key and new_value:
            self.tree.insert('', tk.END, values=(new_key, new_value))

    def remove_entry(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item[0])

    def edit_entry(self, event=None):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        item_id = selected_item[0]
        current_values = self.tree.item(item_id)['values']

        new_key = simpledialog.askstring("编辑", "请输入新的键：", initialvalue=current_values[0])
        new_value = simpledialog.askstring("编辑", "请输入新的值：", initialvalue=current_values[1])

        if new_key is not None and new_value is not None:
            self.tree.item(item_id, values=(new_key, new_value))

    def import_file(self):
        filepath = filedialog.askopenfilename()
        if not filepath:
            return

        with open(filepath, "rb") as file:
            encoded_data = base64.b64encode(file.read()).decode()
        key = filepath.split('/')[-1]  # Use filename as key
        self.tree.insert('', tk.END, values=(key, encoded_data))
        messagebox.showinfo("导入成功", f"文件 {key} 已导入")

    def export_file(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("警告", "请选择要导出的条目")
            return

        key, encoded_data = self.tree.item(selected_item[0])['values']
        filepath = filedialog.asksaveasfilename(defaultextension="", initialfile=key)
        if not filepath:
            return

        with open(filepath, "wb") as file:
            file.write(base64.b64decode(encoded_data))
        messagebox.showinfo("导出成功", f"文件已导出到 {filepath}")

if __name__ == "__main__":
    app = KVTIEditor()
    app.mainloop()