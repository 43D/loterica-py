# Generated by Django 4.0.5 on 2022-06-24 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='double_Mega_sena_concurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='double_value_mega_sena',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('v1', models.IntegerField()),
                ('v2', models.IntegerField()),
                ('quantidade', models.BigIntegerField()),
                ('media_frequencia', models.IntegerField()),
                ('ultimo_concurso', models.BigIntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mega_sena_concurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_concurso', models.BigIntegerField(unique=True)),
                ('data', models.DateField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='quadruple_Mega_sena_concurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('concurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mega_sena_concurso')),
            ],
        ),
        migrations.CreateModel(
            name='quintuple_Mega_sena_concurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('concurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mega_sena_concurso')),
            ],
        ),
        migrations.CreateModel(
            name='sextuple_Mega_sena_concurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('concurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mega_sena_concurso')),
            ],
        ),
        migrations.CreateModel(
            name='single_Mega_sena_concurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('concurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mega_sena_concurso')),
            ],
        ),
        migrations.CreateModel(
            name='triple_Mega_sena_concurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('concurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mega_sena_concurso')),
            ],
        ),
        migrations.CreateModel(
            name='triple_value_mega_sena',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('v1', models.IntegerField()),
                ('v2', models.IntegerField()),
                ('v3', models.IntegerField()),
                ('quantidade', models.BigIntegerField()),
                ('media_frequencia', models.IntegerField()),
                ('ultimo_concurso', models.BigIntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('concursos', models.ManyToManyField(through='api.triple_Mega_sena_concurso', to='api.mega_sena_concurso')),
            ],
        ),
        migrations.AddField(
            model_name='triple_mega_sena_concurso',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.triple_value_mega_sena'),
        ),
        migrations.CreateModel(
            name='single_value_mega_sena',
            fields=[
                ('id', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('v1', models.IntegerField()),
                ('quantidade', models.BigIntegerField()),
                ('media_frequencia', models.IntegerField()),
                ('ultimo_concurso', models.BigIntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('concursos', models.ManyToManyField(through='api.single_Mega_sena_concurso', to='api.mega_sena_concurso')),
            ],
        ),
        migrations.AddField(
            model_name='single_mega_sena_concurso',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.single_value_mega_sena'),
        ),
        migrations.CreateModel(
            name='sextuple_value_mega_sena',
            fields=[
                ('id', models.CharField(max_length=17, primary_key=True, serialize=False)),
                ('v1', models.IntegerField()),
                ('v2', models.IntegerField()),
                ('v3', models.IntegerField()),
                ('v4', models.IntegerField()),
                ('v5', models.IntegerField()),
                ('v6', models.IntegerField()),
                ('quantidade', models.BigIntegerField()),
                ('media_frequencia', models.IntegerField()),
                ('ultimo_concurso', models.BigIntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('concursos', models.ManyToManyField(through='api.sextuple_Mega_sena_concurso', to='api.mega_sena_concurso')),
            ],
        ),
        migrations.AddField(
            model_name='sextuple_mega_sena_concurso',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.sextuple_value_mega_sena'),
        ),
        migrations.CreateModel(
            name='quintuple_value_mega_sena',
            fields=[
                ('id', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('v1', models.IntegerField()),
                ('v2', models.IntegerField()),
                ('v3', models.IntegerField()),
                ('v4', models.IntegerField()),
                ('v5', models.IntegerField()),
                ('quantidade', models.BigIntegerField()),
                ('media_frequencia', models.IntegerField()),
                ('ultimo_concurso', models.BigIntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('concursos', models.ManyToManyField(through='api.quintuple_Mega_sena_concurso', to='api.mega_sena_concurso')),
            ],
        ),
        migrations.AddField(
            model_name='quintuple_mega_sena_concurso',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.quintuple_value_mega_sena'),
        ),
        migrations.CreateModel(
            name='quadruple_value_mega_sena',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('v1', models.IntegerField()),
                ('v2', models.IntegerField()),
                ('v3', models.IntegerField()),
                ('v4', models.IntegerField()),
                ('quantidade', models.BigIntegerField()),
                ('media_frequencia', models.IntegerField()),
                ('ultimo_concurso', models.BigIntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('concursos', models.ManyToManyField(through='api.quadruple_Mega_sena_concurso', to='api.mega_sena_concurso')),
            ],
        ),
        migrations.AddField(
            model_name='quadruple_mega_sena_concurso',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.quadruple_value_mega_sena'),
        ),
        migrations.CreateModel(
            name='Mega_sena_valores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v1', models.IntegerField()),
                ('v2', models.IntegerField()),
                ('v3', models.IntegerField()),
                ('v4', models.IntegerField()),
                ('v5', models.IntegerField()),
                ('v6', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('id_concurso', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.mega_sena_concurso')),
            ],
        ),
        migrations.AddIndex(
            model_name='mega_sena_concurso',
            index=models.Index(fields=['id_concurso'], name='api_mega_se_id_conc_eec7f0_idx'),
        ),
        migrations.AddIndex(
            model_name='mega_sena_concurso',
            index=models.Index(fields=['data'], name='api_mega_se_data_5f73a5_idx'),
        ),
        migrations.AddField(
            model_name='double_value_mega_sena',
            name='concursos',
            field=models.ManyToManyField(through='api.double_Mega_sena_concurso', to='api.mega_sena_concurso'),
        ),
        migrations.AddField(
            model_name='double_mega_sena_concurso',
            name='concurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mega_sena_concurso'),
        ),
        migrations.AddField(
            model_name='double_mega_sena_concurso',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.double_value_mega_sena'),
        ),
        migrations.AddIndex(
            model_name='triple_value_mega_sena',
            index=models.Index(fields=['v1', 'v2', 'v3'], name='api_triple__v1_0e5f74_idx'),
        ),
        migrations.AddIndex(
            model_name='triple_value_mega_sena',
            index=models.Index(fields=['media_frequencia'], name='api_triple__media_f_5cb4f0_idx'),
        ),
        migrations.AddIndex(
            model_name='single_value_mega_sena',
            index=models.Index(fields=['v1'], name='api_single__v1_8796d5_idx'),
        ),
        migrations.AddIndex(
            model_name='single_value_mega_sena',
            index=models.Index(fields=['media_frequencia'], name='api_single__media_f_4aafb4_idx'),
        ),
        migrations.AddIndex(
            model_name='sextuple_value_mega_sena',
            index=models.Index(fields=['v1', 'v2', 'v3', 'v4', 'v5', 'v6'], name='api_sextupl_v1_7957b3_idx'),
        ),
        migrations.AddIndex(
            model_name='sextuple_value_mega_sena',
            index=models.Index(fields=['media_frequencia'], name='api_sextupl_media_f_5b5693_idx'),
        ),
        migrations.AddIndex(
            model_name='quintuple_value_mega_sena',
            index=models.Index(fields=['v1', 'v2', 'v3', 'v4', 'v5'], name='api_quintup_v1_7b6cb6_idx'),
        ),
        migrations.AddIndex(
            model_name='quintuple_value_mega_sena',
            index=models.Index(fields=['media_frequencia'], name='api_quintup_media_f_9a5caf_idx'),
        ),
        migrations.AddIndex(
            model_name='quadruple_value_mega_sena',
            index=models.Index(fields=['v1', 'v2', 'v3', 'v4'], name='api_quadrup_v1_8b61af_idx'),
        ),
        migrations.AddIndex(
            model_name='quadruple_value_mega_sena',
            index=models.Index(fields=['media_frequencia'], name='api_quadrup_media_f_368fef_idx'),
        ),
        migrations.AddIndex(
            model_name='mega_sena_valores',
            index=models.Index(fields=['id_concurso'], name='api_mega_se_id_conc_dfb7ee_idx'),
        ),
        migrations.AddIndex(
            model_name='double_value_mega_sena',
            index=models.Index(fields=['v1', 'v2'], name='api_double__v1_9ae11d_idx'),
        ),
        migrations.AddIndex(
            model_name='double_value_mega_sena',
            index=models.Index(fields=['media_frequencia'], name='api_double__media_f_e861d9_idx'),
        ),
    ]
