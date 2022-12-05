import template
import pathlib
import pytest

@pytest.mark.skip(reason="not implemented yet")
def test_part1_example1():
    input = pathlib.Path("tests/dayXX_example1.txt").read_text().splitlines()
    output = template.part1(input)
    assert output == 0

@pytest.mark.skip(reason="not implemented yet")
def test_part2_example1():
    input = pathlib.Path("tests/dayXX_example1.txt").read_text().splitlines()
    output = template.part2(input)
    assert output == 0