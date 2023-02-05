# 1 вариант решения

with open('C:\\Users\\ATroshkin\\PycharmProjects\\For_task8.txt') as f:
    text = f.read()

text_2 = ''.join(reversed(text))

with open('Reverse_For_task8.txt', 'w+') as rv_f:
    rv_f.write(text_2)

with open('C:\\Users\\ATroshkin\\PycharmProjects\\For_task8.txt') as f:
    print(f.read())

with open('Reverse_For_task8.txt', 'r') as rv_f:
    print(rv_f.read())



# 2 вариант решения

f = open('task8.txt', 'r')
v2_text_1 = f.read()
f.close()

v2_text_2 = ''.join(reversed(v2_text_1))

f = open('2_task8.txt', 'w')
f.write(v2_text_2)
f.close()

print(v2_text_1)
print(v2_text_2)

#Можно ли записать текст из файла в файл не через переменные text , text_2 ?