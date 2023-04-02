# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""

def get_users_list(csv):
    data = read(csv)
    sort_data = sort(data)
    filter_data = filter(data, 30)
    return data, sort_data, filter_data

def read(csv: str):
    return [pair.split(';') for pair in csv.split('\n')]

def sort(data, reverse: bool = False):
    return sorted(data, reverse=reverse)

def filter(data, filter):
    return [pair for pair in data if int(pair[1]) > filter]


if __name__ == '__main__':
    print(get_users_list(csv))
