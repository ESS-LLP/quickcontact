# -*- coding: utf-8 -*-
# Copyright (c) 2015, ESS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import time
from frappe.utils import cstr
from frappe import msgprint, _

def update_contact_from_customer(doc, method):
	if(doc.phone or doc.email or doc.mobile):
		if frappe.db.exists({"doctype": "Contact", "customer": doc.name, "quick_contact": 1}):
			update_contact_by_name(doc, 1, 0)

		else:
			msg_print(create_contact(doc, 1, 0))

def update_contact_from_supplier(doc, method):
	if(doc.phone or doc.email or doc.mobile):
		if frappe.db.exists({"doctype": "Contact", "supplier": doc.name, "quick_contact": 1}):
			update_contact_by_name(doc, 0, 1)

		else:
			msg_print(create_contact(doc, 0, 1))

def msg_print(contact):
	frappe.msgprint(_("Primary and searchable contact <a href='#Form/Contact/{0}'>{0}</a> created").format(contact))

def create_contact(doc, is_customer, is_supplier):
	contact = frappe.new_doc("Contact")
	contact.first_name = doc.name
	contact.email_id = doc.email
	contact.mobile_no = doc.mobile
	contact.phone = doc.phone
	contact.is_primary_contact = 1
	contact.quick_contact = 1
	if(is_customer):
		contact.customer = doc.name
		contact.customer_name = doc.customer_name
	if(is_supplier):
		contact.supplier = doc.name
		contact.supplier_name = doc.supplier_name
	contact.save(ignore_permissions=True)
	return contact.name

def update_contact_by_name(doc, is_customer, is_supplier):
	if(is_customer):
		frappe.db.sql("""update `tabContact` set email_id=%s, mobile_no=%s, phone=%s,
				modified=NOW() where customer=%s and quick_contact=1 """,
			(doc.email, doc.mobile, doc.phone, doc.name ))
	if(is_supplier):
		frappe.db.sql("""update `tabContact` set email_id=%s, mobile_no=%s, phone=%s,
				modified=NOW() where supplier=%s and quick_contact=1 """,
			(doc.email, doc.mobile, doc.phone, doc.name ))


def update_from_contact(doc, method):
	validate_quick_contact(doc)
	if doc.quick_contact == 1:
		if doc.customer:
			frappe.db.sql("""update tabCustomer set mobile = %s, phone = %s,
					email = %s where name = %s""",
					(doc.mobile_no, doc.phone,doc.email_id, doc.customer))
		if doc.supplier:
			frappe.db.sql("""update tabSupplier set mobile = %s, phone = %s,
					email = %s where name = %s""",
					(doc.mobile_no, doc.phone,doc.email_id, doc.supplier))

def validate_quick_contact(doc):
		if doc.quick_contact == 1:
			if doc.customer:
				frappe.db.sql("update tabContact set quick_contact=0 where customer = %s",
					(doc.customer))
			elif doc.supplier:
				frappe.db.sql("update tabContact set quick_contact=0 where supplier = %s",
					 (doc.supplier))
			frappe.db.set_value("Contact",doc.name,"quick_contact","1")

		else:
			if doc.customer:
				if not frappe.db.sql("""select name from tabContact
					where quick_contact=1 and customer = %s""", (doc.customer)):
					doc.quick_contact = 1
			elif doc.supplier:
				if not frappe.db.sql("""select name from tabContact
						where quick_contact=1 and supplier = %s""", (doc.supplier)):
					doc.quick_contact = 1
