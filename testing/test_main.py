"""
TEST FUNCTION
"""

import random


def test_get_item(client):
    """
    test_get_item
    :param client:
    :return:
    """
    random_id = random.randint(1, 100)
    url = f"/items/{random_id}/"
    response = client.get(url)
    assert response.status_code == 200
    assert response.json['item']['id'] == random_id


def test_add_product(client):
    """
    test_add_product
    :param client:
    :return:
    """
    url = '/products/add/'
    data = {
        'product-name': 'Test product name'
    }
    response = client.post(url, data=data)
    assert response.status_code == 302
