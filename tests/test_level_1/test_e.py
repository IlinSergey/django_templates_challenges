from pytest_django.asserts import assertTemplateUsed


def test__admin_page_view(client):
    response = client.get('/admin/')
    assert response.status_code == 200
    assert response.context['is_admin'] is True
    assertTemplateUsed(response, 'level_1/admin_page.html')
