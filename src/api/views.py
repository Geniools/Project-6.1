from rest_framework import viewsets, permissions, mixins, views, status
from rest_framework.response import Response

from api.permissions import IsTreasurerIsSuperuserOrReadOnly
from api.serializers import *
from api.schemas.parser import XMLSchemaParser, JSONSchemaParser


# ViewSets templates
class CreateAndListOnlyViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    pass


class UpdateAndListOnlyViewSet(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    pass


# The following endpoint is used only to demonstrate validation of json and xml data using schemas
class MemberSchemaValidatorView(views.APIView):
    """
    View to demonstrate validation of json and xml data using schemas.
    """
    permission_classes = [permissions.IsAuthenticated, IsTreasurerIsSuperuserOrReadOnly]
    parser_classes = [XMLSchemaParser, JSONSchemaParser]
    
    def post(self, request, format=None):
        # print(request.data)
        
        data = {
            'detail': 'Error message',
        }
        
        # Remove the id from the data, because it is not needed for creation
        del request.data['id']
        member = Member(**request.data)
        try:
            # First validate the data
            member.full_clean()
            # Then save it
            member.save()
        except Exception as e:
            data['detail'] = str(e)
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_201_CREATED)
    
    def put(self, request, pk=None):
        # print(request.data)
        
        data = {
            'detail': 'Error! You have probably not specified an id for the member!',
        }
        
        try:
            # Update the member
            member = Member.objects.get(id=request.data['id'])
            # Remove the id from the data, because it is not needed for creation
            del request.data['id']
            for key, value in request.data.items():
                setattr(member, key, value)
            # First validate the data
            member.full_clean()
            # Then save it
            member.save()
        except KeyError as err:
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            data['detail'] = str(e)
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_200_OK)


# Base app
class TransactionViewSet(UpdateAndListOnlyViewSet):
    # API endpoint that allows transactions to be viewed or updated.
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsTreasurerIsSuperuserOrReadOnly]


class FileViewSet(viewsets.ReadOnlyModelViewSet):
    # API endpoint that allows files (mt940 files) to be viewed
    queryset = File.objects.all().order_by('-registration_time')
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated, IsTreasurerIsSuperuserOrReadOnly]


class CategoryViewSet(CreateAndListOnlyViewSet):
    # API endpoint that allows categories to be viewed or created.
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsTreasurerIsSuperuserOrReadOnly]


class CurrencyViewSet(CreateAndListOnlyViewSet):
    # API endpoint that allows currencies to be viewed or created.
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticated, IsTreasurerIsSuperuserOrReadOnly]


class BalanceDetailsViewSet(viewsets.ReadOnlyModelViewSet):
    # API endpoint that allows balance details to be viewed.
    queryset = BalanceDetails.objects.all()
    serializer_class = BalanceDetailsSerializer
    permission_classes = [permissions.IsAuthenticated, IsTreasurerIsSuperuserOrReadOnly]


# Cash module
class CashTransactionViewSet(CreateAndListOnlyViewSet):
    # API endpoint that allows users to be viewed or edited.
    queryset = CashTransaction.objects.all()
    serializer_class = CashTransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsTreasurerIsSuperuserOrReadOnly]


# Member module
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all().order_by('-email')
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticated, IsTreasurerIsSuperuserOrReadOnly]


class LinkedTransactionViewSet(CreateAndListOnlyViewSet):
    queryset = LinkedTransaction.objects.all()
    serializer_class = LinkedTransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsTreasurerIsSuperuserOrReadOnly]
