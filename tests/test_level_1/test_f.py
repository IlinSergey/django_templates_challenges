from pytest_django.asserts import assertTemplateUsed


def test__students_view(client):
    response = client.get('/students/')
    assert response.status_code == 200
    assert response.context['students'] == ['Иван', 'Мария', 'Петр', 'Алексей']
    assertTemplateUsed(response, 'level_1/students.html')
