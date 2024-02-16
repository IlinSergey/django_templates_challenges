from pytest_django.asserts import assertTemplateUsed

perfomances = [
        {"student_name": "Reed Boles", "week1_completed": False, "week2_completed": False, "week3_completed": False},
        {"student_name": "David Mitchell", "week1_completed": True, "week2_completed": True, "week3_completed": True},
        {"student_name": "Teresa Monger", "week1_completed": False, "week2_completed": False, "week3_completed": True},
        {"student_name": "Doris Dayton", "week1_completed": True, "week2_completed": False, "week3_completed": False},
    ]


def test__students_performance_view(client):
    response = client.get('/students/performance/')
    assert response.status_code == 200
    assert response.context['performances'] == perfomances
    assertTemplateUsed(response, 'level_2/students_performance.html')
