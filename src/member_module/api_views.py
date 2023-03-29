from rest_framework import viewsets, permissions

from member_module.serializers import MemberSerializer, LinkedTransactionSerializer
from member_module.models import Member, LinkedTransaction
from base_app.permissions import IsTreasurerOrReadOnly


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticated, IsTreasurerOrReadOnly]


class LinkedTransactionViewSet(viewsets.ModelViewSet):
    queryset = LinkedTransaction.objects.all()
    serializer_class = LinkedTransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsTreasurerOrReadOnly]
