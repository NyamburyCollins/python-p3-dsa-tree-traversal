class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        return self._search_by_id(self.root, id)

    def _search_by_id(self, node, target_id):
        if not node:
            return None

        if node.get('id') == target_id:
            return node

        for child in node.get('children', []):
            result = self._search_by_id(child, target_id)
            if result:
                return result

        return None
