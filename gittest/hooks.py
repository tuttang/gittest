# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "gittest"
app_title = "Gittest"
app_publisher = "tuttang"
app_description = "testing git commands"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = " "
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/gittest/css/gittest.css"
# app_include_js = "/assets/gittest/js/gittest.js"

# include js, css files in header of web template
# web_include_css = "/assets/gittest/css/gittest.css"
# web_include_js = "/assets/gittest/js/gittest.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "gittest.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "gittest.install.before_install"
# after_install = "gittest.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "gittest.notifications.get_notification_config"

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
# 		"gittest.tasks.all"
# 	],
# 	"daily": [
# 		"gittest.tasks.daily"
# 	],
# 	"hourly": [
# 		"gittest.tasks.hourly"
# 	],
# 	"weekly": [
# 		"gittest.tasks.weekly"
# 	]
# 	"monthly": [
# 		"gittest.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "gittest.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "gittest.event.get_events"
# }

