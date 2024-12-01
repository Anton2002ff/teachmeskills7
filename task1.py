#Задание 1 по Lambda

# greet = lambda name: f"Hello, {name}"
# print(greet("Anton"))


#Задание 2

names = ["Егор", "Влад", "Кристина"]
formatted_names = list(map(lambda name: f"Hello, {name}", names))
print(formatted_names)

#Заданий по генератору
# def positive_numbers_generator(numbers):
#     for number in numbers:
#         if number > 0:
#             yield number
#
#
# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
# positive_numbers = list(positive_numbers_generator(numbers))
# print(positive_numbers)

#Задание 2

# sentence = "thequick brown fox jumps over the lazy dog"
# words = sentence.split()
# lengths = []
#
# for word in words:
#     if word != "the":
#         lengths.append(len(word))
#
# print(lengths)

