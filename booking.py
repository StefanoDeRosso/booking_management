from osv import orm, fields


class RoomInfo(orm.Model):
    _name = 'room.info'
    # _inherit = 'res.partner'

    _description = 'Room info'

    _columns = {
        'name': fields.char('Name'),
        'room_type': fields.char('Room type', required=True),
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

    _constraints = [(_check_name, 'Please avoid spam in rooms_id!', ['name'])]


class BookingManagement(orm.Model):
    _name = 'booking.management'

    _inherit = 'res.partner.address.contact'

    _description = 'Booking management'

    _columns = {
        'guests': fields.integer('Number of guests', required=True),
        'check_in': fields.date('From', required=True),
        'check_out': fields.date('To', required=True),
        'special_requests': fields.text('Special requests')
    }
