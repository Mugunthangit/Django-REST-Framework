from django.db import models

class BusinessType(models.Model):
	business_type = models.IntegerField(blank=False)
	business_name = models.CharField(max_length=100, blank=False)
	created_by = models.CharField(max_length=100, blank=False)
	updated_by = models.CharField(max_length=100, blank=False)

	class Meta(object):
		ordering = ('business_name',)


class Business(models.Model):
	business_type = models.IntegerField(blank=False)
	business_name = models.CharField(max_length=100, blank=False)
	created_by = models.CharField(max_length=100, blank=False)
	updated_by = models.CharField(max_length=100, blank=False)
	business_id = models.IntegerField(blank=False)
	description = models.CharField(max_length=100, blank=False)

	class Meta(object):
		ordering = ('business_type',)