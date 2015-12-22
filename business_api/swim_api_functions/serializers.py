from rest_framework import serializers
from swim_api_functions.models import BusinessType, Business

class BusinessSerializer(serializers.Serializer):
	business_type = serializers.IntegerField()
	business_name = serializers.CharField(max_length = 100)
	created_by = serializers.CharField()
	updated_by = serializers.CharField()
	business_id = serializers.IntegerField()
	description = serializers.CharField()
	
	def create(self, validated_data):
		return Business.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.business_type = validated_data.get('business_type', instance.business_type)
		instance.business_name = validated_data.get('business_name', instance.business_name)
		instance.created_by = validated_data.get('created_by', instance.created_by)
		instance.updated_by = validated_data.get('updated_by', instance.updated_by)
		instance.business_id = validated_data.get('business_id', instance.business_id)
		instance.description = validated_data.get('description', instance.description)
		instance.save()
		return instance
		'''
		class Meta:
			model = Business
        	fields = ('business_type', 'business_name', 'created_by', 'updated_by','business_id','description')'''

	
	
class BusinessTypeSerializer(serializers.Serializer):
	business_type = serializers.IntegerField()
	business_name = serializers.CharField()
	created_by = serializers.CharField()
	updated_by = serializers.CharField()
	
	def create(self, validated_data):
		return BusinessType.objects.create(**validated_data)

	'''class Meta:
		model = BusinessType
		fields = ('business_type', 'business_name', 'created_by', 'updated_by')'''