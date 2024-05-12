import streamlit as st
from PIL import Image
from tensorflow.keras.preprocessing.image import load_img, img_to_array, save_img
from tensorflow.keras.models import model_from_json
import numpy as np
import shutil

import os # inbuilt module
import random # inbuilt module
import webbrowser # inbuilt module

#=================================== Title ===============================
st.title("""
Identificador de Gatos 🐱 o Perros 🐶
	""")

#================================= Title Image ===========================
st.text("""""")
img_path_list = ["static/image_1.jpg",
				"static/image_2.jpg"]
index = random.choice([0,1])
image = Image.open(img_path_list[index])
st.image(
	        image,
	        use_column_width=True,
	    )

#================================= About =================================
st.write("""
## 1️⃣ Sobre la app
	""")
st.write("""
Hola, Bienvenidos a esta actividad.
Es una aplicación de reconocimiento de gatos y perros
	""")
st.write("""
Tienes que cargar las imágenes que quieras identificar
	""")
st.write("""
En caso de que no tengas imágenes, puedes seleccionar alguna de aquí 
	""")

#============================ How To Use It ===============================
st.write("""
## 2️⃣ Como usar la app
	""")
st.write("""
Es muy sencillo!!!
 
- Primero, descarga una imagen de gato 🐈 o perro 🐕!
- Después, búscala desde el explorador de archivos
- Asegurate que has cargado una imagen
- Haz click **👉🏼 Identificar** 

🔘 **NOTA :** *Si cargas otro archivo que no sea una imagen, se mostrará un mensaje de error cuando apretes el boton de Identificar*
	""")

#========================= What It Will Predict ===========================
st.write("""
## 3️⃣ ¿Qué identifica?
	""")
st.write("""
Cualquier imagen que se cargue de perros o gatos
	""")

#======================== Time To See The Magic ===========================
st.write("""
## 👁️‍🗨️ Prueba suerte
	""")

#========================== File Uploader ===================================
img_file_buffer = st.file_uploader("Carga tu imagen aquí 👇🏻")

try:
	image = Image.open(img_file_buffer)
	img_array = np.array(image)
	st.write("""
		Previsualización 👀
		""")
	if image is not None:
	    st.image(
	        image,
	        use_column_width=True
	    )
	st.write("""
		Te queda solo un paso.
		""")
	st.write("""
		**Haz click en '👉🏼 Identificar' ! 😄**
		""")
except:
	st.write("""
		### ❗ No se ha seleccionado ninguna imagen!!!
		""")

#================================= Predict Button ============================
st.text("""""")
submit = st.button("👉🏼 Identificar")

#==================================== Model ==================================
def processing(testing_image_path):
    IMG_SIZE = 50
    img = load_img(testing_image_path, 
            target_size=(IMG_SIZE, IMG_SIZE), color_mode="grayscale")
    img_array = img_to_array(img)
    img_array = img_array/255.0
    img_array = img_array.reshape((1, 50, 50, 1))   
    prediction =loaded_model.predict(img_array)    
    return prediction

def generate_result(prediction):
	st.write("""
	## 🎯 RESULTADO
		""")
	if prediction[0]<0.5:
	    st.write("""
	    	## Es un GATO 🐱!!!
	    	""")
	else:
	    st.write("""
	    	## Es un perro 🐶!!!
	    	""")

#=========================== Predict Button Clicked ==========================
if submit:
	try:
		# save image on that directory
		save_img("temp_dir/test_image.png", img_array)

		image_path = "temp_dir/test_image.png"
		# Predicting
		st.write("👁️ Identificando...")

		model_path_h5 = "model/model.h5"
		model_path_json = "model/model.json"
		json_file = open(model_path_json, 'r')
		loaded_model_json = json_file.read()
		json_file.close()
		loaded_model = model_from_json(loaded_model_json)
		loaded_model.load_weights(model_path_h5)

		loaded_model.compile(loss='binary_crossentropy', metrics=['accuracy'],optimizer='adam')

		prediction = processing(image_path)

		generate_result(prediction)

	except:
		st.write("""
		### ❗ Ups... Algo fue mal
			""")

#=============================== Copy Right ==============================
st.text("""""")
st.text("""""")
st.text("""""")
st.text("""""")
st.text("""""")
st.text("""""")
st.text("""""")
st.text("""""")
st.text("""""")
st.text("""""")
st.write("""
### ©️ Created By Debmalya Sur
	""")
