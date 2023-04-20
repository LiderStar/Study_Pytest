from Lesson2.utils.read_func import read_from_file


def test_read_func():
    test_data = ['one\n', 'two\n', 'three\n', 'four\n', 'five\n', 'six']
    assert test_data == read_from_file("test.txt")

