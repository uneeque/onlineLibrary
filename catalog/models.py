from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Введите жанр книги",
                            verbose_name="Жанр книги")


    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Введите язык книги",
                            verbose_name="язык книги")


    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=20, help_text="Введите имя автора", verbose_name="имя автора")
    last_name = models.CharField(max_length=40, help_text="Введите фамилию автора", verbose_name="фамилия автора")
    day_of_birth = models.DateField(help_text="введите дату рождения автора",
                                    verbose_name="дата рождения автора",
                                    null=True, blank=True)
    day_of_death = models.DateField(help_text="Введите дату смерти автора",
                                    verbose_name="даьа смерти автора",
                                    null=True, blank=True)
    def __str__(self):
        return self.last_name


class Book(models.Model):
    title = models.CharField(max_length=200,
                             help_text="Введите название книги",
                             verbose_name="название книги",)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE,
                              help_text="Введите жанр книги",
                              verbose_name="Жанр книги",
                              null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE,
                                 help_text="Выберите язык Книги",
                                 verbose_name="Язык книги", null=True)
    author = models.ManyToManyField('Author', help_text="Введите автора книги",
                                    verbose_name="Автор Книги")
    summary = models.CharField(max_length=1000, help_text="введите краткое описание книги",
                               verbose_name="Аннотация")
    isbn = models.CharField(max_length=13, help_text="должна содержать 13 символов",
                            verbose_name="ISBN книги")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])


class Status(models.Model):
    name = models.CharField(max_length=20,
                            help_text="введите статус экземпляра книги",
                            verbose_name=" Статус экземпляра книги")

    def __str__(self):
        return self.name


class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    inv_nom = models.CharField(max_length=20, null=True,
                               help_text="введите инвентарный номер экземпляра",
                               verbose_name="Инвентарный номер")
    imprint = models.CharField(max_length=200, help_text="введите издательство и год выпуска",
                               verbose_name="Издательство")
    status = models.ForeignKey('Status', on_delete=models.CASCADE,
                               null=True, help_text="Изменить состояние Экземпляра",
                               verbose_name="Статус экземпляра книги")
    due_back = models.DateField(null=True, blank=True,
                                help_text="Введите конец срока статуса",
                                verbose_name="Дата окончания статуса")

    def __str__(self):
        return '%s %s %s' % (self.inv_nom, self.book, self.status)
