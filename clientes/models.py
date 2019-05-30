from django.db import models

class Documento(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc

class Person(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Nome Verbose', help_text="Preencha seu nome")
    last_name = models.CharField(max_length=100, verbose_name='Sobrenome')
    age = models.IntegerField(verbose_name='Idade')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Salário')
    bio = models.TextField(verbose_name='Biografia')
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True,verbose_name='Imagem')
    doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Documento')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def nome_completo(self):
        return self.first_name + ' ' + self.last_name

class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.descricao

class Venda(models.Model):
    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    desconto = models.DecimalField(max_digits=5, decimal_places=2)
    impostos = models.DecimalField(max_digits=5, decimal_places=2)
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)

    # 05 Tecnicas de Refactor
    # produtos = models.ManyToManyField(Produto, blank=True)

    nfe_emitida = models.BooleanField(default=False)

    def __str__(self):
        return self.numero

    '''
    def get_total(self):
        tot = 0
        for produto in self.produtos.all():
            tot += produto.preco

        return (tot -self.desconto) - self.impostos
    '''

class ItensDoPedido(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade =  models.FloatField(verbose_name='Quantidade')
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.venda.numero + ' - ' + self.produto.descricao

