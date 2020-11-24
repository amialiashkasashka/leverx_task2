from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, version):
        self.version = version

    def __eq__(self, other):
        return self.version == other.version

    def __lt__(self, other):
        return self.version < other.version


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
        print(f'{version_1} < {version_2} - ', Version(version_1) <  Version(version_2))
        print(f'{version_1} > {version_2} - ', Version(version_1) >  Version(version_2))
        print(f'{version_1} != {version_2} - ', Version(version_1) !=  Version(version_2))
        print('\n')


if __name__ == "__main__":
    main()