def get_model(ind):
	m1 = model("M1",0.90309,0.90978,0.89622,0.90295,4552,447,522,4508,'/static/output/d1_acc.png')
	m2 = model("M2",0.90449,0.92652,0.87992,0.90262,4618,351,604,4426,'/static/output/d2_acc.png')
	m3 = model("M3",0.91119,0.91123,0.91232,0.91178,4522,447,441,4589,'/static/output/d3_acc.png')
	m4 = model("M4",0.91079,0.92001,0.90099,0.91040,4575,394,498,4532,'/static/output/d4_acc.png')
	m5 = model("M5",0.90069,0.89710,0.90656,0.901180,4590,376,559,4467,'/static/output/d5_acc.png')
	m6 = model("M6",0.90352,0.91096,0.89574,0.90329,4526,440,524,4502,'/static/output/d1_corrected_acc.png')
	m7 = model("M7",0.90559,0.92245,0.88687,0.90431,4594,375,569,4461,'/static/output/d2_corrected_acc.png')
	m8 = model("M8",0.90839,0.91305,0.90397,0.90849,4536,433,483,4547,'/static/output/d3_corrected_acc.png')
	m9 = model("M9",0.91232,0.93482,0.88758,0.91059,4655,311,565,4461,'/static/output/d4_corrected_acc.png')
	m10 = model("M10",0.90642,0.92236,0.88877,0.90525,4590,376,559,4467,'/static/output/d5_corrected_acc.png')

	arr = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10]
	return arr[ind]

class model:
	def __init__(
		self,
		label,
		akurasi,
		presisi,
		recall,
		f1score,
		tp,
		tn,
		fp,
		fn,	
		path
	):
		self.label = label
		self.akurasi = akurasi
		self.presisi = presisi
		self.recall = recall
		self.f1score = f1score
		self.tp = tp
		self.tn = tn
		self.fp = fp
		self.fn = fn
		self.path = path

	def get_json(self):
		return {
			'label':self.label,
			'akurasi':self.akurasi,
			'presisi':self.presisi,
			'recall':self.recall,
			'f1score':self.f1score,
			'tp':self.tp,
			'tn':self.tn,
			'fp':self.fp,
			'fn':self.fn,
			'path':self.path
		}


	