from rest_framework import serializers

from components.models import *

class OperatingSystemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OperatingSystem
        fields = ('id', 'name', 'version')


class ServerSerializer(serializers.ModelSerializer):

    os = serializers.SlugRelatedField(queryset=OperatingSystem.objects.all(),
						slug_field="id")

    class Meta:
        model = Server
        fields = ('id', 'hostname', 'ipv4', 'ipv6', 'location', 'enabled', 'os', 'types', 'created')
