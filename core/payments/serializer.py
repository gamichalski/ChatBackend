from rest_framework import serializers
from core.payments.models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'id',
            'payment_id',
            'user',
            'transaction_amount',
            'created_at',
            'updated_at',
            'date_expiration',
            'qrcode_key',
            'status',
            'ticket_url',
            'instalments',
        ]
        read_only_fields = ["id", "payment_id", "status", "qrcode_key", "created_at", "updated_at", "date_expiration", "ticket_url"]