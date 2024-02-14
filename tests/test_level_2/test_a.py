from pytest_django.asserts import assertTemplateUsed

from django_templates_homework.custom_types import Message


def test__message_details_view(client):
    response = client.get('/message/')
    assert response.status_code == 200
    assert response.context['message'] == Message(
        text='почувствуй себя ёжиком',
        author_nickname='bg yellow plum',
        likes_num=3,
        reposts_num=12,
    )
    assertTemplateUsed(response, 'level_2/message_detail.html')
