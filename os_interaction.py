import os
import json
import platform


#if platform.system() == 'Linux':
obj = {
	'OS': platform.system(),
	'Relese': platform.release(),
	'CPU': len(os.sched_getaffinity(0)),
	'Architecture': platform.processor(),
	'Node': platform.node()
	}

with open('os_report.json', 'w') as fh:
	json.dump(obj, fh)
