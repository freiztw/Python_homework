#                                            2
# lines = ["first"]
# lines1 = ["first1"]
# lines2 = ["first2"]
# lines3 = ["first3"]
# with open("test.txt", "w") as file:
#     for line in lines:
#         file.write(line + '\n')
#     for line1 in lines1:
#         file.write(line1 + '\n')
# file.close()
# with open('test.txt', 'a') as file:
#     for line2 in lines2:
#         file.write(line2 + '\n')
#     for line3 in lines3:
#             file.write(line3)
# #
#
# text_file = open("test.txt", "w")
# n = text_file.write('Welcome1 ')
# b = text_file.write("\n"'Welcome2 ')
# text_file.close()
# text_file = open("test.txt", "a")
# q = text_file.write("\n"'Welcome3 ')
# aa = text_file.write("\n"'Welcome4')
# text_file.close()


# text_file = open("text.txt", "w")
# n = input("Введите имя: ")
# text_file.write(n + "\n")
# b = input("Введите имя: ")
# text_file.write(b + "\n")
# text_file.close()
# text_file = open("text.txt", "a")
# q = input("Введите имя: ")
# text_file.write(q + "\n")
# z = input("Введите имя: ")
# text_file.write(z + "\n")
# text_file.close()



import json # не уверен в этом задании)

my_dict = {
    123: ('joe', 300000),
    321: ('brad', 255555),
}

with open('my_dict.json', 'w') as f:
    json.dump(my_dict, f, indent=4)