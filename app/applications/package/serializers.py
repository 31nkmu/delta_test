from rest_framework import serializers

from applications.package.models import Package, PackageType


class PackageSerializer(serializers.ModelSerializer):
    delivery = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Package
        exclude = ('user_session',)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['delivery'] = 'Не рассчитано' if not rep['delivery'] else rep['delivery']
        return rep


class PackageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageType
        fields = '__all__'
