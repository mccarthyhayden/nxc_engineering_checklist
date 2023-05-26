from odoo import api, fields, models

class NxcEngineeringChecklistMrpProduction(models.Model):
    _inherit = 'mrp.production'

    #rebuild of field
    rebuild_of = fields.Many2one(
    'mrp.production',
    string='Rebuild Of',
    )

    product_categ_id=fields.Integer(string="Product Category ID")

    #approvals
    internal_design_apprval=fields.Boolean(string="Internal Design Approval")
    customer_design_approval=fields.Boolean(string="Internal Design Approval")
    
    #Sales Checklist Status Indicator
    engineering_checklist_status = fields.Selection([
        ('blocked','In-Progress'),
        ('done','Done'),
    ], string="Checklist Status", compute="_compute_engineering_checklist_status")
    
    #Design Checklist Items
    design_item_1 = fields.Boolean(string="Review CAD model and part print together to verify no discrepancies")
    design_item_2 = fields.Boolean(string="Verify model is a sold and water-tight")
    design_item_3 = fields.Boolean(string="Tolerances less than +/-.003in or +/-.1mm require finish machining")
    design_item_4 = fields.Boolean(string="Build orientation is clearly defined")
    design_item_5 = fields.Boolean(string="All overhanging angles greater than 45 deg are capable of adding supports")
    design_item_6 = fields.Boolean(string="All part modifications consider the entire assembly for fit, form, & function outside of singular part")
    design_item_7 = fields.Boolean(string="Verify there are no features smaller <.010in that would not print")
    design_item_8 = fields.Selection([
        ('1','No - Scaling Not Applied'),
        ('2','Yes - Scaling Applied'),
    ], string="Does Model require scaling for shrink or warp?")
    design_item_9 = fields.Boolean(string="Interconnected parts accommodate clearance required for upskin and downskin contours")
    design_item_10 = fields.Boolean(string="Customer specific print or CAD requirements are able to be manufactured")
    design_complete = fields.Boolean(string="Design Checklist Complete", compute="_compute_design_complete")

    #Design Build Checklist Items
    design_build_item_1 = fields.Boolean(string="Review CAD model and part print together to verify no discrepancies")
    design_build_item_2 = fields.Boolean(string="Verify model is a sold and water-tight")
    design_build_item_3 = fields.Boolean(string="Tolerances less than +/-.003in or +/-.1mm require finish machining")
    design_build_item_4 = fields.Boolean(string="Add necessary machining stock in 3DXpert for critical surfaces")
    design_build_item_5 = fields.Boolean(string="Build orientation is clearly defined")
    design_build_item_6 = fields.Boolean(string="Add .080in machining stock to the surfaces that will be attached to the build plate for EDM removal from plate")
    design_build_item_7 = fields.Boolean(string="All overhanging angles greater than 45 deg are capable of adding supports")
    design_build_item_8 = fields.Boolean(string="Add solid supports from part to build plate appropriate for the size of the part being supported")
    design_build_item_9 = fields.Boolean(string="All part modifications consider the entire assembly for fit, form, & function outside of singular part")
    design_build_item_10 = fields.Boolean(string="Verify there are no features smaller <.010in that would not print")
    design_build_item_11 = fields.Boolean(string="Add separate powder evacuation channel to build plate surface for critical-to-remove internal geometry. All internal geometry should have at least one in and out powder evacuation channel")
    design_build_item_12 = fields.Selection([
        ('1','No - Scaling Not Applied'),
        ('2','Yes - Scaling Applied'),
    ], string="Does Model require scaling for shrink or warp?")
    design_build_item_13 = fields.Boolean(string="Powder evacuation channels are to be semicircular in shape with a radius of .02-.06in")
    design_build_item_14 = fields.Boolean(string="Interconnected parts accommodate clearance required for upskin and downskin contours")
    design_build_item_15 = fields.Boolean(string="Export final file in STL format to SM (stockmodel) subfolder in project folder")
    design_build_complete = fields.Boolean(string="Design Build Checklist Complete", compute="_compute_design_build_complete")

    #Product Configuration Checklist Items
    product_config_item_1 = fields.Boolean(string="CAD Drawing Uploaded (In BOM Operations Steps)")
    product_config_item_2 = fields.Boolean(string="Manufacturing Order Configured")
    product_config_item_3 = fields.Boolean(string="Quality Checks Reviewed")
    product_config_complete = fields.Boolean(string="Product Configuration Checklist Complete", compute="_compute_product_config_complete")

    @api.onchange
    def _compute_design_complete(self):
    #This function determines whether the design checklist is complete.
    #Returns True if the checklist is complete, False otherwise.
      if (
        record.design_item_1 and
        record.design_item_2 and
        record.design_item_3 and
        record.design_item_4 and
        record.design_item_5 and
        record.design_item_6 and
        record.design_item_7 and
        record.design_item_8 in ('1', '2') and
        record.design_item_9 and
        record.design_item_10
      ):
        return True
      else:
        return False

    @api.onchange
    def _compute_design_build_complete(self):
    #This function determines whether the design build checklist is complete.
    #Returns True if the checklist is complete, False otherwise.
      if (
        record.design_build_item_1 and
        record.design_build_item_2 and
        record.design_build_item_3 and
        record.design_build_item_4 and
        record.design_build_item_5 and
        record.design_build_item_6 and
        record.design_build_item_7 and
        record.design_build_item_8 and
        record.design_build_item_9 and
        record.design_build_item_10 and
        record.design_build_item_11 and
        record.design_build_item_12 in ('1', '2') and
        record.design_build_item_13 and
        record.design_build_item_14 and
        record.design_build_item_15
      ):
        return True
      else:
        return False
      
    @api.onchange
    def _compute_product_config_complete(self):
    #This function determines whether the product config checklist is complete.
    #Returns True if the checklist is complete, False otherwise.
      if (
        record.product_config_item_1 and
        record.product_config_item_2 and
        record.product_config_item_3
      ):
        return True
      else:
        return False
      
    @api.onchange
    def _compute_engineering_checklist_status(self):
    #This method computes the value of the `engineering_checklist_status` field.
    #Returns The value of the `engineering_checklist_status` field.
      if record.rebuild_of.engineering_checklist_status == 'done':
        return 'done'
      elif record.product_id.categ_id.id in [11, 16]:
        return 'done'
      elif record.design__complete and record.design_build_complete and record.product_configuration_complete and record.internal_design_approval and record.customer_design_approval:
        return 'done'
      else:
        return 'blocked'