class ImageGeneratorBase:
    def generate(self, prompt):
        raise NotImplementedError("This method should be overridden by subclasses")