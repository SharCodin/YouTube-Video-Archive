class MyWorkflows:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": { "image_in" : ("IMAGE", {}) },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("IMAGE",)
    CATEGORY = "examples"
    FUNCTION = "test"

    def test(self, image_in):
        return image_in


NODE_CLASS_MAPPINGS = {
    "MyWorkflows" : MyWorkflows,
}


NODE_DISPLAY_NAME_MAPPINGS = {
    "MyWorkflows": "Sharvin's Node"
}
