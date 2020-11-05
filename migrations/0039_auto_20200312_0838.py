# Generated by Django 2.2.2 on 2020-03-12 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ihr', '0038_atlas_delay_alarms_hegemony_alarms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asn',
            name='ashash',
            field=models.BooleanField(default=False, help_text='True if participate in AS dependency analysis.'),
        ),
        migrations.AlterField(
            model_name='asn',
            name='disco',
            field=models.BooleanField(default=False, help_text='True if participate in network disconnection analysis.'),
        ),
        migrations.AlterField(
            model_name='asn',
            name='name',
            field=models.CharField(help_text='Name registered for the network.', max_length=255),
        ),
        migrations.AlterField(
            model_name='asn',
            name='number',
            field=models.BigIntegerField(help_text='Autonomous System Number (ASN) or IXP ID. Note that IXP ID are negative to avoid colision.', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='asn',
            name='tartiflette',
            field=models.BooleanField(default=False, help_text='True if participate in link delay and forwarding anomaly analysis.'),
        ),
        migrations.AlterField(
            model_name='disco_probes',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discoprobes', to='ihr.Disco_events'),
        ),
    ]