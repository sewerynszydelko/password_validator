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
    def is_valid(self, text):
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


class PasswordValidator(Validator):

    def __init__(self,password) -> None:
        self.password = password

    def is_valid(self):
        pass