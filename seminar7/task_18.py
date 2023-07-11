import os
from pathlib import Path

file_1 = os.path.join(os.getcwd(), 'new_os_dir', 'my_file.txt')
print(f'{file_1 = }\n{file_1}')

file_2 = Path().cwd() / 'new_path_dir' / 'my_file.txt'
print(f'{file_2 = }\n{file_2}')