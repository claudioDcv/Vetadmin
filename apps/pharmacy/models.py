from django.db import models
from apps.core.models import Person
from django_extensions.db.fields import AutoSlugField
from apps.core.models import Participant


class TypeSupplyMovement(models.Model):
    name = models.CharField(max_length=100)
    natural_key = AutoSlugField(populate_from='name')

    class Meta:
        verbose_name = 'tipo de movimiento'
        verbose_name_plural = 'tipo de movimientos'

    def __str__(self):
        return '{}'.format(self.name)


class UnitOfMeasurement(models.Model):
    name = models.CharField(max_length=100)
    natural_key = AutoSlugField(populate_from='name')

    class Meta:
        verbose_name = 'unidad de medida'
        verbose_name_plural = 'unidades de medida'

    def __str__(self):
        return '{}'.format(self.name)


class Supply(models.Model):
    name = models.CharField(max_length=100)
    natural_key = AutoSlugField(populate_from='name')
    description = models.TextField()
    stocks = models.DecimalField(max_digits=15, decimal_places=1, blank=True, null=True)
    unit_of_measurement = models.ForeignKey(UnitOfMeasurement, models.DO_NOTHING)

    class Meta:
        verbose_name = 'suministro'

    def __str__(self):
        return '{}'.format(self.name)


class SupplyAssignControl(models.Model):
    date = models.DateTimeField()
    code_supply = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    supply = models.ForeignKey(Supply, models.DO_NOTHING)
    user = models.ForeignKey(Person, models.DO_NOTHING, limit_choices_to={'rol__id': 1})

    class Meta:
        verbose_name = 'asignación de suministro a control'

    def __str__(self):
        return '{}({})'.format(self.supply, self.supply.stocks)


class SupplyMovement(models.Model):
    date = models.DateTimeField()
    code_supply = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    supply = models.ForeignKey(Supply, models.DO_NOTHING)
    type_supply_movement = models.ForeignKey(TypeSupplyMovement, models.DO_NOTHING)
    user_from = models.ForeignKey(Participant, models.DO_NOTHING, related_name='user_from')
    user_to = models.ForeignKey(Participant, models.DO_NOTHING, related_name='user_to')
    expire_date = models.DateField()

    class Meta:
        verbose_name = 'movimiento'

    def from_to(self):
        return '{} -> {}'.format(self.user_from, self.user_to)

    def supply_stocks(self):
        return '{}({})'.format(self.supply, self.supply.stocks)

    def __str__(self):
        return self.from_to()

    def save(self, *args, **kwargs):

        if self.supply.stocks is None:
            self.supply.stocks = 0
        if self.type_supply_movement.natural_key == 'egreso':
            self.supply.stocks = self.supply.stocks - self.amount
        else:
            self.supply.stocks = self.supply.stocks + self.amount
        self.supply.save()

        if self.pk is None:
            super(SupplyMovement, self).save(*args, **kwargs)

    def delete(self):

        if self.type_supply_movement.natural_key == 'egreso':
            self.supply.stocks = self.supply.stocks + self.amount
        else:
            self.supply.stocks = self.supply.stocks - self.amount
        self.supply.save()

        super(SupplyMovement, self).delete()
