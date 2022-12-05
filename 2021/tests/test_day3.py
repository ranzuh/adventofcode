import day3
import pathlib
import pytest

@pytest.mark.skip(reason="not implemented yet")
def test_part1_example1():
    input = pathlib.Path("tests/day3_example1.txt").read_text().splitlines()
    output = day3.part1(input)
    assert output == 0

@pytest.mark.skip(reason="not implemented yet")
def test_part2_example1():
    input = pathlib.Path("tests/day3_example1.txt").read_text().splitlines()
    output = day3.part2(input)
    assert output == 0