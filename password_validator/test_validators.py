from validators import (LenghtValidator,
                        ValidationError,
                        HasLowerCharactersValidator,
                        HasUpperCharactersValidator,
                        HasNumberValidator,
                        HasPunctuationValidator,
                        HaveBeenPwndValidator)
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


def test_if_text_been_powned_validator_positive(requests_mock):
    # given
    mock_respone = "D09CA3762AF61E59520943DC26494F8941B:42542807"
    hashe_serched = "BA2CC086FC04994F05501E127257173697071519"

    requests_mock.get("https://api.pwnedpasswords.com/range/" +
                      hashe_serched[:5], text=mock_respone)
    validator = HaveBeenPwndValidator("DFSJI432$@$dfas")
    # when
    result = validator.is_valid()

    # then
    assert result is True


def test_is_text_benn_powned_validator_negative(requests_mock):
    # given
    mock_respone = "D09CA3762AF61E59520943DC26494F8941B:42542807"
    hashe_serched = "7C4A8D09CA3762AF61E59520943DC26494F8941B"

    requests_mock.get("https://api.pwnedpasswords.com/range/" +
                      hashe_serched[:5], text=mock_respone)
    validator = HaveBeenPwndValidator("123456")

    # when
    with pytest.raises(ValidationError) as error:
        validator.is_valid()
    # then
        assert "Password has been powned !!" in str(error.value)
