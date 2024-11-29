import mercadopago
from django.conf import settings
from core.payments.utils.verify import verify
from core.payments.models import Payment as PaymentModel

sdk = mercadopago.SDK(settings.MP_ACCESS_TOKEN)

class Payment():
    

    def get_payment(self, payment_id):
        try:
            payment = sdk.payment().get(payment_id)
            return payment
        except Exception as e:
            return e
        
    def update_payment(self, payment_id, data):
        try:
            payment = PaymentModel.objects.get(payment_id=payment_id)
            payment.status = data.get("status")
            payment.save()
            return payment
        except Exception as e:
            return e
    
    def create_payment(self, data):
        try:
            if data.get("payment_method_id") == "pix":
                return self.payment_pix(data)
            else:
                return self.payment_card(data)
        except Exception as e:
            return e
    
    def payment_pix(self, data):
        try:
            verify.verify_pix_data(data)
            payment = sdk.payment().create(data)
            return payment
        except Exception as e:
            return e

    def payment_card(self, data):
        try:
            verify.verify_card_data(data)
            payment = sdk.payment().create(data)
            return payment
        except Exception as e:
            return e