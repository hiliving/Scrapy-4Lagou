from scrapy.exporters import JsonLinesItemExporter


class recodes(JsonLinesItemExporter):

    def __init__(self, file, **kwargs):
        super(recodes,self).__init__(file, ensure_ascii = None)