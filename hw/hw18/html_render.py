
class Element(object):
    """ Base class definition web page elements"""
    tag = ''
    indent = '    '

    def __init__(self, content=None, **attributes):
        """Constructor:
            content -- tag content
            attributes -- html tag attributes
        """
        if content is not None:
            self.content = [content]
        else:
            self.content = []
        self.attributes = attributes

    def append(self, new_content):
        """ Add some new content to the element"""
        self.content.append(new_content)

    def render(self, file_new, ind=""):
        """Render the content to the given file like object"""
        file_new.write(ind)
        file_new.write("<%s" % self.tag)
        for key, value in self.attributes.items():
            file_new.write(" %s='%s'" % (key, value))
        file_new.write(">\n")
        for s in self.content:
            if isinstance(s, Element):
                s.render(file_new, ind+self.indent)
            else:
                file_new.write(ind+self.indent+str(s)+"\n")
        file_new.write(ind+"</"+self.tag+">\n")


class OneLineTag(Element):
    """Base class for simple one line tags"""
    def render(self, file_new, ind=""):
        """Render on a single line"""
        file_new.write(ind)
        file_new.write("<%s" % self.tag)
        for key, value in self.attributes.items():
            file_new.write(' %s="%s"' % (key, value))
        file_new.write(">")
        file_new.write(str(self.content[0]))
        file_new.write('</%s>\n' % self.tag)


class SelfClosingTag(Element):
    """Base class for self closing tags"""
    def render(self, file_new, ind=""):
        """Render the content to the given file like object"""
        file_new.write(ind)
        file_new.write("<%s" % self.tag)
        for key, value in self.attributes.items():
            file_new.write(" %s='%s'" % (key, value))
        file_new.write(">\n")


class Html(Element):
    """Implements html tag"""
    tag = "html"

    def render(self, file_new, ind=""):
        """Render the content to the given file like object"""
        file_new.write("<!DOCTYPE html>\n")
        Element.render(self, file_new, ind)


class Body(Element):
    """Implements body tag"""
    tag = "body"


class P(Element):
    """Implements paragraph tag"""
    tag = "p"


class Head(Element):
    """Implements head tag"""
    tag = "h"


class Title(OneLineTag):
    """Implements title tag"""
    tag = "title"


class Hr(SelfClosingTag):
    """Implements hr tag"""
    tag = "hr"


class A(OneLineTag):
    """Implements a tag"""
    tag = "a"

    def __init__(self, link, text, **attributes):
        """Constructor:
            link -- href attribute value
            text --link text
            attributes -- html tag attributes
        """
        super(A, self).__init__(text, href=link, **attributes)


class H(OneLineTag):
    """Implements h tag"""
    def __init__(self, level, content=None, **attributes):
        """Constructor:
            level -- header level
            content -- tag content
            attributes -- html tag attributes
        """
        Element.__init__(self, content, **attributes)

        self.tag = "h%i" % level


class Ul(Element):
    """Implements ul tag"""
    tag = "ul"


class Li(Element):
    """Implements li tag"""
    tag = "li"


class Meta(SelfClosingTag):
    """Implements meta tag"""
    tag = "meta"
