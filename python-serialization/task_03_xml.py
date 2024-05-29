#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary to XML and write it to a file.

    Args:
        dictionary (dict): The dictionary to be serialized.
        filename (str): The name of the file to write
        the XML data to.
    """
    def dict_to_xml(tag, d):
        """
        Convert a dictionary to an XML element.

        Args:
            tag (str): The tag name for the XML element.
            d (dict): The dictionary to be converted.

        Returns:
            xml.etree.ElementTree.Element: The XML
            element representing the dictionary.
        """
        elem = ET.Element(tag)
        for key, val in d.items():
            child = ET.Element(key)
            child.text = str(val)
            elem.append(child)
        return elem

    root = dict_to_xml('data', dictionary)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file and convert it
    to a dictionary.

    Args:
        filename (str): The name of the file containing
        the XML data.

    Returns:
        dict: The dictionary representing the XML data.
    """
    def xml_to_dict(elem):
        """
        Convert an XML element to a dictionary.

        Args:
            elem (xml.etree.ElementTree.Element): The XML
            element to be converted.

        Returns:
            dict: The dictionary representing the XML
            element.
        """
        return {child.tag: child.text for child in elem}

    tree = ET.parse(filename)
    root = tree.getroot()
    return xml_to_dict(root)
