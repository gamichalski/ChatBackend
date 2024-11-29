class verify():


    def verify_pix_data(data):
        if int(data.get("transaction_amount", 0)) <= 0:
            raise ValueError("transaction amount is required")

        if data.get("payer_email") is None:
            raise ValueError("payer email is required")

        payer = data.get("payer")

        if data.get("payer_identification_type") is None:
            print(data.get("payer_identification_type"))
            raise ValueError("payer identification type is required")

        if data.get("payer_identification_number") is None:
            print(data.get("payer_identification_number"))
            raise ValueError("payer identification number is required")

        return True

    def verify_card_data(data):
        if data.get("token") is None:
            raise ValueError("token is required")

        if data.get("issuer_id") is None:
            raise ValueError("issuer_id is required")

        if data.get("payment_method_id") is None:
            raise ValueError("method_id is required")

        if int(data.get("transaction_amount", 0)) <= 0:
            raise ValueError("transaction_amount is required")

        if data.get("instalments") is None:
            raise ValueError("instalments is required")

        payer = data.get("payer")
        if payer is None:
            raise ValueError("payer email is required")

        if payer.get("email") is None:
            raise ValueError("payer email is required")

        if payer.get("identification") is None:
            raise ValueError("payer identification is required")

        identification = payer.get("identification")
        if identification is None or identification.get("identificationType") is None:
            raise ValueError("payer identification type is required")

        if identification.get("number") is None:
            raise ValueError("payer identification number is required")

        return True
