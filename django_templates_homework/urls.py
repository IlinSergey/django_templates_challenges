from django.urls import path

from django_templates_homework.views.level_1.a_phone_number import \
    get_phone_number_view
from django_templates_homework.views.level_1.b_contacts_info import \
    contacts_info_view
from django_templates_homework.views.level_1.c_registration import \
    registration_view
from django_templates_homework.views.level_1.d_about_us import about_us_view
from django_templates_homework.views.level_1.e_admin_page import \
    admin_page_view
from django_templates_homework.views.level_1.f_students import students_view
from django_templates_homework.views.level_2.a_message_page import \
    message_details_view
from django_templates_homework.views.level_2.b_student_performance import \
    students_performance_view
from django_templates_homework.views.level_2.c_transactions_list import \
    transactions_list_view
from django_templates_homework.views.level_2.d_tasks_board import \
    tasks_board_view

urlpatterns = [
    # level 1
    path('phone-number/', get_phone_number_view),
    path('contacts/', contacts_info_view),
    path('registration/', registration_view),
    path('about/', about_us_view),
    path('admin/', admin_page_view),
    path('students/', students_view),

    # level 2
    path('message/', message_details_view),
    path('students/performance/', students_performance_view),
    path('transactions/', transactions_list_view),
    path('tasks/', tasks_board_view),
]
