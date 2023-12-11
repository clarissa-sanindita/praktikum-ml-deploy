import time
import os
import cv2
import uuid
import numpy as np
from PIL import Image
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model

"""
Konfigurasi dan Inisialisasi
- `CLASS_DICT`: Sebuah dictionary yang memetakan kategori gambar ke label numerik. Contoh kategori adalah 'Paper', 'Rock', dan 'Scissors'.
- `LABELS`: Daftar label kategori yang diambil dari kunci `CLASS_DICT`.
- `ALLOWED_EXTENSIONS`: Set ekstensi file yang diperbolehkan untuk unggahan.
- `UPLOAD_FOLDER`: Lokasi direktori tempat file yang diunggah akan disimpan.
- `MODEL_FOLDER`: Lokasi direktori tempat model akan digunakan.
"""

CLASS_DICT              = {"Paper": 0, "Rock": 1, "Scissors": 2} # TO CHANGE
LABELS                  = list(CLASS_DICT.keys())
ALLOWED_EXTENSIONS      = {'png', 'jpg', 'jpeg'}
UPLOAD_FOLDER           = 'static/uploads/'
MODEL_FOLDER            = 'static/model/CNN.h5'


"""
Inisialisasi Aplikasi Flask
Aplikasi Flask diinisialisasi dengan batas ukuran file maksimum yang didefinisikan.
"""
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024 


"""
Fungsi `add_header`
- Fungsi ini ditetapkan untuk dipanggil setelah setiap request.
- Mengatur header HTTP untuk mencegah caching di sisi klien.
"""
@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


"""
Rute `/`
Rute utama yang merender template `predict.html`.
"""
@app.route("/")
def index():
    return render_template('predict.html')


"""
Rute `/predict_result`
- Rute ini mengelola logika untuk prediksi gambar.
- Mengambil model yang dipilih dari form request.
- Menyimpan file yang diunggah ke `UPLOAD_FOLDER`.
- Membuka dan memproses gambar yang diunggah menggunakan OpenCV dan PIL.
- Melakukan prediksi menggunakan model yang dimuat.
- Mengembalikan hasil prediksi ke fungsi `predict_result`.
"""
@app.route('/predict_result', methods=['POST'])
def predict():
    chosen_model = request.form['select_model']
    model_dict = {'CNNModel': MODEL_FOLDER} 

    if chosen_model in model_dict:
        model = load_model(model_dict[chosen_model])
    else:
        return "Model not found", 404

    file_path = os.path.join(UPLOAD_FOLDER, 'temp.jpg')
    file = request.files["file"]
    file.save(file_path)

    img = cv2.cvtColor(np.array(Image.open(file_path)), cv2.COLOR_BGR2RGB)
    img = np.expand_dims(cv2.resize(img, model.layers[0].input_shape[0][1:3] \
    if not model.layers[0].input_shape[1:3] else model.layers[0].input_shape[1:3])
    .astype('float32') / 255, axis=0)
    
    start = time.time()
    pred = model.predict(img)[0]
    runtimes = round(time.time()-start,4)
    respon_model = [round(elem * 100, 2) for elem in pred]

    return predict_result(chosen_model, runtimes, respon_model, 'temp.jpg')

"""
Fungsi `predict_result`
- Menerima hasil prediksi dan menyiapkannya untuk ditampilkan.
- Mengidentifikasi kategori prediksi dengan probabilitas tertinggi.
- Merender template `predict_result.html` dengan data prediksi.

"""
def predict_result(model, run_time, probs, img):
    class_list = {'paper': 0, 'rock': 1, 'scissors': 2}
    idx_pred = probs.index(max(probs))
    labels = list(class_list.keys())
    return render_template('predict_result.html', labels=labels,
                            probs=probs, model=model, pred=idx_pred,
                            run_time=run_time, img=img)

if __name__ == "__main__": 
    app.run(debug=True, host='127.0.0.1', port=5000)
