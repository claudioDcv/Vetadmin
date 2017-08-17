from django.contrib import admin
from .models import TypeSupplyMovement, UnitOfMeasurement, Supply, SupplyAssignControl, \
    SupplyMovement


class TypeSupplyMovementAdmin(admin.ModelAdmin):
    pass


class UnitOfMeasurementAdmin(admin.ModelAdmin):
    pass


class SupplyAdmin(admin.ModelAdmin):
    readonly_fields = ('stocks',)


class SupplyAssignControlAdmin(admin.ModelAdmin):
    pass


class SupplyMovementAdmin(admin.ModelAdmin):
    list_display = (
        'from_to',
        'supply_stocks',
        'date',
        'code_supply',
        'amount',
        'type_supply_movement',
    )


admin.site.register(TypeSupplyMovement, TypeSupplyMovementAdmin)
admin.site.register(UnitOfMeasurement, UnitOfMeasurementAdmin)
admin.site.register(Supply, SupplyAdmin)
admin.site.register(SupplyAssignControl, SupplyAssignControlAdmin)
admin.site.register(SupplyMovement, SupplyMovementAdmin)
