import pytest
from withdraw import verify_pin, withdraw

# Giả lập card_no demo
CARD_DEMO = "1234567890"

def test_verify_pin_correct():
    assert verify_pin(CARD_DEMO, "1234") == True

def test_verify_pin_wrong():
    assert verify_pin(CARD_DEMO, "9999") == False

def test_withdraw_success():
    result = withdraw(CARD_DEMO, 100)
    assert result == "Withdraw success"

def test_withdraw_insufficient_funds():
    result = withdraw(CARD_DEMO, 1000000)
    assert "Insufficient funds" in result


