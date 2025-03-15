import minibase

db = minibase.Database()

def seed_circuit_schedule():
	db.table('circuit_schedule').record.create(
		['P', 'T', '01001', 'DWG-001', '100', '3-1/C', '250KCMIL',
		'TC/1', '480V','2000V','Panel A1','Panel B1','DB-01001'
		,'','0']
	)

	db.table('circuit_schedule').record.create(
		['P',
		'T',
		'02001',
		'DWG-002',
		'100',
		'3-1/C',
		'250KCMIL',
		'TC/1',
		'480V',
		'2000V',
		'Panel A2',
		'Panel B2',
		'DB-02001',
		'',
		'0']
	)

	db.table('circuit_schedule').record.create(
		['P',
		'T',
		'03001',
		'DWG-003',
		'100',
		'3-1/C',
		'250KCMIL',
		'TC/1',
		'480V',
		'2000V',
		'Panel A3',
		'Panel B3',
		'DB-03001',
		'',
		'0']
	)

	db.table('circuit_schedule').record.create(
		['P',
		'T',
		'04001',
		'DWG-004',
		'100',
		'3-1/C',
		'250KCMIL',
		'TC/1',
		'480V',
		'2000V',
		'Panel A4',
		'Panel B4',
		'DB-04001',
		'',
		'0']
	)

	db.table('circuit_schedule').record.create(
		['P',
		'T',
		'05001',
		'DWG-005',
		'100',
		'3-1/C',
		'250KCMIL',
		'TC/1',
		'580V',
		'2000V',
		'Panel A5',
		'Panel B5',
		'DB-05001',
		'',
		'0']
	)