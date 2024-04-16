mode = "r+"
file = open("text_lab2.txt", mode) # путь до файла
try:
  file = open("text_lab2.txt")
except FileNotFoundError:
  print("Ошибка: Файл не найден")
else:
  print("Файл открыт успешно")
print
