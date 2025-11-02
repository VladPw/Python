def Open(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print(f"Помилка, файл {file_name} не вдалося відкрити")
        return None
    else:
        print(f"Файл {file_name} відкрито успішно")
        return file
file1_name = "TF10_1.txt"
file2_name = "TF10_2.txt"
file_1 = Open(file1_name, "w")
if file_1 is not None:
    file_1.write("2 Character strings for test 7 of laboratory work October 29\n")
    file_1.write("Another line 678 for code testing\n")
    file_1.close()
    print("Файл TF10_1.txt записано\n")
file_read = Open(file1_name, "r")
file_write = Open(file2_name, "w")
if file_read is not None and file_write is not None:
    text = file_read.read()
    text_no_digits = ''.join([ch for ch in text if not ch.isdigit()])
    for i in range(0, len(text_no_digits), 10):
        file_write.write(text_no_digits[i:i+10] + '\n')
    file_read.close()
    file_write.close()
    print("Цифри вилучено, нові дані у файлі TF10_2 записано\n")
file_final = Open(file2_name, "r")
if file_final is not None:
    print("Вміст файлу TF10_2.txt:")
    for line in file_final:
        print(line.strip())
    file_final.close()
    print("Файл TF10_2.txt закрито")