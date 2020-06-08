from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re


def merge_lists(list2, list1):
    # print(list1)
    # print(list2)
    for i in range(len(list1)):
        if list1[i] == '':
            list1[i] = list2[i]
    return list1


with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)
# print(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
space_pattern = re.compile(r"((^[а-яА-Я]+)\s([а-яА-Я]+)(\s([а-яА-Я]+))*$)")
# pattern = re.compile(r"^(\+7|8)\s*\(*(\d{0, 3})\)*\s*\-?(\d{0, 3})\-?(\d{0, 2})\-?(\d{0, 2})\s*\(*([
# а-я]+\.\s\d+)?\)*$", re.MULTILINE)
phone_pattern = r"^(\+7|8)\s*\(*(\d{0,3})\)*\s*\-?(\d{0,3})\-?(\d{0,2})\-?(\d{0,2})\s*\(*([а-я]+\.\s\d+)?\)*$"
subst = "+7(\\2)\\3-\\4-\\5 \\6"
contacts = {}
# print(len(contacts_list))
for line in contacts_list:
    # print(line)

    if re.match(space_pattern, line[0]):
        # print(re.match(space_pattern, line[0]))
        split_line = line[0].split()
        line[0] = split_line[0]
        line[1] = split_line[1]
        if len(split_line) < 3:
            pass
        else:
            line[2] = split_line[2]
    elif re.match(space_pattern, line[1]):
        split_line = line[1].split()
        line[1] = split_line[0]
        line[2] = split_line[1]
    else:
        pass
    if line[0] in contacts:
        line = merge_lists(line, contacts[line[0]])
    else:
        contacts[line[0]] = line
    # print(contacts)
    text = line[-2]
    # print(text)
    result = re.sub(phone_pattern, subst, text, 0, re.MULTILINE)
    # print(result)
    line[-2] = result
# print(contacts_list)
new_contacts_list = []
for contact in contacts.values():
  new_contacts_list.append(contact)
print('~')
pprint(new_contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(new_contacts_list)
