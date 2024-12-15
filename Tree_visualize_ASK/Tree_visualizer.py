import tkinter as tk

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTreeVisualizer:
    def __init__(self, root):
        self.root = root
        self.canvas_width = 800
        self.canvas_height = 400
        self.node_radius = 20
        self.level_height = 70

    def draw_tree(self, canvas, node, x, y, x_offset):
        if node is not None:
            canvas.create_oval(
                x - self.node_radius, y - self.node_radius,
                x + self.node_radius, y + self.node_radius,
                fill="lightblue"
            )
            canvas.create_text(x, y, text=str(node.key))

            if node.left:
                canvas.create_line(x, y, x - x_offset, y + self.level_height)
                self.draw_tree(canvas, node.left, x - x_offset, y + self.level_height, x_offset // 2)

            if node.right:
                canvas.create_line(x, y, x + x_offset, y + self.level_height)
                self.draw_tree(canvas, node.right, x + x_offset, y + self.level_height, x_offset // 2)

    def visualize(self):
        window = tk.Tk()
        window.title("Binary Tree Visualizer")
        canvas = tk.Canvas(window, width=self.canvas_width, height=self.canvas_height, bg="white")
        canvas.pack()
        self.draw_tree(canvas, self.root, self.canvas_width // 2, 50, self.canvas_width // 4)
        window.mainloop()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.right = Node(7)
visualizer = BinaryTreeVisualizer(root)
visualizer.visualize()
