from demoqa_tests.model.data.user import User
from demoqa_tests.model.pages import practice_form


def test_student_registration_form():
    user = User(
        first_name='Pavel',
        last_name='Durov',
        email='durov@mail.ru',
        gender="Male",
        phone='9998887755',
        birthday_month='May',
        birthday_year='1985',
        birthday_day=13,
        subject='English',
        hobby='Sports',
        address='Some address',
        image='resources/durov.jpg',
        state='NCR',
        city='Delhi'
    )

    userForm.fill(user).submit()
    userForm.should_have_registered(user)


userForm = practice_form.UserForm()
