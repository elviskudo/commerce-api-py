import stripe
from app.config import STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY

def create_checkout_session(data):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': data['product_name'],
                },
                'unit_amount': data['amount'],
            },
            'quantity': data['quantity'],
        }],
        mode='payment',
        success_url=data['success_url'],
        cancel_url=data['cancel_url'],
    )
    return session