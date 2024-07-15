from django.db import models

# Create your models here.
class Categoria(models.Model):
    id_cate  = models.AutoField(db_column='idCate', primary_key=True) 
    categoria     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.categoria)
    

class Producto(models.Model):
  id_prod = models.CharField(primary_key=True, max_length=10)
  nombre = models.CharField(max_length=20)
  id_cate = models.ForeignKey('Categoria',on_delete=models.CASCADE, db_column='idCate')
  precio = models.CharField(max_length=45)
  descripcion = models.CharField(max_length=50, blank=True, null=True)
  stock = models.CharField(max_length=45)
  imagen = models.ImageField(upload_to='productos/', default='media/default.png')

  def __str__(self):
    return str(self.nombre)+" "+str(self.descripcion)+" "+str(self.precio)+" "+str(self.id_cate)+" "+str(self.stock)
  

class CartItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} - {self.quantity} - {self.price}"