
class Element(object):
    """ create class of basic web page elements."""
    tag = ''
    indent = '    '

    def __init__(self, content=None, **kwargs):
        if content is not None:
            self.content = [content]
        else:
            self.content = []
        self.kwargs = kwargs

    def append(self, new_content):
        """ add some new content to the element"""
        self.content.append(new_content)

    def render(self, file_new, ind=""):
        """render the content to the given file like object"""
        file_new.write(ind)
        file_new.write("<%s" % self.tag)
        for key, value in self.kwargs.items():
            file_new.write(" %s='%s'" % (key, value))
        file_new.write(">\n")
        for s in self.content:
            if isinstance(s, Element):
                s.render(file_new, ind+self.indent)
            else:
                file_new.write(ind+self.indent+str(s)+"\n")
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


class Head(Element):
    tag = "h"


class Title(Element):
    tag = "title"


class Hr(Element):
    tag = "hr"

    def render(self, file_new, ind=""):
        """render the content to the given file like object"""
        file_new.write(ind)
        file_new.write("<%s" % self.tag)
        for key, value in self.kwargs.items():
            file_new.write(" %s='%s'" % (key, value))
        file_new.write(">\n")

class A(Element):
    tag = "a"
