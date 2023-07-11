with open('text_data.txt', 'r', encoding='utf-8') as f:
    res = f.read()
    print(f'Read first\n{res}')
    res = f.read()
    print(f'Read second\n{res}')