import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from typing import Optional


class ChatbotApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.create_widgets()
        self.bind_events()

    def create_widgets(self):
        self.create_header()
        self.create_chat_area()
        self.create_footer()

        # make columns and rows expandable
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

    def create_header(self):
        self.style.configure("Header.TLabel", background="#3b3abe",
                             foreground="#ffffff", font=("Helvetica", 20), anchor="center")
        self.header_label = ttk.Label(
            self, text="Chatbot", style="Header.TLabel")
        self.header_label.grid(column=0, row=0, columnspan=4,
                               sticky=(tk.W, tk.E), pady=(20, 10))

    def create_chat_area(self):
        self.style.configure("My.TFrame", background="#f0f0f0", weight=1)
        self.chat_frame = ttk.Frame(self, padding="10", style="My.TFrame")
        self.chat_frame.grid(column=0, row=1, columnspan=4,
                             sticky=(tk.N, tk.S, tk.E, tk.W))
        self.chat_frame.columnconfigure(0, weight=1)
        self.chat_frame.rowconfigure(0, weight=1)

        self.chat_area = tk.Text(self.chat_frame, height=10, state="disabled", font=(
            "Helvetica", 12), wrap="word", background="#f0f0f0", padx=5, pady=5)
        self.chat_area.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.chat_area.columnconfigure(0, weight=1)
        self.chat_area.rowconfigure(0, weight=1)

        self.scrollbar = ttk.Scrollbar(
            self.chat_frame, orient="vertical", command=self.chat_area.yview)
        self.scrollbar.grid(column=1, row=0, sticky=(tk.N, tk.S))
        self.chat_area["yscrollcommand"] = self.scrollbar.set

    def create_footer(self):
        self.style.configure("My.TFrame", background="#181818")
        self.footer_frame = ttk.Frame(self, padding="10", style="My.TFrame")
        self.footer_frame.grid(
            column=0, row=2, columnspan=4, sticky=(tk.W, tk.E))

        # Set column weights
        self.footer_frame.grid_columnconfigure(0, weight=10)
        self.footer_frame.grid_columnconfigure(1, weight=1)
        self.footer_frame.grid_columnconfigure(2, weight=1)
        self.footer_frame.grid_columnconfigure(3, weight=1)

        self.message_entry = tk.Entry(self.footer_frame, width=70, font=(
            "Helvetica", 12), foreground="#ffffff", background="#181818")
        self.message_entry.config(
            insertofftime=0, insertwidth=2, relief="flat", insertbackground="#3b3abe")
        self.message_entry.grid(column=0, row=0, padx=(
            0, 10), pady=10, sticky=(tk.W, tk.E))

        self.load_images()
        self.create_buttons()

        self.style.configure("Color.TButton", background="#3b3abe", foreground="#ffffff", font=(
            "Helvetica", 12), borderwidth=0, highlightthickness=0)

        # Add padding between buttons
        self.footer_frame.grid_columnconfigure(1, minsize=5)
        self.footer_frame.grid_columnconfigure(2, minsize=5)

    def load_images(self):
        try:
            self.mic_icon = tk.PhotoImage(file="assets/mic.png")
            self.doc_icon = tk.PhotoImage(file="assets/file-upload.png")
        except FileNotFoundError as e:
            messagebox.showerror(
                "Error", f"Image file not found: {e.filename}")

    def create_buttons(self):
        self.mic_button = ttk.Button(
            self.footer_frame, image=self.mic_icon, command=self.open_mic, style="Color.TButton")
        self.mic_button.grid(column=1, row=0, padx=(0, 5), pady=5)

        self.file_button = ttk.Button(
            self.footer_frame, image=self.doc_icon, command=self.open_file, style="Color.TButton")
        self.file_button.grid(column=2, row=0, padx=(0, 5), pady=5)

        self.send_button = ttk.Button(
            self.footer_frame, text="Send", command=self.send_message, style="Color.TButton")
        self.send_button.grid(column=3, row=0, pady=5, sticky="e")

    def bind_events(self):
        self.message_entry.bind("<Return>", self.send_message)
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def open_mic(self):
        pass

    def open_file(self):
        pass

    def send_message(self, event=None):
        input_get = self.message_entry.get()
        print(input_get)
        self.update_chat_area("You -> " + input_get + "\n")
        self.message_entry.delete(0, tk.END)

    def update_chat_area(self, message: str):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, message)
        self.chat_area.config(state="disabled")
        self.chat_area.see(tk.END)

    def on_closing(self):
        pass
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Chatbot")
    # root.geometry("600x400")

    app = ChatbotApp(root)
    app.pack(fill="both", expand=True)

    root.mainloop()
