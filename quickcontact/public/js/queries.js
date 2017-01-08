
frappe.provide("erpnext.queries");
$.extend(erpnext.queries, {
	supplier: function() {
		return { query: "quickcontact.quickcontact.queries.supplier_query" };
	},
	customer: function() {
		return { query: "quickcontact.quickcontact.queries.customer_query" };
	}
});
