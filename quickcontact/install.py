from __future__ import unicode_literals

import frappe
from frappe import _

def after_install():
	create_custom_fields()
	#index custom fields
	frappe.db.add_index("Customer", ["mobile"])
	frappe.db.add_index("Customer", ["phone"])
	frappe.db.add_index("Customer", ["email"])
	frappe.db.add_index("Supplier", ["mobile"])
	frappe.db.add_index("Supplier", ["phone"])
	frappe.db.add_index("Supplier", ["email"])
	#get all primary contacts with relation to customer or supplier
	contacts = frappe.db.sql("""select name, phone, email_id, mobile_no, customer, supplier from tabContact where is_primary_contact=1 and (customer !='' or supplier!='') """)
	
	for contact in contacts:
		#if fields phone, email or mobile has value, update contact as searchable and copy data to custom fields in Customer or Supplier
		if(contact[1] or contact[2] or contact[3]):
			frappe.db.set_value("Contact", contact[0], "quick_contact", "1")
			
			if(contact[4]):
				frappe.db.sql("""update tabCustomer set phone = %s, email = %s, mobile = %s where name = %s""", (contact[1], contact[2], contact[3], contact[4]))
			
			if(contact[5]):
				frappe.db.sql("""update tabSupplier set phone = %s, email = %s, mobile = %s where name = %s""", (contact[1], contact[2], contact[3], contact[5]))

def create_custom_fields():
	from frappe.custom.doctype.custom_field.custom_field import create_custom_field
	#custom fields mobile, email and phone in Customer and Supplier, quick_contact in Contact
	create_custom_field('Contact', {
		'label': _('Searchable'),
		'fieldname': 'quick_contact',
		'fieldtype': 'Check',
		'default': 0,
		'insert_after': 'is_primary_contact'
	})
	create_custom_field('Customer', {
		'label': _('Mobile'),
		'fieldname': 'mobile',
		'fieldtype': 'Data',
		'default': 'null',
		'insert_after': 'lead_name'
	})
	create_custom_field('Customer', {
		'label': _('Email'),
		'fieldname': 'email',
		'fieldtype': 'Data',
		'options': 'Email', 
		'default': 'null',
		'insert_after': 'mobile'
	})
	create_custom_field('Customer', {
		'label': _('Phone'),
		'fieldname': 'phone',
		'fieldtype': 'Data',
		'default': 'null',
		'insert_after': 'email'
	})
	create_custom_field('Supplier', {
		'label': _('Mobile'),
		'fieldname': 'mobile',
		'fieldtype': 'Data',
		'default': 'null',
		'insert_after': 'supplier_name'
	})
	create_custom_field('Supplier', {
		'label': _('Email'),
		'fieldname': 'email',
		'fieldtype': 'Data',
		'options': 'Email',
		'default': 'null',
		'insert_after': 'mobile'
	})
	create_custom_field('Supplier', {
		'label': _('Phone'),
		'fieldname': 'phone',
		'fieldtype': 'Data',
		'default': 'null',
		'insert_after': 'email'
	})
