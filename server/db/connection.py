import minibase

db = minibase.Database()

db.table('users').create(
  columns=[
    ['first_name',      'text'],
    ['last_name',       'text'],
    ['username',        'text'],
    ['email',           'text'],
    ['password_digest', 'text'],
  ]
)

db.table('circuit_schedule').create(
  columns=[
    ['designator', 'text'],
    ['equipment',  'text'],
    ['tag',        'text'],
    ['dwg',        'text'],
    ['length',     'text'],
    ['conductors', 'text'],
    ['size',       'text'],
    ['type',       'text'],
    ['sys_volts',  'text'],
    ['insulation', 'text'],
    ['from_equip', 'text'],
    ['to_equip',   'text'],
    ['via',        'text'],
    ['comments',   'text'],
    ['rev',        'text']
  ]
)