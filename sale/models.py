from django.db import models
from django.utils.translation import ugettext_lazy as _


class Selling(models.Model):
	description = models.CharField(_("Описание"), max_length=250)
	netto = models.IntegerField(_("Нетто"))
	delivery_country = models.CharField(_("Страна доставки"), max_length=5)
	vat_rate = models.IntegerField(_("ставка НДС"))
	vat_sum = models.DecimalField(_("сумма НДС"), max_digits=4, decimal_places=2)


	def __str__(self):
		return self.description


	def check_proc(self):
		_ = self.vat_rate / 100
		if round(self.netto*_) != round(self.vat_sum):
			raise ValueError("ошибка процента")

	def save(self, *args, **kwargs):
		self.check_proc()
		super(Selling, self).save(*args, **kwargs)



	class Meta:
		verbose_name = _("Продажа")
		verbose_name_plural = _("Продажи")

