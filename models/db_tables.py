import datetime


db.define_table('courses',
	Field('code', 'string', required=True, notnull=True),
	Field('name', 'string'),
	Field('description', 'string'),
	Field('prerequisites', 'string', 'reference courses',
		requires=IS_IN_DB(db, 'courses.code', '%(name)s')),
	Field('instructor', 'string'),
	Field('capacity', 'integer', default=20, requires=IS_NOT_EMPTY()),
	Field('scheduleId', 'integer',
		'reference courseschedule',
		requires=IS_IN_DB(db, 'courseschedule.id', '%(days)s: %(startTime)s - %(endTime)s')),
	Field('num_registered', 'integer', default=0),
	primarykey=['code']
	)

db.define_table('rooms',
	Field('code', 'string', required=True, notnull=True),
	primarykey=['code'])


db.define_table('courseschedule',
	Field('id', 'integer'),
	Field('days', 'string'),
	Field('startTime', 'time', default=datetime.time(0,0)),
	Field('endTime', 'time', default=datetime.time(0,0)),
	Field('RoomNo', 'string', 'reference rooms', requires=IS_IN_DB(db, 'rooms.code', '%(code)s') )
	)
db.define_table('studentreg',
	Field('id', 'integer'),
	Field('studentid', 'integer','reference students',requires=IS_IN_DB(db, 'students.id', '%(name)s')),
	Field('courseid', 'integer', 'reference courses', requires=IS_IN_DB(db, 'courses.code', '%(name)s')),
	primarykey=['id']
	)
