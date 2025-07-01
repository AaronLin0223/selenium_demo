# Pages package - Page Object Models for Selenium tests
"""
This package contains all page object models for the web application.
Organized by functionality:
- Core pages: login, dashboard, sidebar, etc.
- DHCP pages: dhcp management functionality
- Directory pages: directory server management
"""

__version__ = "1.0.0"
__author__ = "Selenium Test Team"

import os
import importlib
import inspect
from .base_page import BasePage

# Auto-discover and import all page objects
def _discover_pages():
    """自動發現所有頁面對象"""
    pages = {}
    current_dir = os.path.dirname(__file__)
    
    # 遍歷所有 .py 文件
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            if file.endswith('.py') and file != '__init__.py':
                # 構建模塊路徑
                rel_path = os.path.relpath(root, current_dir)
                if rel_path == '.':
                    module_name = file[:-3]  # 移除 .py
                else:
                    module_name = f"{rel_path.replace(os.sep, '.')}.{file[:-3]}"
                
                try:
                    # 動態導入模塊
                    module = importlib.import_module(f".{module_name}", package=__name__)
                    
                    # 查找模塊中的類
                    for name, obj in inspect.getmembers(module):
                        if (inspect.isclass(obj) and 
                            issubclass(obj, BasePage) and 
                            obj != BasePage):
                            pages[name] = obj
                            
                except ImportError as e:
                    print(f"Warning: Could not import {module_name}: {e}")
    
    return pages

# 自動發現所有頁面
_discovered_pages = _discover_pages()

# 動態導入所有發現的頁面
for page_name, page_class in _discovered_pages.items():
    globals()[page_name] = page_class

# 定義 __all__ 為所有發現的頁面
__all__ = list(_discovered_pages.keys())

# Factory function for creating page objects
def create_page(page_name, driver, **kwargs):
    """
    Factory function to create page objects
    
    Args:
        page_name (str): Name of the page class
        driver: WebDriver instance
        **kwargs: Additional arguments for page constructor
    
    Returns:
        Page object instance
    """
    if page_name not in _discovered_pages:
        available_pages = list(_discovered_pages.keys())
        raise ValueError(f"Unknown page: {page_name}. Available: {available_pages}")
    
    return _discovered_pages[page_name](driver, **kwargs)

# 提供頁面列表
def get_available_pages():
    """獲取所有可用的頁面對象列表"""
    return list(_discovered_pages.keys())

# 打印發現的頁面（用於調試）
if __name__ == "__main__":
    print("Discovered pages:")
    for page_name in _discovered_pages.keys():
        print(f"  - {page_name}") 