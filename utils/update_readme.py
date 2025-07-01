#!/usr/bin/env python3
"""
Script to automatically update the project structure in README.md
"""

import os
import re
from pathlib import Path

def get_project_structure(start_path=".", max_depth=3, exclude_dirs=None):
    """Generate project structure tree"""
    if exclude_dirs is None:
        exclude_dirs = {'.git', '__pycache__', '.pytest_cache', '.venv', 'venv', 'node_modules'}
    
    structure = []
    
    def add_to_structure(path, prefix="", depth=0):
        if depth > max_depth:
            return
            
        items = []
        try:
            for item in sorted(os.listdir(path)):
                if item in exclude_dirs or item.startswith('.'):
                    continue
                    
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    items.append(f"{prefix}├── {item}/")
                    add_to_structure(item_path, prefix + "│   ", depth + 1)
                else:
                    items.append(f"{prefix}├── {item}")
        except PermissionError:
            pass
            
        structure.extend(items)
    
    add_to_structure(start_path)
    return structure

def update_readme_structure():
    """Update the project structure section in README.md"""
    readme_path = "README.md"
    
    if not os.path.exists(readme_path):
        print("README.md not found!")
        return
    
    # Read current README
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Generate new structure
    structure_lines = get_project_structure()
    
    # Create the new structure section
    new_structure = "```\nselenium_demo/\n"
    for line in structure_lines:
        new_structure += line + "\n"
    new_structure += "```\n"
    
    # Replace the structure section in README
    pattern = r'```\nselenium_demo/.*?```\n'
    replacement = new_structure
    
    if re.search(pattern, content, re.DOTALL):
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        # Write updated README
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("✅ README.md project structure updated successfully!")
    else:
        print("❌ Could not find project structure section in README.md")

if __name__ == "__main__":
    update_readme_structure() 