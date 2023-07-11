text = ['To get an overview of the flow used to publish your code, see the packaging flow',
        'To learn how to install packages, see the tutorial on installing packages',
        'To learn how to manage dependencies in a version controlled project, see the tutorial on managing'
        ]
with open('new_file.txt', 'w', encoding='utf-8') as f:
    print(f.tell())
    for line in text:
        f.write(f'{line}\n')
        print(f.tell())
    print(f.tell())