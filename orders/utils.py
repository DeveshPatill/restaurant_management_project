from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def is_valid_email(email: str)-> bool:
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False
    except Exception as e:
        print(f"Unexpected error while validating email: {e}")
        return False