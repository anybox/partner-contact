# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Nicolas Bessi. Copyright Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import orm
from openerp.tools.translate import _


class ResUsers(orm.Model):

    _inherit = 'res.users'

    # We should use an AbstractModel to not write two time the same method
    def copy_data(self, cr, uid, _id, default=None, context=None):
        """
        Avoid to replicate the firstname into the name when duplicating a user
        """
        default = default or {}
        if not default.get('lastname'):
            default = default.copy()
            default['lastname'] = (
                _('%s (copy)') % self.read(
                    cr, uid, [_id], ['lastname'], context=context
                )[0]['lastname']
            )
        # force the recompute of the name after the copy
        # remove name from the default is not enough with store=True because
        # the name is also copied
        default['name'] = None
        return super(ResUsers, self).copy_data(
            cr, uid, _id, default, context=context)
