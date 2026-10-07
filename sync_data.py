"""Edit data.json, then run: python3 sync_data.py"""
import json
from pathlib import Path
p = Path(__file__).resolve().parent
data = json.loads((p / 'data.json').read_text(encoding='utf-8'))
(p / 'data.js').write_text('window.STATS_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n', encoding='utf-8')
print('Updated data.js')
