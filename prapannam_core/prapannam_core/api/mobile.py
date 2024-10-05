import frappe

# Get Details of current user
@frappe.whitelist()
def get_current_user():
    current_user = frappe.session.user
    
    return {
        "status": "ok",
        "user": current_user,
    }
