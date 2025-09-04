import os

def list_folder_structure(folder_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(folder_path):
            # Calculate the depth (for indentation)
            level = root.replace(folder_path, '').count(os.sep)
            indent = ' ' * 4 * level
            # Write folder name
            f.write(f'{indent}[{os.path.basename(root)}/]\n')
            sub_indent = ' ' * 4 * (level + 1)
            for file in files:
                f.write(f'{sub_indent}{file}\n')

if __name__ == "__main__":
    folder_path = "./tongue"  # target folder
    output_file = "folder_structure.txt"
    list_folder_structure(folder_path, output_file)
    print(f"Folder structure written to {output_file}")
