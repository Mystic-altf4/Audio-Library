from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from playsound import playsound
import os
import a
from werkzeug.utils import secure_filename
app = Flask(__name__)

script_dir = os.path.dirname(__file__)

filenames = ['ArcadeTime.mp3', "ArcadeSpeaker.mp3", 'BurnandSuffer.mp3', "sufferspeaker.mp3", 'CatchyMenu.mp3',"menu.mp3","Epic_Win.mp3", "WinSpeaker.mp3", "ntldlnlnss.mp3", "null.mp3","StartOfATale.mp3", "StartSpeaker.mp3","woods.mp3","WoodsSpeaker.mp3","CasanovaROCK.mp3","casanovaloud.mp3"]
file_paths = {filename: os.path.join(script_dir, 'static', 'sounds', filename) for filename in filenames}
# Set the upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
uploaded = []
@app.route("/",methods=["POST", "GET"])
def anasayfa():
    global uploaded
    uploaded = os.listdir("C:/Users/User/Desktop/folders/vsc/mezuniyet/static/uploads")
    return render_template("index.html", uploaded=uploaded)
@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(directory='static/sounds', path=filename, as_attachment=True)
@app.route("/upload", methods=["POST", "GET"])
def upload_file():
    if request.method == "POST":
        # Check if the file part exists

        print(request.files)  # Debugging: Show what's in request.files
        print(request.form)   # Debugging: Show what's in request.form

        if 'file' not in request.files:
            return "No file part"
        
        file = request.files['file']
        
        # Check if the file has a valid filename
        if file.filename == '':
            return "No selected file"
        
        # Save the file to the upload folder
        if file:
            filename = secure_filename(file.filename)  # Secure the filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            uploaded.append(filepath)
            

            return f"File uploaded successfully: {filename}"
        
    return render_template("upload.html")


@app.route("/toggle_action", methods=["POST"])
def toggle_action():
    toggle_state = request.form.get("toggle")
    if toggle_state == "on":
        print("Speaker is ON")
        return render_template("speaker.html")
        # Add your logic here, e.g., enable a feature, play a sound, etc.
    else:
        # Toggle is off (unchecked), perform an alternative action
        print("Speaker is OFF")
        return render_template("index.html")
@app.route("/upload_action", methods=["POST"])
def upload_action():
    upload_state = request.form.get("upcheck")
    if upload_state == "on":
        print("UPLOAD is ON")
        return render_template("upload.html")
        # Add your logic here, e.g., enable a feature, play a sound, etc.
    else:
        # Toggle is off (unchecked), perform an alternative action
        print("Speaker is OFF")
        return render_template("index.html")
@app.route("/audio_action", methods=["POST"])
def audio_action():
    audio_state = request.form.get("audio")
    if audio_state == "on":
        print("Audio is ON")
        x = a.l()
        print(x)
        if x == "Arcade Time":
            return redirect(url_for("play_arcade"))
        elif x == "Burn and Suffer":
            return redirect(url_for("play_suffer"))
        elif x == "Epic Quest Fail":
            return redirect(url_for("play_menu"))
        elif x == "Epic Win":
            return redirect(url_for("play_win"))
        elif x == "Start Of A Tale":
            return redirect(url_for("play_start"))
        elif x == "Untold Loneliness":
            return redirect(url_for("play_null"))
        elif x == "Sleeping Tragedies":
            return redirect(url_for("play_lost"))
        elif x == "Casanova Rock":
            return redirect(url_for("play_casanova"))
        else:
            print("This Song Doesn't Exist!")
        # Add your logic here, e.g., enable a feature, play a sound, etc.
    else:
        # Toggle is off (unchecked), perform an alternative action
        print("Audio is OFF")
    return render_template("index.html")
@app.route("/playone",methods = ["POST","GET"])
def play_win():
    playsound(file_paths["Epic_Win.mp3"])
    return render_template("index.html")
@app.route("/playoneloud",methods = ["POST","GET"])
def play_win_speaker():
    playsound(file_paths["WinSpeaker.mp3"])
    return render_template("speaker.html")
@app.route("/playtwo",methods = ["POST","GET"])
def play_arcade():
    playsound(file_paths["ArcadeTime.mp3"])
    return render_template("index.html")
@app.route("/playtwoloud",methods = ["POST","GET"])
def play_arcade_speaker():
    playsound(file_paths["ArcadeSpeaker.mp3"])
    return render_template("speaker.html")
@app.route("/playthree",methods = ["POST","GET"])
def play_suffer():
    playsound(file_paths["BurnandSuffer.mp3"])
    return render_template("index.html")
@app.route("/playthreeloud",methods = ["POST","GET"])
def play_suffer_speaker():
    playsound(file_paths["sufferspeaker.mp3"])
    return render_template("speaker.html")
@app.route("/playfour",methods = ["POST","GET"])
def play_null():
    playsound(file_paths["ntldlnlnss.mp3"])
    return render_template("index.html")
@app.route("/playfourloud",methods = ["POST","GET"])
def play_null_speaker():
    playsound(file_paths["null.mp3"])
    return render_template("speaker.html")
@app.route("/playfive",methods = ["POST", "GET"])
def play_menu():
    playsound(file_paths["CatchyMenu.mp3"])
    return render_template("index.html")
@app.route("/playfiveloud",methods = ["POST","GET"])
def play_menu_speaker():
    playsound(file_paths["menu.mp3"])
    return render_template("speaker.html")
@app.route("/playsix", methods = ["POST", "GET"])
def play_start():
    playsound(file_paths["StartOfATale.mp3"])
    return render_template("index.html")
@app.route("/playsixloud",methods = ["POST","GET"])
def play_start_speaker():
    playsound(file_paths["StartSpeaker.mp3"])
    return render_template("speaker.html")
@app.route("/playseven", methods = ["POST", "GET"])
def play_lost():
    playsound(file_paths["woods.mp3"])
    return render_template("index.html")
@app.route("/playsevenloud",methods = ["POST","GET"])
def play_lost_speaker():
    playsound(file_paths["WoodsSpeaker.mp3"])
    return render_template("speaker.html")
@app.route("/playeight",methods = ["POST","GET"])
def play_casanova():
    playsound(file_paths["CasanovaROCK.mp3"])
    return render_template("index.html")
@app.route("/playeightloud",methods = ["POST","GET"])
def play_casanova_speaker():
    playsound(file_paths["casanovaloud.mp3"])
    return render_template("speaker.html")
@app.route("/playupload",methods = ["POST","GET"])
def play_upload():
    tam_dosya_yolu = os.path.join(script_dir, uploaded[0])
    playsound(tam_dosya_yolu)
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)