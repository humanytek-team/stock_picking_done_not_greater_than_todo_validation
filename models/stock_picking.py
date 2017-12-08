# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp import api, models, _
from openerp.exceptions import ValidationError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def do_new_transfer(self):

        if not self.user_has_groups('stock.group_stock_manager'):
            for pick in self:
                for pack_operation in pick.pack_operation_product_ids:
                    if pack_operation.qty_done > pack_operation.product_qty:
                        raise ValidationError(
                            _('The quantity done should not be greater than quantity to do')
                            )

        return super(StockPicking, self).do_new_transfer()
