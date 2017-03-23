# see https://tavianator.com/the-visitor-pattern-in-python/


class Doc(object):
    def accept(self, visitor):
        for element in self.elements:
            element.accept(visitor)


class Text(object):
    def __init__(self, text):
        self.text = text

    def accept(self, visitor):
        visitor.visit(self)


class BoldText(Text):
    pass


class Link(Text):
    def __init__(self, uri, text=None):
        self.uri = uri
        self.text = text


class ToHtml(object):
    def __init__(self):
        self.output = ''

    def visit(self, obj):
        getattr(self, 'visit_obj_' + obj.__class__.__name__.lower())(obj)

    def visit_obj_text(self, obj):
        self.output += '%s' % (obj.text,)

    def visit_obj_boldtext(self, obj):
        self.output += '<b>%s</b>' % (obj.text,)

    def visit_obj_link(self, obj):
        self.output += '<a href="%s">%s</a>' % (obj.uri, obj.text or obj.uri)


class ToText(ToHtml):
    def __init__(self):
        self.output = ''

    def visit_obj_boldtext(self, obj):
        self.output += '*%s*' % (obj.text,)

    def visit_obj_link(self, obj):
        self.output += '[[%s][%s]]' % (obj.uri, obj.text or obj.uri)


doc = Doc()
doc.elements = [Text('plain text'), BoldText('bold text'), Link('amadev.ru')]

html_visitor = ToHtml()
doc.accept(html_visitor)
print html_visitor.output

text_visitor = ToText()
doc.accept(text_visitor)
print text_visitor.output
