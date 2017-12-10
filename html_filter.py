from html.parser import HTMLParser

available_tags = ['b', 'i', 'img']
available_attrs = ['src']
filtered_html = ''


class HTMLFilter(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global filtered_html
        if tag.lower() in available_tags:
            filtered_html += '<{} '.format(tag)
            for attr in attrs:
                if attr[0].lower() in available_attrs:
                    filtered_html += '{}="{}" '.format(attr[0], attr[1])
            filtered_html += '>'

    def handle_endtag(self, tag):
        global filtered_html
        if tag.lower() in available_tags:
            filtered_html += '</{}>'.format(tag)

    def handle_data(self, data):
        global filtered_html
        filtered_html += data


def filter_html(html_str):
    global filtered_html
    filtered_html = ''
    parser = HTMLFilter()
    parser.feed(html_str)
    return filtered_html
