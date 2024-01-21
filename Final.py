import ast
import tkinter as tk

# Step 1: Define a basic lexer
def lexer(code):
    return code.split('\n')

# Step 2: Define a basic parser
def parser(tokens):
    code_str = '\n'.join(tokens)  # Assuming tokens is a list of strings
    tree = ast.parse(code_str, filename='<string>', mode='exec')
    return tree

# Step 3: Define a function to build a parse tree
def build_parse_tree(node, tree=None):
    if tree is None:
        tree = {'value': ast.dump(node), 'children': []}
    for child in ast.iter_child_nodes(node):
        child_node = {'value': ast.dump(child), 'children': []}
        tree['children'].append(child_node)
        build_parse_tree(child, tree=child_node)
    return tree

# Step 4: Define a function to visualize the parse tree using Tkinter
def visualize_tree(tree, canvas, x, y, level=0, parent_id=None, direction=None):
    text = f"{tree['value']} ({level})"
    node_id = canvas.create_rectangle(x, y, x + 150, y + 30, fill="lightblue")
    canvas.create_text(x + 5, y + 5, text=text, anchor='w', font=('Arial', 8, 'bold'))

    if parent_id is not None:
        label = f"{tree['value']} ({level})"
        if direction == 'left':
            canvas.create_text((x + parent_id) // 2, y - 10, text=label, anchor='s', font=('Arial', 8))
        else:
            canvas.create_text((x + parent_id) // 2, y - 10, text=label, anchor='s', font=('Arial', 8))

    y_offset = 70
    x_offset = 200

    child_ids = []
    for child in tree['children']:
        child_x = x + x_offset
        child_y = y + y_offset
        child_ids.append(visualize_tree(child, canvas, child_x, child_y, level + 1, node_id, 'right'))
        y_offset += 50

    return node_id

# Step 5: Example code
code1 = "mathresult1 = 5 * 4.3 + 2.1;"

# Step 6: Tokenize and parse
tokens1 = lexer(code1)
parsed_tree1 = build_parse_tree(parser(tokens1))

# Step 7: Visualize the parse tree using Tkinter
root = tk.Tk()
root.title("Parse Tree Visualization")

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

visualize_tree(parsed_tree1, canvas, 200, 50)

root.mainloop()
