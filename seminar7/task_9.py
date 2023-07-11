text = ['As a popular open source development project, Python has an active supporting.',
        'community of contributors and users that also make their software available for',
        'other Python developers to use under open source license terms.']
with open ('some_dir/dir/new_file.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, end='***\n##', file=f)