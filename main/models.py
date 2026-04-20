from django.db import models


class Guruh(models.Model):
    nomi = models.CharField(max_length=100)
    tavsif = models.TextField(blank=True)

    
    rasm = models.ImageField(upload_to='guruhlar/', null=True, blank=True)

    yaratilgan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomi

    def talabalar_soni(self):
        return self.talaba_set.count()

class Talaba(models.Model):
    JINS_CHOICES = [
        ('erkak', 'Erkak'),
        ('ayol', 'Ayol'),
    ]
    ism = models.CharField(max_length=100, verbose_name="Ism")
    familiya = models.CharField(max_length=100, verbose_name="Familiya")
    email = models.EmailField(unique=True, verbose_name="Email")
    telefon = models.CharField(max_length=20, blank=True, verbose_name="Telefon")
    guruh = models.ForeignKey(Guruh, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Guruh")
    tug_sanasi = models.DateField(null=True, blank=True, verbose_name="Tug'ilgan sana")
    jins = models.CharField(max_length=10, choices=JINS_CHOICES, default='erkak', verbose_name="Jins")
    manzil = models.TextField(blank=True, verbose_name="Manzil")
    yaratilgan = models.DateTimeField(auto_now_add=True)
    yangilangan = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"
        ordering = ['familiya', 'ism']

    def __str__(self):
        return f"{self.familiya} {self.ism}"

    def to_liq_ism(self):
        return f"{self.familiya} {self.ism}"
