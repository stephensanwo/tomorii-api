import re
from .exceptions import Exceptions


def validateRegistrationInput(user):
    errors = {}

    # Validate String entries
    if user['first_name'].strip() == "":
        errors["first_name"] = (Exceptions(
            msg="First name is required", loc="first_name").dict())

    if user['last_name'].strip() == "":
        errors["last_name"] = (Exceptions(
            msg="Last name is required", loc="last_name").dict())

    if user['username'].strip() == "":
        errors["username"] = (Exceptions(
            msg="Username is required", loc="user_name").dict())

    # Validate Email
    if user['email'].strip() == "":
        errors["email"] = errors["email"] = (Exceptions(
            msg="Email is required", loc="email").dict())

    else:
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

        if re.search(regex, user['email']):
            pass
        else:
            errors["email"] = errors["email"] = (Exceptions(
                msg="Email must be a valid email address", loc="email").dict())

    # Validate Passwords

    if user['password'].strip() == "":
        errors["password"] = errors["password"] = (Exceptions(
            msg="Password is required", loc="password").dict())

    if user['confirm_password'].strip() == "":
        errors["confirm_password"] = (Exceptions(
            msg="Confirm password is required", loc="confirm_password").dict())

    if (user['password'] != user['confirm_password']):
        errors["confirm_password"] = (Exceptions(
            msg="Passwords must match", loc="confirm_password").dict())
        errors["password"] = errors["password"] = (Exceptions(
            msg="Passwords must match", loc="password").dict())

    valid = len(errors) < 1

    return errors, valid
