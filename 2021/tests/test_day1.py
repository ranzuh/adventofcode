import day1
import pathlib

def test_part1_example1():
    input = pathlib.Path("tests/example1.txt").read_text().splitlines()
    output = day1.part1(input)
    assert output == 7

def test_part1_example2():
    input = pathlib.Path("tests/example2.txt").read_text().splitlines()
    output = day1.part1(input)
    assert output == 16

def test_part2_example1():
    input = pathlib.Path("tests/example1.txt").read_text().splitlines()
    output = day1.part2(input)
    assert output == 5