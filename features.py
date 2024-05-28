import re
import fuzzywuzzy.fuzz


def features(username: str, name: str) -> list:
    result = []
    username = re.sub(r'[^a-zA-Z0-9\s]', '', username)
    name = re.sub(r'[^a-zA-Z0-9\s]', '', name)
    count_num_username = 0
    for char in username:
        if char.isdigit():
            count_num_username += 1
    count_words_name = len(name.split(' '))
    count_num_name = 0
    for char in name:
        if char.isdigit():
            count_num_name += 1
    nums_username = count_num_username / len(username)
    nums_name = count_num_name / len(name)
    name_username = 1 if fuzzywuzzy.fuzz.ratio(username, name) > 40 else 0
    result += [nums_username, count_words_name, nums_name, name_username]
    return result
