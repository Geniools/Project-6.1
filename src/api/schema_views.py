from rest_framework import permissions, views, status
from rest_framework.response import Response
from api.permissions import IsTreasurerIsSuperuserOrReadOnly
from api.schemas.parser import XMLSchemaParser, JSONSchemaParser

from api.serializers import Member

from api.schemas import SCHEMA_ROOT


# An abstract class that is used to validate json and xml data using schemas
class SchemaValidatorView(views.APIView):
    """
        View to demonstrate validation of json and xml data using schemas.
    """
    
    permission_classes = [permissions.IsAuthenticated, IsTreasurerIsSuperuserOrReadOnly]
    parser_classes = [XMLSchemaParser, JSONSchemaParser]
    
    def __init__(self, xml_schema, json_schema):
        # First change the schema for xml
        XMLSchemaParser.XML_SCHEMA = xml_schema
        # Then change the schema for json
        JSONSchemaParser.JSON_SCHEMA = json_schema
        super().__init__()
    
    def post(self, request, format=None):
        print(request.data)
        # If the data is valid, and the schema validation passes, the view will return a default 201 CREATED response.
        
        # TODO: The child classes should override this method, and implement the creation of the object
        return Response(status=status.HTTP_201_CREATED)
    
    def put(self, request, pk=None):
        print(request.data)
        # If the data is valid, and the schema validation passes, the view will return a default 200 OK response.
        
        # TODO: The child classes should override this method, and implement the update of the object
        return Response(status=status.HTTP_200_OK)


# All the following classes are used to demonstrate validation of json and xml data using schemas, and must inherit from SchemaValidatorView

class MemberSchemaValidatorView(SchemaValidatorView):
    def __init__(self):
        # First change the schema for xml
        xml_schema = SCHEMA_ROOT / "xsd/member-schema.xsd"
        # Then change the schema for json
        json_schema = SCHEMA_ROOT / "json/member-schema.json"
        super().__init__(xml_schema, json_schema)
    
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


class BalanceDetailsSchemaValidator(SchemaValidatorView):
    def __init__(self):
        # First change the schema for xml
        xml_schema = SCHEMA_ROOT / "xsd/balanceDetails-schema.xsd"
        # Then change the schema for json
        json_schema = SCHEMA_ROOT / "json/balanceDetails-schema.json"
        super().__init__(xml_schema, json_schema)


class CashSchemaValidator(SchemaValidatorView):
    def __init__(self):
        # First change the schema for xml
        xml_schema = SCHEMA_ROOT / "xsd/cash-schema.xsd"
        # Then change the schema for json
        json_schema = SCHEMA_ROOT / "json/cash-schema.json"
        super().__init__(xml_schema, json_schema)


class CategorySchemaValidator(SchemaValidatorView):
    def __init__(self):
        # First change the schema for xml
        xml_schema = SCHEMA_ROOT / "xsd/category-schema.xsd"
        # Then change the schema for json
        json_schema = SCHEMA_ROOT / "json/category-schema.json"
        super().__init__(xml_schema, json_schema)


class CurrencySchemaValidator(SchemaValidatorView):
    def __init__(self):
        # First change the schema for xml
        xml_schema = SCHEMA_ROOT / "xsd/currency-schema.xsd"
        # Then change the schema for json
        json_schema = SCHEMA_ROOT / "json/currency-schema.json"
        super().__init__(xml_schema, json_schema)


class FileSchemaValidator(SchemaValidatorView):
    def __init__(self):
        # First change the schema for xml
        xml_schema = SCHEMA_ROOT / "xsd/file-schema.xsd"
        # Then change the schema for json
        json_schema = SCHEMA_ROOT / "json/file-schema.json"
        super().__init__(xml_schema, json_schema)


class TransactionSchemaValidator(SchemaValidatorView):
    def __init__(self):
        # First change the schema for xml
        xml_schema = SCHEMA_ROOT / "xsd/transaction-schema.xsd"
        # Then change the schema for json
        json_schema = SCHEMA_ROOT / "json/transaction-schema.json"
        super().__init__(xml_schema, json_schema)
