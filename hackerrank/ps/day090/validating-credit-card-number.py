import xml.etree.ElementTree as etree
def get_attr_number(node):
    score = 0
    for child in node.iter():
        score += len(child.attrib)
    return score

if __name__ == '__main__':
    xml = '\n'.join([input() for _ in range(int(input()))])
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))