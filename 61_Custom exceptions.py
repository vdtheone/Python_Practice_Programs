# Custom exceptions

class MycustomException(Exception):
    pass

def devide(a, b):
    if b == 0:
        raise MycustomException("Division by zero is not allowed")
    return a/b

try:
    devide(10, 0)
except MycustomException as e:
    print("Error - ", e)


class ValidationError(Exception):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")


def validate_username(username):
    if len(username) < 5:
        raise ValidationError("username", "must be at least 5 characters long")


try:
    validate_username("abc")
except ValidationError as e:
    print(e)


class InsufficientBalanceError(Exception):
    pass


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(
                f"Requested {amount}, available {self.balance}"
            )
        self.balance -= amount
        return self.balance


account = BankAccount(100)

try:
    account.withdraw(150)
except InsufficientBalanceError as e:
    print("Transaction failed:", e)


class AppError(Exception):
    """Base class for application errors"""
    pass


class DatabaseError(AppError):
    pass


class AuthenticationError(AppError):
    pass


def login(token):
    if token != "valid":
        raise AuthenticationError("Invalid token")


try:
    login("invalid")
except AuthenticationError as e:
    print("Auth error:", e)
except AppError:
    print("General app error")


# try:
#     int("abc")
# except ValueError:
#     print("Logging error")
#     raise   # preserves traceback


# class ServiceError(Exception):
#     pass


# try:
#     1 / 0
# except ZeroDivisionError as e:
#     raise ServiceError("Service failed") from e



class TemporaryFailure(Exception):
    pass


def unreliable_service():
    raise TemporaryFailure("Temporary issue")


for attempt in range(3):
    try:
        unreliable_service()
        break
    except TemporaryFailure as e:
        print(f"Retry {attempt + 1}: {e}")
