with open('text.txt', 'r', encoding='utf-8') as f:
    s = f.read()
    key = input('Введите ключ шифрования: ')
    secret = ''
    for symbol in s:
        code = ord(symbol) + int(key)
        decode = chr(code)
        secret += decode
print('Текст зашифрован!')

with open('code.txt', 'w', encoding='utf-8') as f:
    f.write(secret)
print('Файл code.txt к отправке готов!')