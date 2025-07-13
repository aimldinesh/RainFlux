import os

def print_tree(startpath, max_depth=2):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        if level > max_depth:
            continue
        indent = '│   ' * level
        print(f"{indent}├── {os.path.basename(root)}/")
        subindent = '│   ' * (level + 1)
        for f in files:
            print(f"{subindent}└── {f}")

# Replace this with your actual project path
print_tree(r"D:\Mlops_course_2025\Mlops_new_course\MLOPS-PROJECTS\MLOPS_RainFlux_project")
