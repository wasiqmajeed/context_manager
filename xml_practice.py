import xml.etree.ElementTree as ET

with open('payment.xml', 'rb') as f:
    tree = ET.parse(f)
    root = tree.getroot()
    # print("root->", root.tag)
    # for x in root[0][0].findall('InitgPty'):
    #     print(x.tag, "=", x[1][0][0][0].text)

    # Updating the text in the XML to some new value
    for data in root.iter():
        print(data.tag, ":", data.text)
        if data.text == "Your Company Name":
            data.text = "Kyriba"
    # Saving the changes to a new file
    tree.write("new_payment.xml")


