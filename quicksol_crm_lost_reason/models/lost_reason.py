from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    custom_lost_reason = fields.Text('Additional Lost Reason')
    is_other_reason = fields.Boolean(compute='_compute_is_other_reason', store=False)

    @api.depends('lost_reason_id')
    def _compute_is_other_reason(self):
        for record in self:
            record.is_other_reason = record.lost_reason_id.name == 'Others' if record.lost_reason_id else False

    # def action_set_lost(self, **additional_values):
    #     # Add custom reason to the lost reason popup
    #     if self.env.context.get('custom_lost_reason'):
    #         additional_values['custom_lost_reason'] = self.env.context.get('custom_lost_reason')
    #     return super(CrmLead, self).action_set_lost(**additional_values)
