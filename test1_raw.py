

def check_proc(netto, vat_rate, vat_sum):
	""" метод проверки процента """
	_ = vat_rate / 100
	if round(netto*_) != round(vat_sum):
		print("Не верно указан процент", netto, vat_rate, vat_sum)