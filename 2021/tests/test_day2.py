import day2
import pathlib

def test_part1_example1():
    input = pathlib.Path("tests/day2_example1.txt").read_text().splitlines()
    output = day2.part1(input)
    assert output == 150

def test_part2_example1():
    input = pathlib.Path("tests/day2_example1.txt").read_text().splitlines()
    output = day2.part2(input)
    assert output == 900