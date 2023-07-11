text = ['To get an overview of the flow used to publish your code, see the packaging flow',
        'To learn how to install packages, see the tutorial on installing packages',
        'To learn how to manage dependencies in a version controlled project, see the tutorial on managing '
        'application dependencies']
with open('some_dir/dir/new_file.txt', 'a', encoding='utf-8') as f:
    for line in text:
        res = f.write(f'{line}\n')
        print(f'{res = }\n{len(line) = }')
