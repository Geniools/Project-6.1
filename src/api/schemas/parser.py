import json
import jsonschema
import io

from jsonschema import Draft7Validator
from lxml import etree

from django.conf import settings
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser
from rest_framework_xml.parsers import XMLParser


class XMLSchemaParser(XMLParser):
    XML_SCHEMA = settings.BASE_DIR / "api/schemas/member-schema.xsd"
    
    def __init__(self):
        super().__init__()
        # Get the schema for xml (XSD)
        xsd_tree = etree.parse(self.XML_SCHEMA)
        self.xmlschema = etree.XMLSchema(xsd_tree)
    
    def parse(self, stream, media_type=None, parser_context=None):
        """
        Parses the incoming bytestream as XML and returns the resulting data.
        Moreover, it validates the xml against a pre-defined schema.
        """
        
        # Normally, the actual parsing is done by the parent class, which returns a dict
        # data = super().parse(stream, media_type, parser_context)
        
        # But we want to parse the xml against the schema first
        stream_copy = io.BytesIO(stream.read())  # First, make a copy of the stream, because we need to read it twice
        try:
            tree = etree.parse(stream_copy)
            self.xmlschema.assertValid(tree)
        except etree.XMLSyntaxError as e:
            raise ParseError('Malformed XML. %s' % e)
        except etree.DocumentInvalid as e:
            raise ParseError('Invalid XML. %s' % e)
        
        # If the xml is valid, we can parse it
        data = super().parse(stream_copy, media_type, parser_context)
        return data


class JSONSchemaParser(JSONParser):
    JSON_SCHEMA = settings.BASE_DIR / "api/schemas/member-schema.json"
    
    def __init__(self):
        super().__init__()
        # Get the schema for json (JSON Schema)
        with open(self.JSON_SCHEMA) as json_file:
            self.schema_json = json.load(json_file)
    
    def parse(self, stream, media_type=None, parser_context=None):
        """
        Parses the incoming bytestream as JSON and returns the resulting data.
        Moreover, it validates the json against a pre-defined schema.
        """
        
        # Normally, the actual parsing is done by the parent class, which returns a dict
        data = super().parse(stream, media_type, parser_context)
        
        # Then we validate the json against the schema
        try:
            Draft7Validator(self.schema_json).validate(data)
        except jsonschema.exceptions.ValidationError as ex:
            raise ParseError('Malformed JSON. %s' % ex)
        
        return data
