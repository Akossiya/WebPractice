from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=200)
    company_description = models.TextField(default='')
    company_city = models.CharField(max_length=200)
    company_address = models.TextField(default='')

    def to_json(self):
        return {
            'company_name': self.company_name,
            'company_description': self.company_description,
            'company_city': self.company_city,
            'company_address': self.company_address,
        }


class Vacancy(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    vacancy_name = models.CharField(max_length=200)
    vacancy_description = models.TextField(default='')
    vacancy_salary = models.FloatField()

    def to_json(self):
        return {
            'id': self.id,
            'vacancy_name': self.vacancy_name,
            'vacancy_description': self.vacancy_description,
            'vacancy_salary': self.vacancy_salary
        }
