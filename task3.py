import sys
import re

path = sys.argv[1]
extra_command = sys.argv[2] if len(sys.argv) == 3 else ""


def parse_log_line(line: str) -> dict:
    logs = {}
    if (len(line) > 0):
        items = line.split(' ')
        logs['date'] = items[0]
        logs['time'] = items[1]
        logs['level'] = items[2]
        logs['message'] = ' '.join(items[3:])
    return logs


def load_logs(file_path: str) -> list:
    try:
        with open(file_path, mode='r') as fh:
            all_file = fh.read().split('\n')
            return all_file
    except FileNotFoundError:
        return (0, 0)


def filter_logs_by_level(logs: list, level: str) -> list:
    filtered = list(
        filter(lambda x: x and x['level'].lower() == level.lower(), logs))

    return filtered


def count_logs_by_level(logs: list) -> dict:
    counted_logs = {
        'INFO': 0,
        'DEBUG': 0,
        'ERROR': 0,
        'WARNING': 0
    }
    for i in logs:
        if i:
            match i['level']:
                case 'INFO':
                    counted_logs['INFO'] += 1
                case 'DEBUG':
                    counted_logs['DEBUG'] += 1
                case 'ERROR':
                    counted_logs['ERROR'] += 1
                case 'WARNING':
                    counted_logs['WARNING'] += 1
    return counted_logs


def display_log_counts(counts: dict):
    text1 = 'Рівень логування '
    text2 = ' Кількість'
    print(text1+"|"+text2)
    print('-'*len(text1)+"|"+'-'*len(text2))
    formatted_list = map(
        lambda kv: kv[0] + ' ' * (len(text1) - len(kv[0])) + '|' + ' ' + str(kv[1]), counts.items())
    for item in formatted_list:
        print(item)


if len(extra_command) == 0:

    logs = load_logs(path)
    parsed_logs = list(map(parse_log_line, logs))

    display_log_counts(count_logs_by_level(parsed_logs))
else:
    logs = load_logs(path)
    parsed_logs = filter_logs_by_level(
        list(map(parse_log_line, logs)), extra_command)
    print('Деталі логів для рівня ' + extra_command + ':')
    for i in parsed_logs:
        print(i['date'] + ' ' + i['time'] + ' - ' + i['message'])
