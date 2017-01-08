# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "quickcontact"
app_title = "QuickContact"
app_publisher = "ESS"
app_description = "Search Customer/Supplier by contact details"
app_icon = "octicon octicon-repo"
app_color = "grey"
app_email = "info@earthianslive.com"
app_license = "GNU General Public License"
fixtures = []

after_install = "quickcontact.install.after_install"

app_include_js = "assets/quickcontact/js/queries.js"

doc_events = {
	"Customer": {
		"on_update": "quickcontact.quickcontact.quickcontact.update_contact_from_customer"
	},
	"Supplier": {
		"on_update": "quickcontact.quickcontact.quickcontact.update_contact_from_supplier"
	},
	"Contact": {
		"on_update": "quickcontact.quickcontact.quickcontact.update_from_contact"
	}
}

standard_queries = {
	"Customer": "quickcontact.quickcontact.queries.customer_query",
	"Supplier": "quickcontact.quickcontact.queries.supplier_query"
}



# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/quickcontact/css/quickcontact.css"
# app_include_js = "/assets/quickcontact/js/quickcontact.js"

# include js, css files in header of web template
# web_include_css = "/assets/quickcontact/css/quickcontact.css"
# web_include_js = "/assets/quickcontact/js/quickcontact.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "quickcontact.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "quickcontact.install.before_install"
# after_install = "quickcontact.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "quickcontact.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"quickcontact.tasks.all"
# 	],
# 	"daily": [
# 		"quickcontact.tasks.daily"
# 	],
# 	"hourly": [
# 		"quickcontact.tasks.hourly"
# 	],
# 	"weekly": [
# 		"quickcontact.tasks.weekly"
# 	]
# 	"monthly": [
# 		"quickcontact.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "quickcontact.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "quickcontact.event.get_events"
# }

