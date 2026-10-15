
import pytest
from process import process


@pytest.mark.statement
@pytest.mark.parametrize("values, expected", [
    pytest.param([2], ["positivo", "par"], id="CP01-R1"),
])
def test_statement_coverage(values, expected):
    assert process(values) == expected


@pytest.mark.branch
@pytest.mark.parametrize("values, expected", [
    pytest.param([2], ["positivo", "par"], id="CP01-R1-verdadero-verdadero"),
    pytest.param([-3], [], id="CP02-R4-falso-falso"),
])
