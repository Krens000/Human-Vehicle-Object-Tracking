import os

def ensure_dir(path):
    """Create directory if not exists"""
    if not os.path.exists(path):
        os.makedirs(path)
