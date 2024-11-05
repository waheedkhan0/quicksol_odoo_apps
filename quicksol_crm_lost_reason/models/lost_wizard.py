from odoo import models, fields, api


class CrmLeadLost(models.TransientModel):
    _inherit = 'crm.lead.lost'

    custom_lost_reason = fields.Text('Additional Lost Reason')
    is_other_reason = fields.Boolean(compute='_compute_is_other_reason',store=False)

    @api.depends('lost_reason_id')
    def _compute_is_other_reason(self):
        for record in self:
            record.is_other_reason = record.lost_reason_id.name == 'Others' if record.lost_reason_id else False

    def action_lost_reason_apply(self):
        result = super(CrmLeadLost, self).action_lost_reason_apply()
        if self.is_other_reason and self.custom_lost_reason:
            leads = self.env['crm.lead'].browse(self.env.context.get('active_ids'))
            leads.write({'custom_lost_reason': self.custom_lost_reason})
        return result

