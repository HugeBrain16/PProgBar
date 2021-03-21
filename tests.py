import pprogbar, os

def test_create():
	x = pprogbar.Progger(200,20,30,100,0x0000FF)
	x.create('progbar-test.png')
	assert os.path.exists('progbar-test.png') == True, "Failed to create progress bar"