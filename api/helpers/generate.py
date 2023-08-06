"""generate data for the frontend"""


def generate_data(neurons):
    """generate data for the frontend"""
    try:
        print("neurons", neurons)

        data = {
            "nodes": [
                {"data": {"id": "a"}},
                {"data": {"id": "b", "parent": "parent"}},
                {"data": {"id": "c", "parent": "parent"}},
                {"data": {"id": "d"}},
                {"data": {"id": "e"}},
                {"data": {"id": "parent"}},
            ],
            "edges": [
                {"data": {"id": "ab", "source": "a", "target": "b"}},
                {"data": {"id": "bc", "source": "b", "target": "d"}},
                {"data": {"id": "cd", "source": "c", "target": "a"}},
                {"data": {"id": "de", "source": "d", "target": "e"}},
                {"data": {"id": "ea", "source": "e", "target": "a"}},
            ],
        }

        return data

    # pylint: disable=broad-except
    except Exception as error:
        return error
