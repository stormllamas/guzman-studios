from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .serializers import TransactionSerializer
from .models import Transaction


class TransactionAPI(GenericAPIView):
    serializer_class = TransactionSerializer

    def get(self, _, pk=None):
        transaction = get_object_or_404(Transaction, id=pk)

        return Response({
            "id": transaction.id,
            "value": transaction.value,
            "creation_date": transaction.creation_date,
        })
