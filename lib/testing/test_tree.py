# test_tree.py
from tree import Tree

def test_get_element_by_id():
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

    assert tree.get_element_by_id('heading') == {
        'tag_name': 'h1',
        'id': 'heading',
        'text_content': 'Title',
        'children': []
    }

    assert tree.get_element_by_id('nope') is None
