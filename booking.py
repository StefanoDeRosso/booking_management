from osv import orm, fields, osv


class booking_info(orm.Model):
    _name = 'booking.info'
    # _inherit = 'res.partner'

    _description = 'Room info'

    _columns = {
        # 'rooms_id': fields.one2many('travel.room', 'hostel_id', 'Rooms'),
        'name': fields.char('Name'),
        'room_type': fields.char('Room type', size=16),
        'price': fields.float('Price'),
        'guests': fields.integer('Guests'),
        'active': fields.boolean('Active')
    }

    _defaults = {
        'active': True,
        # 'state': 'draft',
    }

    def _check_name(self, cr, uid, ids, context=None):
        for booking_info in self.browse(cr, uid, ids, context=None):
            if 'spam' in booking_info.name:
                return False
        return True

    # _sql_constraints = [('rooms_id_uniq', unique('rooms_id'), 'Rooms must be unique!')]
    _constraints = [(_check_name, 'Please avoid spam in rooms_id!', ['name'])]
