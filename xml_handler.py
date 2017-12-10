import xml.etree.cElementTree as Et


def get_root():
    try:
        root = Et.parse('reviews.xml').getroot()
    except FileNotFoundError:
        root = Et.Element('reviews')
    return root


def add_review_to_root(node, author_name, review):
    Et.SubElement(node, "review", name=author_name).text = review


def get_all_reviews():
    root = get_root()
    dic_reviews = {}
    reviews = []
    for child in root:
        reviews.append((child.attrib['name'], child.text))
    dic_reviews['reviews'] = reviews
    return dic_reviews


def write(root):
    tree = Et.ElementTree(root)
    tree.write('reviews.xml', encoding='utf-8', xml_declaration=True)



