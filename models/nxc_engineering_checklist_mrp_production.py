from odoo import api, fields, models

class NxcEngineeringChecklistMrpProduction(models.Model):
    _inherit = 'mrp.production'

    #Sales Checklist Status Indicator
    sales_checklist_status = fields.Selection([
        ('blocked','In-Progress'),
        ('done','Done'),
    ], string="Checklist Status")
    
    #Feasiblity Review Checklist items
    feasibility_check_1 = fields.Boolean(string="Product(s) is/are Adequately Defined")
    feasibility_check_2 = fields.Boolean(string="Product(s) can be manufactured as designed/specified")
    feasibility_check_3 = fields.Boolean(string="Any special characteristics have been identified")
    feasibility_check_4 = fields.Boolean(string="Product performance requirements can be met")
    feasibility_check_5 = fields.Boolean(string="Statutory and regulatory requirements understood and can be met")
    feasibility_check_6 = fields.Boolean(string="Any nonstandard manufacturing methods are defined")
    feasibility_check_7 = fields.Boolean(string="Product meets customer-defined objectives (Price & Timing)")
    feasibility_check_8 = fields.Boolean(string="Product meets our goals for cost and margin")
    feasibility_check_9 = fields.Selection([
        ('1','NOT Feasible - Revisions Required'),
        ('2','Feasible - Revisions Recommended'),
        ('3','Feasible - No Revisions Needed'),
    ], string="Feasability Rating")
    feasibility_check_10 = fields.Boolean(string="Device Master Record (DMR) completed")
    feasbility_remarks = fields.Html(string="Remarks")
    feasibility_review_complete = fields.boolean(string="Feasbility Review Complete")

    #Contract Review Checklist items
    contract_check_1 = fields.Boolean(string="Product Category is Accurately Configured")
    contract_check_2 = fields.Boolean(string="Quantities are Correct")
    contract_check_3 = fields.Boolean(string="Payment Terms are Correct")
    contract_check_4 = fields.Boolean(string="Pricing is Correct for Required Quantities")
    contract_check_5 = fields.Boolean(string="Latest CAD Data & Associated Specs Available")
    contract_check_6 = fields.Boolean(string="Customer Identity is Correct")
    contract_check_7 = fields.Boolean(string="Customer is Aware of Potential Risks")
    contract_check_8 = fields.Boolean(string="Delivery Date / Lead Time(s) Confirmed")
    contract_review_complete = fields.Boolean(string="Contract Review Complete")