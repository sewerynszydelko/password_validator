""" Validators main file """
import string
from abc import ABC, abstractmethod
from hashlib import sha1
from requests import get


class ValidationError(Exception):
    """Error for validator"""


class Validator(ABC):
    """ Validator interface for Validators """
    @abstractmethod
    def __init__(self, text):
        """Force to iplement __init__ method"""

    @abstractmethod
    def is_valid(self):
        """Force to iplement is_valid method"""


class LenghtValidator(Validator):
    """ Lenght Validaotr """

    def __init__(self, text):
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
        if len(self.text) >= lenght:
            return True

        raise ValidationError("Text is too short")


class HasLowerCharactersValidator(Validator):
    """ Check of given text has any lower case characters """

    def __init__(self, text):
        self.text = text

    def is_valid(self) -> bool:
        """ Look if any leter is lower in given text
        Returns:
            Bool: True or Raise Error with messegae
        """
        if any(letter.islower() for letter in self.text):
            return True

        raise ValidationError("Text has no lower letters")


class HasUpperCharactersValidator(Validator):
    """ Upper Case Validator """

    def __init__(self, text):
        self.text = text

    def is_valid(self):
        """
        Raises:
            ValidationError: riases with message if is not valid
        Returns:
            bool: True or Raise error
        """
        if any(letter.isupper() for letter in self.text):
            return True

        raise ValidationError("Text has no Upper case letters")


class HasNumberValidator(Validator):
    """ Number Validator """

    def __init__(self, text):
        self.text = text

    def is_valid(self):
        """Check if data hvae any number
        Raises:
            ValidationError: Raises when is not valid
        Returns:
            bool: True or riase error with proper message
        """
        if any(char.isnumeric() for char in self.text):
            return True

        raise ValidationError("Text has no numbers")


class HasPunctuationValidator(Validator):
    """ Punctuation Validator """

    def __init__(self, text):
        self.text = text

    def is_valid(self) -> bool:
        """ Check if text is valid
        Raises:
            ValidationError: text has no punctuations
        Returns:
            bool: True or raise error
        """
        if any(char in string.punctuation for char in self.text):
            return True

        raise ValidationError("Text has no punctiations like:'!@#$%^&*()_+'")


class HaveBeenPwndValidator(Validator):
    """  Api Have Been Powned Validator """

    def __init__(self, text):
        self.text = text

    def is_valid(self) -> bool:
        """ Check if data is powned
        Raises:
            ValidationError: Raises if data is leaaked
        Returns:
            bool: True if valid or rasies Eror with proper message
        """
        hashed_password = sha1(self.text.encode("utf-8")).hexdigest().upper()
        respone = get("https://api.pwnedpasswords.com/range/" +
                      hashed_password[:5], timeout=7)

        splited_data = respone.text.splitlines()
        hashe_data = [data[:data.find(":")] for data in splited_data]

        if hashed_password[5:] in hashe_data:
            raise ValidationError("Password has been powned !!")

        return True


class PasswordValidator(Validator):
    """Password validator"""
    def __init__(self, password) -> None:
        self.password = password
        self.validators = [LenghtValidator,
                        HasLowerCharactersValidator,
                        HasUpperCharactersValidator,
                        HasNumberValidator,
                        HasPunctuationValidator,
                        HaveBeenPwndValidator]

    def is_valid(self) -> bool:
        """ Check if password is valid
        Returns:
            bool: Return True if all pasword pass all validators
        """
        for clas_name in self.validators:
            result = clas_name(self.password)
            result.is_valid()

        return True
