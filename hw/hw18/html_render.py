
class Element(object):
    """ create class of basic web page elements."""
    tag = ''
    indent = '    '

    def __init__(self, content=None):
        if content is not None:
            self.content = [content]
        else:
            self.content = []

    def append(self, new_content):
        """ add some new content to the element"""
        self.content.append(new_content)

    def render(self, file_new, ind=""):
        """render the content to the given file like object"""

        file_new.write(ind+"<"+self.tag+">\n")
        for s in self.content:
            if isinstance(s, Element):
                s.render(file_new, ind+self.indent)
            else:
                file_new.write(ind+self.indent+str(s))
        file_new.write(ind+"</"+self.tag+">\n")


class Html(Element):
    tag = "html"

    def render(self, file_new, ind=""):
        file_new.write("<!DOCTYPE html>")
        Element.render(self, file_new, ind)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"
