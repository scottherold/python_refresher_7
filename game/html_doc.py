class Tag(object):
    """A class that represents the composition of a HTML tag
    
    Attributes:
        start_tag (str): The name of the opening tag.
        end_tag (str): The name of the closing tag.
        contents (str): The tag's contents

    Methods:
        display: Prints the opening and closing tag, with the enclosed
        contents.
    """

    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file):
        print(self, file=file)


class DocType(Tag):
    """A subclass of Tag that represents the HTML document type notation"""

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = '' # DOCTYPE doesn't have an end tag


class Head(Tag):
    """A subclass of Tag that represents the HTML head tag
    
    Attributes:
        title_tag (str): The title tag within a Header tag in a HTML document
    """

    def __init__(self, title=None):
        super().__init__('head', '')
        if title:
            self._title_tag = Tag('title', title)
            self.contents = str(self._title_tag)


class Body(Tag):
    """A subclass of Tag that represents the HTML body tag
    
    Attributes:
        body_contents (list): A list of tags that make up the HTML body

    Methods:
        add_tag: Adds a new HTML tag to the body_contents attribute
        display: Overrides Tag display method to concantenate all tags in
        body_contents before printing.
    """

    def __init__(self):
        super().__init__('body', '') # body contents will be built seperately
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file):
        # body_contents must be concatenated before displayed
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)


class HtmlDoc(object):
    """A class representing a HTML web page
    
    Attributes:
        doc_type (DocType): The doctype tag of the document
        head (Head): The head tag of the document
        body (Body): The body tag of the document

    Methods:
        add_tag: delegates the Body class's add_tag method to add additional
        tags to the HTML document (in the document's body)
        display: delegates to the Head and Body class' methods to display the
        tags contained within them.
    """

    def __init__(self, title=None):
        self._doc_type=DocType()
        self._head = Head(title)
        self._body = Body()

    def add_tag(self, name, contents):
            self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)

# only runs if not imported
if __name__ == '__main__':
    my_page = HtmlDoc('Demo HTML Document')
    my_page.add_tag('h1', 'Main heading')
    my_page.add_tag('h2', 'sub-heading')
    my_page.add_tag('p', 'This is a paragraph that will appear on the page')
    with open('test.html', 'w') as test_doc:
        my_page.display(file=test_doc)