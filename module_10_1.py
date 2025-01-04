import threading
import time

def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for word in range(word_count):
            file.write(f'какое-то слово №{word + 1}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time.time()
print(f'разница начала и конца работы функций {end_time - start_time}')

start2_time = time.time()
th1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
th2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
th3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
th4 = threading.Thread(target=write_words, args= (100, 'example8.txt'))

th1.start()
th2.start()
th3.start()
th4.start()

th1.join()
th2.join()
th3.join()
th4.join()

end2_time = time.time()
print(f'Работа потоков {end2_time - start2_time}')