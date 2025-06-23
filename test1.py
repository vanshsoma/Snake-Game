import tkinter as tk

class GridExample:
    def __init__(self, master, rows, cols, cell_size):
        self.master = master
        self.master.title("Grid Example")

        self.canvas = tk.Canvas(master, width=cols * cell_size, height=rows * cell_size, bg="black")
        self.canvas.pack()

        # Draw horizontal grid lines
        for i in range(1, rows):
            y = i * cell_size
            self.canvas.create_line(0, y, cols * cell_size, y, fill="white")

        # Draw vertical grid lines
        for j in range(1, cols):
            x = j * cell_size
            self.canvas.create_line(x, 0, x, rows * cell_size, fill="white")

if __name__ == "__main__":
    rows = 30
    cols = 30
    cell_size = 20

    root = tk.Tk()
    app = GridExample(root, rows, cols, cell_size)
    root.mainloop()
