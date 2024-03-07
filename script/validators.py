import string
from abc import ABC, abstractmethod
from requests import get


class ValidationError(Exception):
    pass


class Validator(ABC):
    """ Validator interface
    """
    @abstractmethod
    def __init__(self, text):
        pass

    @abstractmethod
    def is_valid(self):
        pass


class LenghtValidator(Validator):
    """ Lenght Validaotr
    """

    def __init__(self, text):
        """ Initalize validaotr lenght"""
        self.text = text

    def is_valid(self, lenght=8) -> bool:
        """ Valid if given text is long enought
        Args:
            lenght (int, optional): Can be adjust . Defaults to 8.
        Raises:
            ValidationError: Riaise when text is shorter than set lenght
        Returns:
            bool : True or raise error
        """
        if len(self.text) == lenght:
            return True

        raise ValidationError("Text is too short")


class HasLowerCharactersValidator(Validator):

    def __init__(self, text):
        self.text = text

    def is_valid(self):
        if any(letter.islower() for letter in self.text):
            return True

        raise ValidationError("Text has no lower letters")


class HasUpperCharactersValidator(Validator):

    def __init__(self, text):
        self.text = text

    def is_valid(self):
        if any(letter.isupper() for letter in self.text):
            return True

        raise ValidationError("Text has no Upper case letters")


class HasNumberValidator(Validator):

    def __init__(self, text):
        self.text = text

    def is_valid(self):
        if any(char.isnumeric() for char in self.text):
            return True

        raise ValidationError("Text has no numbers")


class HasPunctuationValidator(Validator):

    def __init__(self, text):
        self.text = text

    def is_valid(self):
        if any(char in string.punctuation for char in self.text):
            return True

        raise ValidationError("Text has no punctiations like:'!@#$%^&*()_+'")


class PasswordValidator(Validator):

    def __init__(self, password) -> None:
        self.password = password

    def is_valid(self):
        pass
