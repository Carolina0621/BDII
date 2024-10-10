from django.db import models

from bases.models import ClaseModelo

class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Categoría',
        unique=True
    )


    def __str__(self): 
        return '{}'.format(self.descripcion)
    
    def save(self):  
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()  

    class Meta:
        verbose_name_plural = 'Categorías'


class subcategoria(ClaseModelo):
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Subcategoría',
        unique=True
    )
    
    def __str__(self):
        return '{}:{}'.format(self.Categoria.descripcion, self.descripcion)
    
    def save(self):  
        self.descripcion = self.descripcion.upper()
        super(subcategoria, self).save() 

    class Meta:
        verbose_name_plural = 'Sub Categorías'
        unique_together = ('Categoria', 'descripcion')


class Marca(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Marca',
        unique=True
    )
    def __str__(self): 
        return '{}'.format(self.descripcion)
    
    def save(self):  
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save()  
    class Meta:
        verbose_name_plural = 'Marca'

class UnidadMedida(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Unidad de Medida',
        unique=True
    )
    def __str__(self): 
        return '{}'.format(self.descripcion)
    
    def save(self):  
        self.descripcion = self.descripcion.upper()
        super(UnidadMedida, self).save()  
    class Meta:
        verbose_name_plural = 'Unidades de Medida'

class Producto(ClaseModelo):
    descripcion = models.CharField(
        max_length=20,
        unique=True
    )

    codigo_barra = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(subcategoria, on_delete=models.CASCADE)

    def __str__(self): 
        return '{}'.format(self.descripcion)
    
    def save(self):  
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save()  
    class Meta:
        verbose_name_plural = 'Productos'
        unique_together = ('codigo', 'codigo_barra')