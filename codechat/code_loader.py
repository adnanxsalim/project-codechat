import os

def load_codebase(path, file_extensions=None, max_file_size_kb=100):
    if file_extensions is None:
        file_extensions = [".py", ".js", ".ts", ".jsx", ".tsx", ".wasp", ".c", ".mjs", ".java", ".html", ".css", ".json"]

    code_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if any(file.endswith(ext) for ext in file_extensions):
                full_path = os.path.join(root, file)
                try:
                    if os.path.getsize(full_path) <= max_file_size_kb * 1024:
                        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            code_files.append((full_path, content))
                except Exception as e:
                    print(f"⚠️ Skipped {full_path}: {e}")
    return code_files
