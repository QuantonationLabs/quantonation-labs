from pathlib import Path
from streamlit.testing.v1 import AppTest

at=AppTest.from_file(str(Path(__file__).with_name('app.py'))).run(timeout=30)
assert not at.exception,at.exception
at.slider[0].set_value(.5).run()
assert not at.exception and any(m.value=='50.0%' for m in at.metric)
at.slider[0].set_value(1.0).run()
assert not at.exception and any(m.value=='100.0%' for m in at.metric)
at.slider[1].set_value(1.2).run()
assert not at.exception
print('PASS: public showcase controls, analytical half/whole flip and local science view')
