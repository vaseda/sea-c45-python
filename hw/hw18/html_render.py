
class element (object):

    """ Create an Element class for rendering an html element.
    """
    tag = 'html'
    intend = '    '

    def __init__(self, content=None):
        if content is not None:
            self.content = [str(content)]
        else:
            self.content = []

    def append(self, new_content):

        """ Add some new content to the element.
        """
        self.content.append(new_content)

    def rander(self, f_new, ind=""):

        """Render the content to the new file like object.
        """
        file_new.write(ind+"<"+self.tag+">\n"+ind+self.indent)
        file_new.write(("\n"+ind+self.indent).join(self.content))
        file_new.write(("\n"+ind+"</"+self.tag+">")

# body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text"))

# body.append(hr.P(u"And here is another piece of text -- you should be able to add any number"))

# page.append(body)

# render(page, u"test_html_output2.html")



class body (element):

    """Create subclass of Element class, for <body> tag.
    """
    tag='body'
    intend='    '

    def __init__(self, content=None):
        if content is not None:
            self.content=[str(content)]
        else:
            self.content=[]


    def append(self, new_content):
            self.content.append(new_content)
    """ Add some new content to the body.
    """
        self.content.append(new_content)

    def rander(self, f_new, ind=""):

        """Render the content to the new file like object.
        """
        file_new.write(ind+"<body>"+self.tag+">\n"+ind+self.indent)
        file_new.write(("\n"+ind+self.indent).join(self.content))
        file_new.write(("\n"+ind+"</"+self.tag+">")      


class paragraph (element):

    """Create subclass of Element, for < paragraph > tag.
    """
    tag='p'
    intend='    '

    def __init__(self,):

    """Render the content to the new file like object.
    """
        file_new.write(ind+"<html>"+self.tag+">\n"+ind+self.indent)
        file_new.write(("\n"+ind+self.indent).join(self.content))
        file_new.write(("\n"+ind+"</"+self.tag+">")        


