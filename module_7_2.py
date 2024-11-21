def custom_write(file_name, string):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as f:
        for index, string in enumerate(string, start=1):
            byte_position = f.tell()
            f.write(string + '\n')
            strings_positions[(index, byte_position)] = string

    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)