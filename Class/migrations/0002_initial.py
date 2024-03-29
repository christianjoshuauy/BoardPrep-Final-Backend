# Generated by Django 4.2.4 on 2024-01-09 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Course', '0001_initial'),
        ('Class', '0001_initial'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.student'),
        ),
        migrations.AddField(
            model_name='post',
            name='class_instance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Class.class'),
        ),
        migrations.AddField(
            model_name='post',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.teacher'),
        ),
        migrations.AddField(
            model_name='joinrequest',
            name='class_instance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Class.class'),
        ),
        migrations.AddField(
            model_name='joinrequest',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.student'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Class.post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user'),
        ),
        migrations.AddField(
            model_name='class',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.course'),
        ),
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='classes', to='User.student'),
        ),
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.teacher'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user'),
        ),
        migrations.AddField(
            model_name='activity',
            name='attachments',
            field=models.ManyToManyField(blank=True, related_name='activities', to='Class.attachment'),
        ),
        migrations.AddField(
            model_name='activity',
            name='class_instance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Class.class'),
        ),
        migrations.AddField(
            model_name='activity',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.teacher'),
        ),
        migrations.AlterUniqueTogether(
            name='joinrequest',
            unique_together={('class_instance', 'student')},
        ),
    ]
