from odoo import api, fields, models

class NxcEngineeringChecklistMrpProduction(models.Model):
    _inherit = 'mrp.production'

    #rebuild of field
    rebuild_of=fields.Many2One()

    #approvals
    internal_design_apprval=fields.Boolean(string="Internal Design Approval" readonly=True invisible="|(product_categ_id=11)|(product_categ_id=16)")
    customer_design_approval=fields.Boolean(string="Internal Design Approval" readonly=True invisible="|(product_categ_id=11)|(product_categ_id=16)")
    
    #Sales Checklist Status Indicator
    engineering_checklist_status = fields.Selection([
        ('blocked','In-Progress'),
        ('done','Done'),
    ], string="Checklist Status", readonly=True compute="_compute_engineering_checklist_status")
    
    #Design Checklist Items
    design_attrs = {
      'readonly': [
        ('design_complete', '=', True)
      ]
    }
    design_item_1 = fields.Boolean(string="Review CAD model and part print together to verify no discrepancies", **design_attrs)
    design_item_2 = fields.Boolean(string="Verify model is a sold and water-tight", **design_attrs)
    design_item_3 = fields.Boolean(string="Tolerances less than +/-.003in or +/-.1mm require finish machining", **design_attrs)
    design_item_4 = fields.Boolean(string="Build orientation is clearly defined", **design_attrs)
    design_item_5 = fields.Boolean(string="All overhanging angles greater than 45 deg are capable of adding supports", **design_attrs)
    design_item_6 = fields.Boolean(string="All part modifications consider the entire assembly for fit, form, & function outside of singular part", **design_attrs)
    design_item_7 = fields.Boolean(string="Verify there are no features smaller <.010in that would not print", **design_attrs)
    design_item_8 = fields.Selection([
        ('1','No - Scaling Not Applied'),
        ('2','Yes - Scaling Applied'),
    ], string="Does Model require scaling for shrink or warp?")
    design_item_9 = fields.Boolean(string="Interconnected parts accommodate clearance required for upskin and downskin contours", **design_attrs)
    design_item_10 = fields.Boolean(string="Customer specific print or CAD requirements are able to be manufactured", **design_attrs)
    design_complete = fields.boolean(string="Design Checklist Complete" widget="boolean_toggle" readonly=True invisible=True compute="_compute_design_complete")

    #Design Build Checklist Items
    design_build_attrs = {
      'readonly': [
        ('design_build_complete', '=', True)
      ]
    }
    design_build_item_1 = fields.Boolean(string="", **design_build_attrs)
    design_build_item_2 = fields.Boolean(string="", **design_build_attrs)
    design_build_item_3 = fields.Boolean(string="", **design_build_attrs)
    design_build_item_4 = fields.Boolean(string="", **design_build_attrs)
    design_build_item_5 = fields.Boolean(string="", **design_build_attrs)
    design_build_item_6 = fields.Boolean(string="", **design_build_attrs)
    design_build_item_7 = fields.Boolean(string="", **design_build_attrs)
    design_build_item_8 = fields.Boolean(string="", **design_build_attrs)
    design_build_item_9 = fields.Boolean(string="", **design_build_attrs)
    design_build_item_10 = fields.Boolean(string="", **design_build_attrs)
    design_build_item_11 = fields.Boolean(string="", **design_build_attrs)
    design_build_item_12 = fields.Selection([
        ('1','No - Scaling Not Applied'),
        ('2','Yes - Scaling Applied'),
    ], string="Does Model require scaling for shrink or warp?", **design_build_attrs)
    design_build_item_13 = fields.Boolean(string="", **design_build_attrs)
    design_build_item_14 = fields.Boolean(string="", **design_build_attrs)
    design_build_complete = fields.boolean(string="Design Build Checklist Complete" widget="boolean_toggle" readonly=True invisible=True compute="_compute_design_build_complete")

    #Product Configuration Checklist Items
    product_config_attrs = {
      'readonly': [
        ('product_config_complete', '=', True)
      ]
    }
    product_config_item_1 = fields.Boolean(string="CAD Drawing Uploaded (In BOM Operations Steps)", **product_config_attrs)
    product_config_item_2 = fields.Boolean(string="Manufacturing Order Configured", **product_config_attrs)
    product_config_item_3 = fields.Boolean(string="Quality Checks Reviewed", **product_config_attrs)
    product_config_complete = fields.boolean(string="Product Configuration Checklist Complete" widget="boolean_toggle" readonly=True invisible=True compute="_compute_product_config_complete")

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
        record.design_build_item_14
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