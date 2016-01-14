from osv import orm, fields, osv


class booking_info(orm.Model):
    _name = 'room.info'
    # _inherit = 'res.partner'

    _description = 'Room info'

    _columns = {
        # 'rooms_id': fields.one2many('travel.room', 'hostel_id', 'Rooms'),
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

    '''
    def onchange_room_type(self, cr, uid, ids, room_type, context=None):
        value = {'parent_id': False}
        if room_type:
            room = self.pool.get('room.info').browse(cr, uid, room_type)
            value['room_type'] = room.id
        return {'value': value}
    '''

    # _sql_constraints = [('rooms_id_uniq', unique('rooms_id'), 'Rooms must be unique!')]
    _constraints = [(_check_name, 'Please avoid spam in rooms_id!', ['name'])]

class booking_management(orm.Model):
    _name = 'booking.management'

    _description = 'Booking management'

    _columns = {
        'first_name': fields.char('First name', required=True),
        'last_name': fields.char('Last name', required=True),
        'tel': fields.char('Telephone number', size=32, readonly=False, required=True),
        'guests': fields.integer('Number of guests', required=True),
        'email': fields.char('Email'),
        'check_in': fields.date('From', required=True),
        'check_out': fields.date('To', required=True),
        'special_requests': fields.text('Special requests'),
        'name': fields.many2one('room.info', 'Room', required=True)
    }

    def _check_name(self, cr, uid, ids, context=None):
        for booking_management in self.browse(cr, uid, ids, context=None):
            if 'spam' in booking_management.name:
                return False
        return True
