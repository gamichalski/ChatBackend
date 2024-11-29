class verify():


    def verify_pix_data(data):
        if data.get("transaction_amount") <= 0 or data.get("transaction_amount") is None:
            ValueError("transaction amount is required")
        
        if data.get("payer").get("email") is None:
            return ValueError("payer email is required")
        
        if data.get("payer").get("identification") is None:
            return ValueError("payer identification is required")
        
        if data.get("payer").get("identification").get("identificationType") is None:
            return ValueError("payer identification type is required")
        
        if data.get("payer").get("identification").get("number") is None:
            return ValueError("payer identification number is required")
        
        return True
    
    
    def verify_card_data(data):
        if data.get("token") is None:
            return ValueError("token is required")
        
        if data.get("issuer_id") is None:
            return ValueError("issuer_id is required")
        
        if data.get("payment_method_id") is None:
            return ValueError("method_id is required")
        
        if data.get("transaction_amount") <= 0 or data.get("transaction_amount") is None:
            return ValueError("transaction_amount is required")
        
        if data.get("instalments") is None:
            return ValueError("payer email is required")
        
        if data.get("payer").get("email") is None:
            return ValueError("payer email is required")
        
        if data.get("payer").get("identification") is None:
            return ValueError("payer identification is required")
        
        if data.get("payer").get("identification").get("identificationType") is None:
            return ValueError("payer identification type is required")
        
        if data.get("payer").get("identification").get("number") is None:
            return ValueError("payer identification number is required")
        
        return True