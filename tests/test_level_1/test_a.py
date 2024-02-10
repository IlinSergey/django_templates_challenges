from pytest_django.asserts import assertTemplateUsed


def test__get_phone_number_view(client):
    response = client.get('/phone-number/')
    assert response.status_code == 200
    assert response.context['phone_number'] == '+79848522383'
    assertTemplateUsed(response, 'level_1/phone_number.html')
