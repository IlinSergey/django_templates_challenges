from pytest_django.asserts import assertTemplateUsed


def test__transactions_list_view(client):
    response = client.get('/transactions/')
    assert response.status_code == 200
    assert len(response.context['transactions']) == 100
    assertTemplateUsed(response, 'level_2/transactions_list.html')
