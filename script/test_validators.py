from validators import (LenghtValidator,
                        ValidationError,
                        HasLowerCharactersValidator,
                        HasUpperCharactersValidator,
                        HasNumberValidator,
                        HasPunctuationValidator)
import pytest


def test_if_lenght_validator_positive():
    # given
    test_validator = LenghtValidator("abcdefgh")

    # when
    result = test_validator.is_valid()

    # then
    assert result is True


def test_if_lenght_validator_negative():
    # given
    test_validator = LenghtValidator("abc")

    # when
    with pytest.raises(ValidationError) as error:
        test_validator.is_valid()

        # then
        assert "Text is too short" in str(error.value)


def test_if_text_has_lower_character_validaotr_possitive():
    # given
    validator = HasLowerCharactersValidator("abCdeFG")

    # when
    result = validator.is_valid()

    # then
    assert result is True


def test_if_text_has_lower_characters_validaotr_negative():
    # given
    validator = HasLowerCharactersValidator("ABCADA")

    # when
    with pytest.raises(ValidationError) as error:
        validator.is_valid()

    # then
        assert "Text has no lower letters" in str(error.value)


def test_if_text_has_upper_case_characters_validator_positive():
    # given
    validator = HasUpperCharactersValidator("abcdEfgg")

    # when
    result = validator.is_valid()

    # then
    assert result is True


def test__if_text_has_upper_case_characters_validator_negative():
    # given
    validator = HasUpperCharactersValidator("abcd")

    # when
    with pytest.raises(ValidationError) as error:
        validator.is_valid()

    # then
        assert "Text has no Upper case letters" in str(error.value)


def test_if_text_have_number_validator_positive():
    # given
    validator = HasNumberValidator("ab2cdww9w")

    # when
    result = validator.is_valid()

    # then
    assert result is True


def test_if_text_has_number_validator_negative():
    # given
    validator = HasNumberValidator("abcd")

    # when
    with pytest.raises(ValidationError) as error:
        validator.is_valid()

    # then
        assert "Text has no numbers" in str(error.value)


def test_if_text_has_punctuation_validator_positive():
    # given
    validator = HasPunctuationValidator("ab!c^d*%")

    # when
    result = validator.is_valid()

    # then
    assert result is True

def test_if_text_has_punctuation_validator_negative():
    # given
    validator = HasPunctuationValidator("abcssda")

    # when
    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert "Text has no punctiations like:'!@#$%^&*()_+'" in str(error.value)