from validators import LenghtValidator, ValidationError
import pytest


def test_lenght_validator_positive():
    # given
    test_validator = LenghtValidator("abcdefgh")
    # when
    result = test_validator.is_valid()
    # then
    assert result is True


def test_lenght_validator_negative():
    # given
    test_validator = LenghtValidator("abc")
    # when
    """
    with pytest.raises(ValidationError) as error:
        test_validator.is_valid()
        
        assert "Text is too short" in str(error)"""
    with pytest.raises(ValidationError) as error:
        test_validator.is_valid()
        assert "Text is too short" in str(error.value)
