def get_dataset(ind):
	s1 = [
		"cincinny cantik bngt aku sukaa tp syang kbesarn aqu psen satu diksh bonus mkch toko kwan abadi mkch lazada",
		"terimakasih barang realfix yaa sukaa",
		"sen xl kok dtg m gmna gag tepat kali",
		"barang sesuai datangy lama bget",
		"alhamdulilah barang sampai enakk trims seller kurir lazada",
		"bahan lembut nyaman pakai",
		"jual yg amanah mba biar berkah hidup minta krim minta wrna kirim wrna alhasil tu brg gua buang deh tong sampah anggap aja w sedekah sama emis nyesell bgt belanja toko bgi yg mau blanja toko mending jangan deh drpd kecewa",
		"sangat kcewa jahit beranta mau putus",
		"packing bagus sayang tidk sesuai warna pesan",
		"terima kasih udah jual hijab bagus harga murah sukses"
	]
	s2 = [
		"cincinny cantik bngt aku sukaa tp syang kbesarn aqu psen satu diksh bonus mkch toko kwan abadi mkch lazada",
		"terimakasih barangnya realfix yaa sukaa",
		"pesen xl kok dtg m gmna gag tepat kali",
		"barang sesuai datangy lama bget",
		"alhamdulilah barang sampai enakk trims seller kurir lazada",
		"bahannya lembut nyaman pakai",
		"jualan yg amanah mba biar berkah hidupnya mintanya krimnya minta wrna kirimnya wrna alhasil tu brg gua buang deh tong sampah anggap aja w sedekah sama pengemis nyesell bgt belanja toko bgi yg mau blanja ditoko mending jangan deh drpd kecewa",
		"sangat kcewa jahitannya berantakan mau putus",
		"packing bagus sayangkan tidk sesuai warna pesan",
		"terima kasih udah jual hijab bagus harga murah sukses"
	]

	s3 = [
		"cincinny cantik bngt aku sukaa tp syang kbesarn aqu psen satu diksh bonus mkch ya toko kwan abadi mkch lazada",
		"terimakasih barangnya realfix yaa saya sukaa",
		"pesen xl kok yang dtg m gmna ini gag tepat kali",
		"barang tidak sesuai datangy lama bget",
		"alhamdulilah barang sudah sampai enakk trims seller kurir lazada",
		"bahannya lembut nyaman untuk di pakai",
		"jualan itu yg amanah mba biar berkah hidupnya mintanya apa krimnya apa minta wrna apa kirimnya wrna apa alhasil tu brg gua buang deh ke tong sampah anggap aja w sedekah sama pengemis nyesell bgt belanja di toko ini bgi yg mau blanja ditoko ini mending jangan deh drpd kecewa"
		"saya sangat kcewa jahitannya berantakan mau putus lagi",
		"packing bagus tapi di sayangkan tidk sesuai warna yang di pesan",
		"terima kasih udah jual hijab bagus dengan harga murah sukses"	
	]

	s4 = [
		"cincinny cantik bngt aku sukaa tp syang kbesarn aqu psen satu diksh bonus mkch ya toko kwan abadi mkch lazada",
		"terimakasih barang realfix yaa saya sukaa",
		"sen xl kok yang dtg m gmna ini gag tepat kali",
		"barang tidak sesuai datangy lama bget",
		"alhamdulilah barang sudah sampai enakk trims seller kurir lazada",
		"bahan lembut nyaman untuk di pakai",
		"jual itu yg amanah mba biar berkah hidup minta apa krim apa minta wrna apa kirim wrna apa alhasil tu brg gua buang deh ke tong sampah anggap aja w sedekah sama emis nyesell bgt belanja di toko ini bgi yg mau blanja toko ini mending jangan deh drpd kecewa",
		"saya sangat kcewa jahit beranta mau putus lagi",
		"packing bagus tapi di sayang tidk sesuai warna yang di pesan",
		"terima kasih udah jual hijab bagus dengan harga murah sukses"
	]
	s5 = [
		"cincinny cantik bngt aku sukaa tp syang kbesarn aqu psen satu diksh bonus mkch toko kwan abadi mkch lazada",
		"terimakasih barang realfix yaa saya sukaa",
		"sen xl kok yang dtg m gmna gag tepat kali",
		"barang sesuai datangy lama bgettt",
		"alhamdulilah barang sampai enakk trims seller kurir lazada",
		"bahan lembut nyaman pakai",
		"jual yg amanah mba biar berkah hidup minta krim minta wrna kirim wrna alhasil tu brg gua buang deh tong sampah anggap aja w sedekah sama emis nyesell bgt belanja toko ini bgi yg mau blanja toko mending jangan deh drpd kecewa",
		"sangat kcewa jahit beranta mau putus",
		"packing bagus tapi sayang tidk sesuai warna pesan",
		"terima kasih udah jual hijab bagus harga murah sukses"
	]
	s6 = [
		"cincinnya cantik banget aku suka tapi sayang besaran aku pesan satu dikasih bonus makasih toko akan badai makasih lazada",
		"terimakasih barang realpict ya suka",
		"pesan xl kok datang m gimana tidak tepat kali",
		"barang sesuai datang lama banget",
		"alhamdulillah barang sampai enak terimakasih seller kurir lazada",
		"bahan lembut nyaman pakai",
		"jual yang amanah mbak biar berkah hidup minta kirim minta warna kirim warna alhasil itu barang gua buang deh tong sampah anggap aja gua sedekah sama seems nyesel banget belanja toko bagi yang mau belanja toko mending jangan deh daripada kecewa",
		"sangat kecewa jahit beneran mau putus",
		"packing bagus sayang tidak sesuai warna pesan",
		"terima kasih sudah jual hijab bagus harga murah sukses"
	]
	s7 = [
		"cincinnya cantik banget aku suka tapi sayang besaran aku pesan satu dikasih bonus makasih toko akan badai makasih lazada",
		"terimakasih barangnya realpict ya suka",
		"pesen xl kok datang m gimana tidak tepat kali",
		"barang sesuai datang lama banget",
		"alhamdulillah barang sampai enak terimakasih seller kurir lazada",
		"bahannya lembut nyaman pakai",
		"jualan yang amanah mbak biar berkah hidupnya mintanya kirimnya minta warna kirimnya warna alhasil itu barang gua buang deh tong sampah anggap aja gua sedekah sama pengemis nyesel banget belanja toko bagi yang mau belanja ditoko mending jangan deh daripada kecewa",
		"sangat kecewa jahitannya berantakan mau putus",
		"packing bagus sayangkan tidak sesuai warna pesan",
		"terima kasih sudah jual hijab bagus harga murah sukses",
	]
	s8 = [
		"cincinnya cantik banget aku suka tapi sayang besaran aku pesan satu dikasih bonus makasih iya toko akan badai makasih lazada",
		"terimakasih barangnya realpict ya saya suka",
		"pesen xl kok yang datang m gimana ini tidak tepat kali",
		"barang tidak sesuai datang lama banget",
		"alhamdulillah barang sudah sampai enak terimakasih seller kurir lazada",
		"bahannya lembut nyaman untuk di pakai",
		"jualan itu yang amanah mbak biar berkah hidupnya mintanya apa kirimnya apa minta warna apa kirimnya warna apa alhasil itu barang gua buang deh ke tong sampah anggap aja gua sedekah sama pengemis nyesel banget belanja di toko ini bagi yang mau belanja ditoko ini mending jangan deh daripada kecewa",
		"saya sangat kecewa jahitannya berantakan mau putus lagi",
		"packing bagus tapi di sayangkan tidak sesuai warna yang di pesan",
		"terima kasih sudah jual hijab bagus dengan harga murah sukses"
	]
	s9 = [
		"cincinnya cantik banget aku suka tapi sayang besaran aku pesan satu dikasih bonus makasih iya toko akan badai makasih lazada",
		"terimakasih barang realpict ya saya suka",
		"pesan xl kok yang datang m gimana ini tidak tepat kali",
		"barang tidak sesuai datang lama banget",
		"alhamdulillah barang sudah sampai enak terimakasih seller kurir lazada",
		"bahan lembut nyaman untuk di pakai",
		"jual itu yang amanah mbak biar berkah hidup minta apa kirim apa minta warna apa kirim warna apa alhasil itu barang gua buang deh ke tong sampah anggap aja gua sedekah sama seems nyesel banget belanja di toko ini bagi yang mau belanja toko ini mending jangan deh daripada kecewa",
		"saya sangat kecewa jahit beneran mau putus lagi",
		"packing bagus tapi di sayang tidak sesuai warna yang di pesan",
		"terima kasih sudah jual hijab bagus dengan harga murah sukses"
	]
	s10 = [
		"cincinnya cantik banget aku suka tapi sayang besaran aku pesan satu dikasih bonus makasih toko akan badai makasih lazada",
		"terimakasih barang realpict ya saya suka",
		"pesan xl kok yang datang m gimana tidak tepat kali",
		"barang sesuai datang lama bgettt",
		"alhamdulillah barang sampai enak terimakasih seller kurir lazada",
		"bahan lembut nyaman pakai",
		"jual yang amanah mbak biar berkah hidup minta kirim minta warna kirim warna alhasil itu barang gua buang deh tong sampah anggap aja gua sedekah sama seems nyesel banget belanja toko ini bagi yang mau belanja toko mending jangan deh daripada kecewa",
		"sangat kecewa jahit beneran mau putus",
		"packing bagus tapi sayang tidak sesuai warna pesan",
		"terima kasih sudah jual hijab bagus harga murah sukses"
	]



	d1 = dataset("D1","Normalisasi - Stopword Removal - Stemming",1,s1)
	d2 = dataset("D2","Normalisasi - Stopword Removal",2,s2)
	d3 = dataset("D3","Normalisasi",3,s3)
	d4 = dataset("D4","Normalisasi - Stemming",4,s4)
	d5 = dataset("D5","Stopword Removal - Stemming",1,s5)

	d6 = dataset("D6","Normalisasi - Stopword Removal - Stemming - WordCorrection",1,s6)
	d7 = dataset("D7","Normalisasi - Stopword Removal - WordCorrection",2,s7)
	d8 = dataset("D8","Normalisasi - WordCorrection",3,s8)
	d9 = dataset("D9","Normalisasi - Stemming - WordCorrection",4,s9)
	d10 = dataset("D10","Stopword Removal - Stemming - WordCorrection",1,s10)

	arr = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]
	return arr[ind]



class dataset:
	def __init__(self,label,preprocess,preprocess_id,sampel):
		self.label = label
		self.preprocess = preprocess
		self.preprocess_id = preprocess_id
		self.sampel = sampel

	def get_json(self):
		return {
			'label':self.informasi,
			'preprocess':self.preprocess,
			'preprocess_id':self.preprocess_id,
			'sampel':self.sampel
		}

