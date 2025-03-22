# gui.py

import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import data_processing as dp

class StudentDataAnalyzerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Data Analyzer")

        self.filepath = None

        # Menu Frame
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack(pady=10)

        self.load_button = tk.Button(self.menu_frame, text="Load Data", command=self.open_file)
        self.load_button.grid(row=0, column=0, padx=5)

        self.analysis_button = tk.Button(self.menu_frame, text="Performance Analysis", command=self.perform_analysis)
        self.analysis_button.grid(row=0, column=1, padx=5)

        self.student_stats_button = tk.Button(self.menu_frame, text="Student Statistics", command=self.get_student_stats)
        self.student_stats_button.grid(row=0, column=2, padx=5)

        self.teacher_stats_button = tk.Button(self.menu_frame, text="Teacher Statistics", command=self.get_teacher_name)
        self.teacher_stats_button.grid(row=0, column=3, padx=5)

        # Plot Frame
        self.plot_frame = tk.Frame(self.root)
        self.plot_frame.pack(pady=10)

        self.fig = Figure(figsize=(10, 4), dpi=100)  # Adjust figsize for better layout
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack()

        # Text Box for displaying data
        self.text_box = tk.Text(self.root, height=20, width=140)  # Adjust height and width as needed
        self.text_box.pack(pady=10)

        # Author Label
        self.author_label = tk.Label(self.root, text="Authors: Visva V (23PD40), Ghirivaasan A (23PD11)")
        self.author_label.pack(side="bottom")

    def open_file(self):
        self.filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if self.filepath:
            messagebox.showinfo("File Loaded", f"Data loaded from: {self.filepath}")

    def perform_analysis(self):
        if self.filepath:
            try:
                dp.process_data(self.filepath, self.fig)
                self.canvas.draw()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred during analysis: {e}")
        else:
            messagebox.showerror("Error", "Please load a file first.")

    def get_student_stats(self):
        if self.filepath:
            try:
                roll_no = simpledialog.askinteger("Student Roll No.", "Enter student's roll number:")
                if roll_no:
                    student_stats = dp.display_student_stats(self.filepath, roll_no)
                    # Drop unnamed columns
                    student_stats = student_stats.loc[:, ~student_stats.columns.str.contains('^Unnamed')]
                    # Format the student statistics for display
                    student_stats_str = student_stats.to_string(index=True)
                    self.text_box.delete(1.0, tk.END)  # Clear previous content
                    self.text_box.insert(tk.END, student_stats_str)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while getting student statistics: {e}")
        else:
            messagebox.showerror("Error", "Please load a file first.")

    def get_teacher_name(self):
        if self.filepath:
            try:
                teacher_name = simpledialog.askstring("Teacher's Name", "Enter teacher's name:")
                if teacher_name:
                    teacher_stats = dp.display_teacher_stats(self.filepath, teacher_name)
                    self.text_box.delete(1.0, tk.END)  # Clear previous content
                    self.text_box.insert(tk.END, teacher_stats)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while getting teacher statistics: {e}")
        else:
            messagebox.showerror("Error", "Please load a file first.")

    def run(self):
        self.root.mainloop()
