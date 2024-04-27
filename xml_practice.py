import xml.etree.ElementTree as ET

with open('new_payment.xml', 'rb') as f:
    tree = ET.parse(f)
    root = tree.getroot()
    print("root->", root.tag)
    for x in root[0][0].findall('InitgPty'):
        print(x.tag, "=", x[1][0][0][0].text)

    # Updating the text in the XML to some new value
    for data in root.iter():
        print(data.tag, ":", data.text)
        if data.text == "Your Company Name":
            data.text = "Kyriba"

    # Add an attribute to a tag that has the match text
    for data in root.iter():
        if data.text == 'XYZ-12345':
            data.set('attribute_added', "no")
    # Update the text in a tag without iterating through the whole file
    for data in root.iter('MsgId'):
        data.text = "Updated Message Id"
    print(root[0][0])

    #Add a new tag to the XML file
    ET.SubElement(root[0][0], 'new_tag').text = 'This is the value of the new tag'
    ET.indent(tree, space='\t', level=0)
    ET.SubElement(root[0][0], 'new_tag')
    for data in root.iter('new_tag'):
        text = 'This is the value of the new tag'
        data.text = text
        data.attrib = {"name": 'This is the attribute'}
        ET.indent(tree, space='\t', level=0)

    # Delete the tag <CreDtTm> from file
    for data in root.iter('GrpHdr'):
        del data[1]

    # Saving the changes to a new file
    tree.write("new_payment.xml")


