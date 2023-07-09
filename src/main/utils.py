# from xml.etree import ElementTree
import xmltodict


def convert_xml_to_dict(xml: str or bytes) -> dict:
    # root = ElementTree.fromstring(xml)
    # result = {}
    # for child in root:
    #     result[child.tag] = child.text
    
    result = xmltodict.parse(xml)
    return result
