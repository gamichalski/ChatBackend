import mercadopago
from django.conf import settings

sdk = mercadopago.SDK(settings.MP_ACCESS_TOKEN)

class Payment():

    def validate(data):
        if data.get("payment_method_id") == "pix":
            if data.get("transaction_amount") <= 0 or data.get("payer").get("email") is None or data.get("payer").get("identification") is None or data.get("payer").get("identification").get("identificationType") is None or data.get("payer").get("identification").get("number") is None:
                return False
            else:
                return True
            
        else:
            if data.get("transaction_amount") <= 0 or data.get("payer").get("email") is None or data.get("payer").get("identification") is None or data.get("payer").get("identification").get("identificationType") is None or data.get("payer").get("identification").get("number") is None or data.get("payment_method_id") is None or data.get("token") is None:
                return False
            else:
                return True


    def pix_payment(self, data):
        return


    def card_payment(self, data):
        return 


