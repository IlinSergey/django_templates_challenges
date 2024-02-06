from pytest_django.asserts import assertTemplateUsed


def test__get_phone_number_view(client):
    response = client.get('/about/')
    assert response.status_code == 200
    assert response.context['company_name'] == 'Learn Python'
    assert response.context['work_from_year'] == 2013
    assertTemplateUsed(response, 'level_1/about_us.html')
