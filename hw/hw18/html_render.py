
class Element (object):

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

        """ Add some new content to the element
        """
        self.content.append(new_content)

    def rander(self, f_new, ind=""):

        """Render the content to the new file like object.
        """
        file_new.write(ind+"<"+self.tag+">\n"+ind+self.indent)
        file_new.write(("\n"+ind+self.indent).join(self.content))
        file_new.write(("\n"+ind+"</"+self.tag+">")







