from flask import Flask, render_template, request, jsonify
from model_prediction import *

app = Flask(__name__)

text=""
predicted_emotion=""
predicted_emotion_img_url=""

@app.route("/")
def home():
    entries = show_entry()
    return render_template("index.html", entries=entries)
    

@app.route("/predict-emotion", methods=["POST"])
def predict_emotion():
    input_text = request.json.get("text")
    if not input_text:
        return jsonify({
            "status": "error",
            "message": "Please enter some text to predict emotion!"
        }), 400
    else:
        predicted_emotion, predicted_emotion_img_url = predict(input_text)                         
        return jsonify({
            "data": {
                "predicted_emotion": predicted_emotion,
                "predicted_emotion_img_url": predicted_emotion_img_url
            },
            "status": "success"
        }), 200
        
#Write the code for API here
def show_entry():
    day_entry_list = pd.read_csv("static/assets/data_files/data_entry.csv")
    day_entry_list = day_entry_list.iloc[::-1]

    date1 = (day_entry_list['date'].values[0])
    date2 =(day_entry_list['date'].values[1])
    date3 = (day_entry_list['date'].values[2])

    entry1 = day_entry_list['text'].values[0]
    entry2 = day_entry_list['text'].values[1]
    entry3 = day_entry_list['text'].values[2]

    emotion1=day_entry_list['emotion'].values[0]
    emotion2=day_entry_list['emotion'].values[1]
    emotion3=day_entry_list['emotion'].values[2]

    emotion_url_1=""
    emotion_url_2=""
    emotion_url_3=""

    for key, value in emo_code_url.items():
        if key==emotion1:
            emotion_url_1 = value[0]
        if key==emotion2:
            emotion_url_2 = value[1]
        if key==emotion3:
            emotion_url_3 = value[2]
    return[
        {
            "date": date1, 
            "entry": entry1,
            "emotion": emotion1,
            "emotion_url": emotion_url_1
        },
        {
        
            "date": date2,
            "entry": entry2,
            "emotion": emotion2,
            "emotion_url": emotion_url_2
        },
        {
            "date": date3,
            "entry": entry3,
            "emotion": emotion3,
            "emotion_url": emotion_url_3
        },
        ]




                
if __name__ == "__main__":
    app.run(debug=True)

