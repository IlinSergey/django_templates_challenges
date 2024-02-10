from pytest_django.asserts import assertTemplateUsed


def test__registration_view(client):
    response = client.get('/registration/')
    assert response.status_code == 200
    assert response.context['title'] == 'Регистрация'
    assertTemplateUsed(response, 'level_1/registration.html')
