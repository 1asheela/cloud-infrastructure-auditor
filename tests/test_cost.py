def calculate_cost(hours, rate):
    return hours * rate

def test_cost_calculation():
    result = calculate_cost(10, 2)
    assert result == 20