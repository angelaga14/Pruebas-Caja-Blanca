
import pytest
from process import process


# ETAPA 1: STATEMENT COVERAGE

@pytest.mark.statement
@pytest.mark.parametrize(
    "values, expected",
    [
        ([2], ["positivo", "par"]),
    ]
)
def test_statement_coverage(values, expected):
    assert process(values) == expected


# ETAPA 2: BRANCH COVERAGE

@pytest.mark.branch
@pytest.mark.parametrize(
    "values, expected",
    [
        ([2], ["positivo", "par"]),
        ([-3], []),
    ]
)
def test_branch_coverage(values, expected):
    assert process(values) == expected


# ETAPA 3: PATH COVERAGE

@pytest.mark.path
@pytest.mark.parametrize(
    "values, expected",
    [
        ([2, 2], ["positivo", "par", "positivo", "par"]),
        ([2, 3], ["positivo", "par", "positivo"]),
        ([2, -2], ["positivo", "par", "par"]),
        ([2, -3], ["positivo", "par"]),
        ([3, 2], ["positivo", "positivo", "par"]),
        ([3, 3], ["positivo", "positivo"]),
        ([3, -2], ["positivo", "par"]),
        ([3, -3], ["positivo"]),
        ([-2, 2], ["par", "positivo", "par"]),
        ([-2, 3], ["par", "positivo"]),
        ([-2, -2], ["par", "par"]),
        ([-2, -3], ["par"]),
        ([-3, 2], ["positivo", "par"]),
        ([-3, 3], ["positivo"]),
        ([-3, -2], ["par"]),
        ([-3, -3], []),
    ]
)
def test_path_coverage(values, expected):
    assert process(values) == expected
