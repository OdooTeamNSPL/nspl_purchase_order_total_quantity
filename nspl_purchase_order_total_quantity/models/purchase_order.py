from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    total_received_qty = fields.Float(string="Total Received Qty", compute='_compute_quantities', store=True)
    total_billed_qty = fields.Float(string="Total Billed Qty", compute='_compute_quantities', store=True)
    total_demand_qty = fields.Float(string="Total Demand Qty", compute='_compute_quantities')
    pending_receipt_qty = fields.Float(string="Pending Receipt Qty", compute='_compute_quantities')
    pending_bill_qty = fields.Float(string="Pending Bill Qty", compute='_compute_quantities')

    @api.depends('order_line.product_qty', 'order_line.qty_received', 'order_line.qty_invoiced', 'order_line.product_id.type')
    def _compute_quantities(self):
        for order in self:
            total_demand = total_received = total_billed = 0.0
            for line in order.order_line:
                total_demand += line.product_qty
                total_received += line.qty_received
                total_billed += line.qty_invoiced
            order.total_demand_qty = total_demand
            order.total_received_qty = total_received
            order.total_billed_qty = total_billed
            order.pending_receipt_qty = total_demand - total_received
            order.pending_bill_qty = total_demand - total_billed
