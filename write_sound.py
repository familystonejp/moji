import speech_recognition as sr
r = sr.Recognizer()
with sr.AudioFile("audio.wav") as source:
    audio = r.record (source, duration=226)
print ("音声をテキストに変換中。しばらくお待ちください。")

try:
    result = r.recognize_google(audio, language='ja-JP')
    print ("変換が完了しました。")
    print ("結果")
    print ("『"+result+"』")
except sr.RequestError:
    print ("リクエストエラーが発生しました。\n処理を終了します。")
except sr.UnknownValueError:
    print ("正しく読み込みができませんでした。\n別の動画を試してください。")                 

