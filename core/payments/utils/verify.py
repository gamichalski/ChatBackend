class verify():
    def verify_pix_data(data):
        if data.get("transaction_amount") <= 0:
            return False
        if data.get("payer").get("email") is None:
            return False
        if data.get("payer").get("identification") is None:
            return False
        if data.get("payer").get("identification").get("identificationType") is None:
            return False
        if data.get("payer").get("identification").get("number") is None:
            return False
        return True
    
    
    def verify_card_data(data):
        if data.get("transaction_amount") <= 0:
            return False
        if data.get("payer").get("email") is None:
            return False