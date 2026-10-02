def car_info(manufacturer, brand, **info):
	"""Сохраняет в словарь данные: производителя машины, бренд, доп. информацию"""
	info['car_manufacturer'] = manufacturer
	info['car_brand'] = brand
	return info