# services/billing.py
import os
import stripe
from flask import request, abort
from api.v1.extensions import db
from api.v1.models.subscription import Subscription

stripe.api_key = os.getenv('STRIPE_API_KEY')

WEBHOOK_SECRET = os.getenv('STRIPE_WEBHOOK_SECRET')


def handle_stripe_webhook():
    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, WEBHOOK_SECRET
        )
    except (ValueError, stripe.error.SignatureVerificationError):
        abort(400)

    # Handle the event types you care about
    if event['type'] == 'invoice.paid':
        data = event['data']['object']
        customer_id = data['customer']
        # Lookup subscription by stripe customer
        sub = Subscription.query.filter_by(
            stripe_customer_id=customer_id).first()
        if sub:
            sub.status = 'active'
            sub.start_date = datetime.utcnow()
            sub.end_date = datetime.utcnow() + timedelta(days=30)
            db.session.commit()
    elif event['type'] == 'invoice.payment_failed':
        data = event['data']['object']
        customer_id = data['customer']
        sub = Subscription.query.filter_by(
            stripe_customer_id=customer_id).first()
        if sub:
            sub.status = 'past_due'
            db.session.commit()
    # Add more event handling as needed

    return {'status': 'success'}
