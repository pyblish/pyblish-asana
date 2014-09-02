import pyblish.backend.plugin


class ConformWithAsana(pyblish.backend.plugin.Conform):
    def process(self, context):
        yield None, None
