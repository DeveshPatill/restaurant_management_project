from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings 
import logging
from datetime import datetime, time
from django.db.models import Sum
from .models import Order
import secrets, strings


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

    Regards,,
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
    
def is_restaurant_open9:
    now =datetime.now
    current_time = now.time()
    current_day = now.strftime("%A")

    opening_hours ={
        "Monday":(time(9,0), time(22,0)),
        "Tuesday":(time(9,0), time(22,0)),
        "Wednesday":(time(9.0), time(22,0)),
        "Thursday":(time(9,0), time(22,0)),
        "Friday":(time(9,0), time(22,0)),
        "Saturday":(time(9,0), time(22,0)),
        "Sunday":(time(9,0), time(22,0)),
    }
    open_time, close_time = opening_hours[current_day]
    return open_time <= current_time <= close_time

def get_daily_sales_total(date):
    result = Order.objects.filter(created_at__date=date).aggregate(total_sum=Sum('total_price'))
    return result['total_sum'] or 0


def genertae_unique_order_id(length=8):
    characyters = string.ascii_uppercase + string.digits

    while True:
        unique_id = ''.join(secrets.choice(characters)for _ in range(length))
        if not Order.objects.filter(order_id=unique_id).exists():
            return unique_id

