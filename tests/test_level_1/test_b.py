from pytest_django.asserts import assertTemplateUsed


def test__contact_info_view(client):
    response = client.get('/contacts/')
    assert response.status_code == 200
    assertTemplateUsed(response, 'level_1/contacts_info.html')
