from validators import LenghtValidator, ValidationError, HasLowerLetterValidator
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
    with pytest.raises(ValidationError) as error:
        test_validator.is_valid()

        # then
        assert "Text is too short" in str(error.value)


def test_text_has_lower_letters_validaotr_possitive():
    # given
    validator = HasLowerLetterValidator("abCdeFG")

    # when
    result = validator.is_valid()

    # then
    assert result is True


def test_text_has_lower_letters_validaotr_negative():
    # given
    validator = HasLowerLetterValidator("ABCADA")

    # when
    with pytest.raises(ValidationError) as error:
        validator.is_valid()

        # then
        assert "Text has no lower letters" in str(error.value)
