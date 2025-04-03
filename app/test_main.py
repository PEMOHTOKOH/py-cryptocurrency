import pytest
from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,result",
    [
        (1, 2, "Buy more cryptocurrency"),
        (2, 1, "Sell all your cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: MagicMock,
        current_rate: int | float,
        prediction_rate: int | float,
        result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    assert (cryptocurrency_action(current_rate)) == result
