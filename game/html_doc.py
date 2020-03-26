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

    def display(self):
        print(self)


class DocType(Tag):
    """A subclass of Tag that represents the HTML document type notation"""

    def __init__(self):
        super().__init__('1DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = '' # DOCTYPE doesn't have an end tag


class Head(Tag):
    """A subclass of Tag that represents the HTML head tag"""

    def __init__(self):
        super().__init__('head', '')


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

    def display(self):
        # body_contents must be concatenated before displayed
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display()
