# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class KRA(Document):
	def validate(self):
		if self.score > 100:
			frappe.throw("Nilai maksimal score adalah 100.")
