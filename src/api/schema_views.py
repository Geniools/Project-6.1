from rest_framework import permissions, views, status
from rest_framework.response import Response
from api.permissions import IsTreasurerIsSuperuserOrReadOnly
from api.schemas.parser import XMLSchemaParser, JSONSchemaParser

from api.serializers import Member


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
