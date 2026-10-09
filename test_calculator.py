import pytest
from calculator import calculate_commission

class TestCalculateCommission:
    #Позитивные тесты:
    @pytest.mark.parametrize("amount, expected", [
        (100, 50.0),
        (1000, 50.0),
        (1001, 100.0),
        (20000, 100.0),
        (20001, 400.01),
        (50000, 700.0),
        (150, 50.0),
        (11111, 100.0)
    ])
    def test_commission_calculation(self, amount, expected):
        assert calculate_commission(amount) == expected

    #Негативные тесты
    @pytest.mark.parametrize("invalid_amount", [99, 50001, -1, 0])
    def test_commission_invalid_amount_raises_error(self, invalid_amount):
        with pytest.raises(ValueError):
            calculate_commission(invalid_amount)

    @pytest.mark.parametrize("invalid_input", ["abc", None, ""])
    def test_commission_non_numeric_raises_type_error(self, invalid_input):
        with pytest.raises(TypeError):
            calculate_commission(invalid_input)
