# Copyright (c) 2022, foram and contributors
# For license information, please see license.txt

from wsgiref import validate
import datetime
from datetime  import timedelta
import frappe
from datetime import date
from frappe.model.document import Document

class LibraryTransaction(Document):
	# def refresh(self):
		# y= frappe.db.get_value("""select value from `tabSingles` where field = 'loan_period';""")
		# y=int(frappe.db.get_single_value("Library Settings", 'loan_period'))
		
		# print(y)
		# self.duration="Hello"
		# print(self.duration)
	# def validate(self):
	# 	y=int(frappe.db.get_single_value("Library Settings", 'loan_period'))
	# 	self.duration=y
	# 	print(y)

	def before_save(self):
		a=self.member
		print(a)
		a1= frappe.db.sql_list(f"""select member_name from `tabLibrary Transaction` where status="Issued" and member='{a}';""")
		b1=len(a1)
		print(b1)
		print(type(b1))
		y=int(frappe.db.get_single_value("Library Settings", 'loan_period'))
		# self.duration=y
		# y=int(frappe.db.get_single_value("Library Settings", 'loan_period'))
		# self.duration=y
		# print(y)
		print(y)
		# a2= frappe.db.get_value("""select value from `tabSingles` where field = 'no_article';""")
		a2=int(frappe.db.get_single_value("Library Settings", 'no_article'))
		print(a2)
		print(type(a2))
		# x=frappe.db.sql_list(f"""select member_name from `tabLibrary Transaction` where status="Issued";""")
		if self.status=="Issued":
			if b1<a2:
				ab=datetime.date.today()
				print(ab)
				self.start_date=ab
				self.duration=y
				ab2=ab+timedelta(days=y)
				# ab2=datetime.datetime.add_days(frappe.datetime.now_date(), ab1)
				print(ab2)
				self.end_date=ab2
				frappe.msgprint("Thanks")
			else:
				frappe.throw("NO NO u cant get the book")
		else:
			frappe.msgprint("Thanks for returning")
	# 	if b1<a2:
	# 		{
	# 			frappe.msgprint("Thanks")
	# 		}
	# 	else:
	# 		return 

	# def hello(self):
	# 	if (self.status=="Return"):
	# 		{
	# 			frappe.msgprint("Thanks you for returning")
	# 		}
	# 	else:
	# 		{
	# 			frappe.throw()
	# 		}
	# # def validate(frm):
	# 	a=frappe.db.get_list('Library Transaction', pluck='member_name')
	# 	print(a)
# @frappe.whitelist()
# def get_all_roles(a):
# # def get_all_roles():
# 	# a="foram  undefined"
# 	print(a)
# 	a1= frappe.db.sql_list(f"""select member_name from `tabLibrary Transaction` where member_name = '{a}';""")
# 	b1=len(a1)
# 	print(b1)
# 	print(type(b1))
# 	# a2= frappe.db.get_value("""select value from `tabSingles` where field = 'no_article';""")
# 	a2=int(frappe.db.get_single_value("Library Settings", 'no_article'))
# 	print(a2)
# 	print(type(a2))
# 	if (b1>a2):
# 		# {
# 		# 	frappe.throw("NO NO u cant get the book ")
# 		# }
# 		return  frappe.throw("NO NO u cant get the book ")
	# else:
	# 	{
	# 		frappe.msgprint("Hello")
	# 		# frappe.throw("NO NO u cant get the book ")
	# 	}
	# b2=len(a2)
    # value="hello"
	# a1= frappe.
	# print(a)
	# return a2
