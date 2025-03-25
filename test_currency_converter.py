import pytest
from pytest import raises
from currency_converter import CurrencyConverter


@pytest.fixture
def currency_converter():
    return CurrencyConverter()


def test_valid_conversion(currency_converter):
    # Test valid conversions
    assert currency_converter.conversion("USD", "EUR", 150) == 138.0
    assert currency_converter.conversion("USD", "EUR", 150.10) == pytest.approx(
        138.092, rel=1e-2)  # Use approx with tolerance
    assert currency_converter.conversion("EUR", "USD", 100) == pytest.approx(
        109.0, rel=1e-2)  # Use approx with tolerance


def test_invalid_currency_pair(currency_converter):
    # Test invalid currency pairs
    with raises(ValueError):
        currency_converter.conversion("GBP", "EUR", 50)


def test_invalid_amount_type(currency_converter):
    # Test invalid amount type
    assert isinstance(currency_converter.conversion(
        "USD", "EUR", "50"), TypeError)


def test_invalid_currency_type(currency_converter):
    # Test invalid currency type
    assert isinstance(currency_converter.conversion(100, "EUR", 50), TypeError)
    assert isinstance(currency_converter.conversion("USD", 100, 50), TypeError)
    assert isinstance(currency_converter.conversion(
        "USD", "EUR", None), TypeError)


def test_missing_currency_type(currency_converter):
    # Test missing or non-existent currency pair
    with raises(ValueError):
        currency_converter.conversion("USD", "INR", 50)
    with raises(ValueError):
        currency_converter.conversion("CNY", "USD", 100)
