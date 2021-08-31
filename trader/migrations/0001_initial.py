

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positions', jsonfield.fields.JSONField(default={'name': 'positions'})),
                ('pastReturns', jsonfield.fields.JSONField(default={'name': 'pastReturns'})),
                ('cash', models.IntegerField(default=1000000)),
                ('AUM', models.IntegerField(default=1000000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
