<<<<<<< HEAD
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Trang chủ
@app.route('/')
def home():
    return render_template('index.html')  # Phải có templates/index.html

# Route xử lý chat BMI
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    text = data.get('message', '').strip()
    try:
        weight, height = map(float, text.split())
        height_m = height / 100
        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            status = "Thiếu cân"
            risk = "⚠️ Nguy cơ: Suy dinh dưỡng, thiếu năng lượng, hệ miễn dịch yếu."
        elif bmi < 25:
            status = "Bình thường"
            risk = "✅ Bạn có thể trạng tốt, nguy cơ bệnh thấp."
        elif bmi < 30:
            status = "Thừa cân"
            risk = "⚠️ Nguy cơ: Dễ mắc bệnh tim mạch, cao huyết áp, gan nhiễm mỡ."
        else:
            status = "Béo phì"
            risk = "⚠️ Nguy cơ cao: Bệnh tim mạch, tiểu đường type 2, đột quỵ."

        reply = (
            f"📏 Chiều cao: {height} cm\n"
            f"⚖️ Cân nặng: {weight} kg\n"
            f"✅ BMI: {bmi:.2f}\n"
            f"💡 Tình trạng: {status}\n"
            f"{risk}"
        )
    except:
        reply = "❌ Vui lòng nhập đúng: [cân nặng] [chiều cao] (VD: 70 170)"

    return jsonify({"reply": reply})

# Không cần app.run() nếu chạy gunicorn
# Nếu chạy local thì mới cần
if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Trang chủ
@app.route('/')
def home():
    return render_template('index.html')  # Phải có templates/index.html

# Route xử lý chat BMI
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    text = data.get('message', '').strip()
    try:
        weight, height = map(float, text.split())
        height_m = height / 100
        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            status = "Thiếu cân"
            risk = "⚠️ Nguy cơ: Suy dinh dưỡng, thiếu năng lượng, hệ miễn dịch yếu."
        elif bmi < 25:
            status = "Bình thường"
            risk = "✅ Bạn có thể trạng tốt, nguy cơ bệnh thấp."
        elif bmi < 30:
            status = "Thừa cân"
            risk = "⚠️ Nguy cơ: Dễ mắc bệnh tim mạch, cao huyết áp, gan nhiễm mỡ."
        else:
            status = "Béo phì"
            risk = "⚠️ Nguy cơ cao: Bệnh tim mạch, tiểu đường type 2, đột quỵ."

        reply = (
            f"📏 Chiều cao: {height} cm\n"
            f"⚖️ Cân nặng: {weight} kg\n"
            f"✅ BMI: {bmi:.2f}\n"
            f"💡 Tình trạng: {status}\n"
            f"{risk}"
        )
    except:
        reply = "❌ Vui lòng nhập đúng: [cân nặng] [chiều cao] (VD: 70 170)"

    return jsonify({"reply": reply})

# Không cần app.run() nếu chạy gunicorn
# Nếu chạy local thì mới cần
if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 8b518b79e44a13b311eeff63c0eb09eeb58a83b1
