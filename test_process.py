
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
