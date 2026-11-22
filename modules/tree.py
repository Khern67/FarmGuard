class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

class FarmTree:
    """Simple hierarchy: farm -> crop -> section."""
    def __init__(self, farm_name="Farm"):
        self.root = TreeNode(farm_name)

    def add_path(self, crop_name, section):
        crop = next((n for n in self.root.children if n.value == crop_name), None)
        if crop is None:
            crop = TreeNode(crop_name)
            self.root.add_child(crop)
        if not any(n.value == section for n in crop.children):
            crop.add_child(TreeNode(section))

    def preorder(self):
        result = []
        def visit(node, depth=0):
            result.append((depth, node.value))
            for child in node.children:
                visit(child, depth + 1)
        visit(self.root)
        return result
