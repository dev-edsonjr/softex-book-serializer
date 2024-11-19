from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='Nome')
    author = models.CharField(max_length=100, verbose_name='Autor')
    published_date = models.DateField(verbose_name='Data de Publicação')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Preço')
    pages = models.IntegerField(verbose_name='Páginas')
     
    class Meta:
      ordering = ['title']
      verbose_name = 'Livro'
       
    def __str__(self):
      return self.name
     