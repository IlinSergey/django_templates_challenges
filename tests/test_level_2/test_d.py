from pytest_django.asserts import assertTemplateUsed


def test__tasks_board_view(client):
    response = client.get('/tasks/')
    assert response.status_code == 200
    assert len(response.context['tasks']) == 6
    assertTemplateUsed(response, 'level_2/tasks_board.html')
