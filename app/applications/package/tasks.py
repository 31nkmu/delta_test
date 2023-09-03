from decimal import Decimal

from applications.interface.rate import RateInterface
from applications.package.models import Package
from config.celery import app


def calculate_delivery(weight: float | int,
                       cost: float | int,
                       rate: float | int) -> Decimal:
    """
    высчитывает цену доставки
    """
    return Decimal((weight/1000 * 0.5 + cost*0.01) * rate)


@app.task
def period_update_delivery():
    rate_obj = RateInterface()
    packages_to_update = Package.objects.filter(delivery__isnull=True).all()
    res_objects = []
    for package_obj in packages_to_update:
        rate = float(rate_obj.get_rub_rate())
        delivery = calculate_delivery(
            weight=float(package_obj.weight),
            cost=float(package_obj.cost),
            rate=rate
        )
        package_obj.delivery = delivery
        res_objects.append(package_obj)
    Package.objects.bulk_create(
        res_objects,
        update_conflicts=True,
        update_fields=('delivery',),
        unique_fields=('id',),
    )
