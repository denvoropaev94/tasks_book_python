text = ' This guide is maintained on GitHub by the Python Packaging Authority. We happily accept any contributions and feedback. '

with open('some_dir/dir/new_file.txt', 'a', encoding='utf-8') as f:
    res = f.write(text)
    print(f'{res = }\n{len(text) = }')