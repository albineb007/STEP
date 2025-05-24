import os
import django
from typing import List, Tuple
from django.utils import timezone
from faker import Faker
from factory.django import DjangoModelFactory
from factory import SubFactory, LazyAttribute, Iterator
from django_extensions.management.commands import runscript

# Set up Django environment
import sys
import os
import django

# Adjust sys.path to include project root for config module import
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
django.setup()

from accounts.models import User, Student, Parent, DepartmentHead, LEVEL, RELATION_SHIP
from course.models import Program, Course
from quiz.models import Quiz

# Use Indian locale for Faker to generate Indian names
fake = Faker('en_IN')

class UserFactory(DjangoModelFactory):
    """
    Factory for creating User instances with optional flags.
    """
    class Meta:
        model = User

    username: str = LazyAttribute(lambda x: fake.user_name())
    first_name: str = LazyAttribute(lambda x: fake.first_name())
    last_name: str = LazyAttribute(lambda x: fake.last_name())
    email: str = LazyAttribute(lambda x: fake.email())
    date_joined: timezone.datetime = timezone.now()
    phone: str = LazyAttribute(lambda x: fake.phone_number())
    address: str = LazyAttribute(lambda x: fake.address())
    is_student: bool = False
    is_lecturer: bool = False
    is_parent: bool = False
    is_dep_head: bool = False
    password: str = "defaultpassword123"

    @classmethod
    def _create(cls, model_class: type, *args, **kwargs) -> User:
        password = kwargs.pop('password', None) or cls.password
        user: User = super()._create(model_class, *args, **kwargs)
        user.set_password(password)
        if cls.is_student:
            user.is_student = True
        elif cls.is_parent:
            user.is_parent = True
        elif cls.is_lecturer:
            user.is_lecturer = True
        user.save()
        return user

class LecturerFactory(DjangoModelFactory):
    """
    Factory for creating Lecturer users.
    """
    class Meta:
        model = User

    username: str = LazyAttribute(lambda x: fake.user_name())
    first_name: str = LazyAttribute(lambda x: fake.first_name())
    last_name: str = LazyAttribute(lambda x: fake.last_name())
    email: str = LazyAttribute(lambda x: fake.email())
    date_joined: timezone.datetime = timezone.now()
    phone: str = LazyAttribute(lambda x: fake.phone_number())
    address: str = LazyAttribute(lambda x: fake.address())
    is_lecturer: bool = True

class ProgramFactory(DjangoModelFactory):
    class Meta:
        model = Program

    title: str = LazyAttribute(lambda x: fake.sentence(nb_words=3))
    summary: str = LazyAttribute(lambda x: fake.text())

    @classmethod
    def _create(cls, model_class: type, *args, **kwargs) -> Program:
        program, created = Program.objects.get_or_create(title=kwargs.get("title"), defaults=kwargs)
        return program

class CourseFactory(DjangoModelFactory):
    class Meta:
        model = Course

    title: str = LazyAttribute(lambda x: fake.sentence(nb_words=3))
    program: Program = SubFactory(ProgramFactory)

class QuizFactory(DjangoModelFactory):
    class Meta:
        model = Quiz

    title: str = LazyAttribute(lambda x: fake.sentence(nb_words=3))
    course: Course = SubFactory(CourseFactory)

class StudentFactory(DjangoModelFactory):
    class Meta:
        model = Student

    student: User = SubFactory(UserFactory, is_student=True)
    level: str = Iterator([choice[0] for choice in LEVEL])
    program: Program = SubFactory(ProgramFactory)

class ParentFactory(DjangoModelFactory):
    class Meta:
        model = Parent

    user: User = SubFactory(UserFactory, is_parent=True)
    student: Student = SubFactory(StudentFactory)
    first_name: str = LazyAttribute(lambda x: fake.first_name())
    last_name: str = LazyAttribute(lambda x: fake.last_name())
    phone: str = LazyAttribute(lambda x: fake.phone_number())
    email: str = LazyAttribute(lambda x: fake.email())
    relation_ship: str = Iterator([choice[0] for choice in RELATION_SHIP])

def generate_fake_accounts_data() -> None:
    programs: List[Program] = ProgramFactory.create_batch(2)
    courses: List[Course] = CourseFactory.create_batch(2)
    quizzes: List[Quiz] = QuizFactory.create_batch(2)
    lecturers: List[User] = LecturerFactory.create_batch(10)
    students: List[Student] = StudentFactory.create_batch(10)
    parents: List[Parent] = ParentFactory.create_batch(10)

    print(f"Created {len(programs)} programs.")
    print(f"Created {len(courses)} courses.")
    print(f"Created {len(quizzes)} quizzes.")
    print(f"Created {len(lecturers)} lecturers.")
    print(f"Created {len(students)} students.")
    print(f"Created {len(parents)} parents.")

generate_fake_accounts_data()

