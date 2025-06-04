# main.py
from tree import Tree

tree = Tree({
    'tag_name': 'body',
    'id': None,
    'children': [
        {
            'tag_name': 'div',
            'id': 'main',
            'children': [
                {
                    'tag_name': 'h1',
                    'id': 'heading',
                    'text_content': 'Title',
                    'children': []
                },
                {
                    'tag_name': 'h2',
                    'id': None,
                    'text_content': 'Subtitle',
                    'children': []
                }
            ]
        }
    ]
})

print("Looking for ID 'heading':")
print(tree.get_element_by_id('heading'))

print("Looking for ID 'nope':")
print(tree.get_element_by_id('nope'))
