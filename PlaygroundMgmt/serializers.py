from rest_framework import serializers
from .models import AssetType

class AssetTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = AssetType
		fields = ('id', 'name')