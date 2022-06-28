from django.db import models


class Mega_sena_concurso(models.Model):
    id_concurso = models.BigIntegerField(unique=True)
    data = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['id_concurso']),
            models.Index(fields=['data']),
        ]

    def __str__(self):
        return "Concurso: " + str(self.id_concurso)


class Mega_sena_valores(models.Model):
    v1 = models.IntegerField()
    v2 = models.IntegerField()
    v3 = models.IntegerField()
    v4 = models.IntegerField()
    v5 = models.IntegerField()
    v6 = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    id_concurso = models.OneToOneField(
        Mega_sena_concurso, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['id_concurso']),
        ]

    def __str__(self):
        return "Valores do Conurso: "+ str(self.id_concurso)


class single_value_mega_sena(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    v1 = models.IntegerField()
    quantidade = models.BigIntegerField()
    media_frequencia = models.IntegerField()
    ultimo_concurso = models.BigIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    concursos = models.ManyToManyField(
        Mega_sena_concurso, through='single_Mega_sena_concurso')

    class Meta:
        indexes = [
            models.Index(fields=['v1']),
            models.Index(fields=['media_frequencia']),
        ]


class single_Mega_sena_concurso(models.Model):
    concurso = models.ForeignKey(Mega_sena_concurso, on_delete=models.CASCADE)
    value = models.ForeignKey(
        single_value_mega_sena, on_delete=models.RESTRICT)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class double_value_mega_sena(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    v1 = models.IntegerField()
    v2 = models.IntegerField()
    quantidade = models.BigIntegerField()
    media_frequencia = models.IntegerField()
    ultimo_concurso = models.BigIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    concursos = models.ManyToManyField(
        Mega_sena_concurso, through='double_Mega_sena_concurso')

    class Meta:
        indexes = [
            models.Index(fields=['v1', 'v2']),
            models.Index(fields=['media_frequencia']),
        ]


class double_Mega_sena_concurso(models.Model):
    concurso = models.ForeignKey(Mega_sena_concurso, on_delete=models.CASCADE)
    value = models.ForeignKey(
        double_value_mega_sena, on_delete=models.RESTRICT)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class triple_value_mega_sena(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    v1 = models.IntegerField()
    v2 = models.IntegerField()
    v3 = models.IntegerField()
    quantidade = models.BigIntegerField()
    media_frequencia = models.IntegerField()
    ultimo_concurso = models.BigIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    concursos = models.ManyToManyField(
        Mega_sena_concurso, through='triple_Mega_sena_concurso')

    class Meta:
        indexes = [
            models.Index(fields=['v1', 'v2', 'v3']),
            models.Index(fields=['media_frequencia']),
        ]


class triple_Mega_sena_concurso(models.Model):
    concurso = models.ForeignKey(Mega_sena_concurso, on_delete=models.CASCADE)
    value = models.ForeignKey(
        triple_value_mega_sena, on_delete=models.RESTRICT)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class quadruple_value_mega_sena(models.Model):
    id = models.CharField(max_length=11, primary_key=True)
    v1 = models.IntegerField()
    v2 = models.IntegerField()
    v3 = models.IntegerField()
    v4 = models.IntegerField()
    quantidade = models.BigIntegerField()
    media_frequencia = models.IntegerField()
    ultimo_concurso = models.BigIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    concursos = models.ManyToManyField(
        Mega_sena_concurso, through='quadruple_Mega_sena_concurso')

    class Meta:
        indexes = [
            models.Index(fields=['v1', 'v2', 'v3', 'v4']),
            models.Index(fields=['media_frequencia']),
        ]


class quadruple_Mega_sena_concurso(models.Model):
    concurso = models.ForeignKey(Mega_sena_concurso, on_delete=models.CASCADE)
    value = models.ForeignKey(
        quadruple_value_mega_sena, on_delete=models.RESTRICT)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class quintuple_value_mega_sena(models.Model):
    id = models.CharField(max_length=14, primary_key=True)
    v1 = models.IntegerField()
    v2 = models.IntegerField()
    v3 = models.IntegerField()
    v4 = models.IntegerField()
    v5 = models.IntegerField()
    quantidade = models.BigIntegerField()
    media_frequencia = models.IntegerField()
    ultimo_concurso = models.BigIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    concursos = models.ManyToManyField(
        Mega_sena_concurso, through='quintuple_Mega_sena_concurso')

    class Meta:
        indexes = [
            models.Index(fields=['v1', 'v2', 'v3', 'v4', 'v5']),
            models.Index(fields=['media_frequencia']),
        ]


class quintuple_Mega_sena_concurso(models.Model):
    concurso = models.ForeignKey(Mega_sena_concurso, on_delete=models.CASCADE)
    value = models.ForeignKey(
        quintuple_value_mega_sena, on_delete=models.RESTRICT)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class sextuple_value_mega_sena(models.Model):
    id = models.CharField(max_length=17, primary_key=True)
    v1 = models.IntegerField()
    v2 = models.IntegerField()
    v3 = models.IntegerField()
    v4 = models.IntegerField()
    v5 = models.IntegerField()
    v6 = models.IntegerField()
    quantidade = models.BigIntegerField()
    media_frequencia = models.IntegerField()
    ultimo_concurso = models.BigIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    concursos = models.ManyToManyField(
        Mega_sena_concurso, through='sextuple_Mega_sena_concurso')

    class Meta:
        indexes = [
            models.Index(fields=['v1', 'v2', 'v3', 'v4', 'v5', 'v6']),
            models.Index(fields=['media_frequencia']),
        ]


class sextuple_Mega_sena_concurso(models.Model):
    concurso = models.ForeignKey(Mega_sena_concurso, on_delete=models.CASCADE)
    value = models.ForeignKey(
        sextuple_value_mega_sena, on_delete=models.RESTRICT)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
