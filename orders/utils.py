from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings 
import logging

def is_valid_email(email: str)-> bool:
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False
    except Exception as e:
        print(f"Unexpected error while validating email: {e}")
        return False

logger = logging.getLogger(__name__)

def send_order_confirmation_email(order_id, customer_email, customer_name=None):
    subject = f"Order Confirmation - #{order_id}".
    message = f"""
    Hello {customer_name or 'Customer'}, 
    Thankyou for your order!

    Your order ID is {order_id}.
    We will notify you once it has been shipped.

    Regards,
    Your Company Team
    """

    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [customer_email]

    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        logger.info(f"Order confirmation email sent to {customer_email} for order {order_id}")
        return {"success": True, "message":"Email sent succesfully."}
    except BadHeaderError:
        logger.error("Invalid header found while sending order confirmation email.")
        return {"success":False, "message":"Invalid header found."}
    except Exception as e:
        logger.error(f"Error sending order confirmation email: {str(e)}")
        return {"success":False, "message": str(e)}