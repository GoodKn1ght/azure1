from django.test import TestCase
from .models import User, Person, Extract, Operation_Olap, Operation, Analitics, Employee
from django.utils.timezone import make_aware
from datetime import datetime
class UserModelTest(TestCase):
    def test_string_representation(self):
        user = User(Terms_Of_Use='Terms Example', Hashed_Password='123abc', Mother_Surname='Smith')
        self.assertEqual(str(user.Terms_Of_Use), 'Terms Example')

    def test_default_money_left(self):
        user = User.objects.create(Terms_Of_Use='Terms Example', Hashed_Password='123abc', Mother_Surname='Smith')
        self.assertEqual(user.Money_Left, 0.0)
class PersonModelTest(TestCase):
    def test_string_representation(self):
        person = Person(Phone_Number='+123456789', Documents='Passport', Email='test@example.com')
        self.assertEqual(str(person.Email), 'test@example.com')

    def test_email_format(self):
        person = Person.objects.create(Phone_Number='+123456789', Documents='ID Card', Email='invalid-email')
        self.assertFalse('@' in person.Email)
class ExtractModelTest(TestCase):
    def test_string_representation(self):
        extract = Extract(Operation_Type='Withdrawal', Money_Used=100.50)
        self.assertEqual(str(extract.Operation_Type), 'Withdrawal')

class OperationModelTest(TestCase):
    def test_processing_stage(self):
        user = User.objects.create(Terms_Of_Use='Terms Example', Hashed_Password='123abc', Mother_Surname='Smith')
        time_completed = make_aware(datetime(2024, 12, 9))
        operation = Operation.objects.create(
            Operation_Type="Withdrawal",
            User_ID=user,
            Money_Used=200,
            Time_Completed=time_completed,
            Proccessing_Stage="In Progress"
        )
        self.assertEqual(operation.Proccessing_Stage, "In Progress")

class AnaliticsModelTest(TestCase):
    def test_impact_defaults(self):
        analytics = Analitics.objects.create(month_year="12-2024", total_spending=3000)
        self.assertEqual(analytics.total_impact_from_employees, 0.0)
        self.assertEqual(analytics.total_impact_from_users, 0.0)
class EmployeeModelTest(TestCase):
    def test_default_employee_position(self):
        employee = Employee.objects.create(Year_Enrolled=2022, Position="Manager", Office="Kyiv")
        self.assertEqual(employee.Position, "Manager")