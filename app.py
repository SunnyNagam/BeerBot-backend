from flask import Flask, request, jsonify, send_file

app = Flask(__name__)
image = None

@app.route('/hello', methods=['GET', 'POST'])
def hello_world():
	if image == None:
		return 'Hello, World!'
	else:
		return send_file('image.jpg', mimetype='image')

@app.route('/pi', methods=['POST'])
def pi():
	pi_data = request.json
	print(f'Recieved from pi: {pi_data}') #--> Value on server {'temp': 100, 'temp_1': 150}
	return jsonify(pi_data)

@app.route('/detect', methods=['POST'])
def detect():
	global image
	image = request.files.get('image', '')
	image.save("image.jpg")
	#image_bytes = Image.open(io.BytesIO(image.read()))
	return 'Recieved image but who knows if it worked'
 
if __name__ == '__main__':
	app.run(host='0.0.0.0')