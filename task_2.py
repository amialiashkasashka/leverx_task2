'''
    List out of range problem fixed by adding '=' to each version (to get one more iteration)
    ex. 1.0.0 / 1.0.0b. '=' = separator between letters/digits
'''

import re
from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, version):
        self.version = version
        self.splitted_version = self._split_version(self.version)
        self.priority_list = ['a', 'b', 'r', '=', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


    def __eq__(self, other):
        this_splitted_version = self.splitted_version
        other_splitted_version = self._split_version(other.version)
        this_splitted_version.append('=')
        other_splitted_version.append('=')
        len_max_v = max(len(this_splitted_version), len(other_splitted_version))


        # решает в каких случаях нужно добавлять нули для сравнения, добавить дешевле, чем удалить
        for i in range(0, len_max_v):
            if this_splitted_version[i] == other_splitted_version[i]:
                shorter_v, longer_v = this_splitted_version, other_splitted_version
                if len(shorter_v) > len(longer_v):
                    shorter_v, longer_v = other_splitted_version, this_splitted_version
                nulls_ending = False
                for _ in longer_v:
                    if longer_v.count('0') == len(longer_v) - len(shorter_v):
                        nulls_ending = True
                        break
                if nulls_ending == True:
                    shorter_v = self.add_nulls_to_shorter(shorter_v=shorter_v, longer_v=longer_v)
                return shorter_v == longer_v
            continue

    def __lt__(self, other):
        this_splitted_version = self.splitted_version
        other_splitted_version = self._split_version(other.version)
        this_splitted_version.append('=')
        other_splitted_version.append('=')
        len_max_v = max(len(this_splitted_version), len(other_splitted_version))

        for i in range(0, len_max_v):
            if this_splitted_version[i] == other_splitted_version[i]:
                # shorter_v, longer_v = this_splitted_version, other_splitted_version
                # if len(shorter_v) > len(longer_v):
                #     shorter_v, longer_v = other_splitted_version, this_splitted_version
                # if longer_v.count('0') == len(longer_v) - len(shorter_v):
                #     shorter_v = self.add_nulls_to_shorter(shorter_v=shorter_v, longer_v=longer_v)
                #     print(shorter_v)
                #     print(longer_v)
                #     return shorter_v < longer_v
                continue

            elif this_splitted_version[i].isdigit() and other_splitted_version[i].isdigit():
                return int(this_splitted_version[i]) < int(other_splitted_version[i])

            return self.priority_list.index(this_splitted_version[i]) < \
                      self.priority_list.index(other_splitted_version[i])

    # для версий наподобие '1.1' == '1.1.0'
    def add_nulls_to_shorter(self, shorter_v: list, longer_v: list) -> list:
        if '=' in shorter_v:
            shorter_v.remove('=')
        while len(shorter_v) < len(longer_v) - 1:
            shorter_v.append('0')
        shorter_v.append('=')
        return shorter_v

    def _split_version(self, version: str) -> list:
        return re.findall(r"\d{1,}|(?<![a-zA-Z])[a-zA-Z]", version)



def main():
    to_test = [
        ("1.0.0", "2.0.0"),
        ("1.0.0", "1.42.0"),
        ("1.2.0", "1.2.42"),
        ("1.1.0-alpha", "1.2.0-alpha.1"),
        ("1.0.1b", "1.0.10-alpha.beta"),
        ("1.0.0-rc.1", "1.0.0"),
    ]

    for version_1, version_2 in to_test:
        assert Version(version_1) < Version(version_2), "le failed"
        assert Version(version_2) > Version(version_1), "ge failed"
        assert Version(version_2) != Version(version_1), "neq failed"



if __name__ == "__main__":
    main()