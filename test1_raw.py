
# округление происходит в большую сторону, 10,60 --> 11, 7.82 --> 8 
def check_proc_max(netto, vat_rate, vat_sum):
	""" метод проверки процента """
	_ = vat_rate / 100
	if round(netto*_) != round(vat_sum):
		print("Не верно указан процент", netto, vat_rate, vat_sum)


# округление происходит в меньшую сторону, 10,60 --> 10, 7.82 --> 7
# просто обрвсывает дробную часть 
def check_proc_min(netto, vat_rate, vat_sum):
	""" метод проверки процента """
	_ = vat_rate / 100
	if round(netto*_) != int(vat_sum):
		print("Не верно указан процент", netto, vat_rate, vat_sum)
