import os


ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
main_path = os.path.join(ROOT_DIR, 'main.py')
src_dir = os.path.join(ROOT_DIR, 'src')
app_dir = os.path.join(src_dir, 'app')
assets_dir = os.path.join(src_dir, 'assets')
img_dir = os.path.join(assets_dir, 'img')
