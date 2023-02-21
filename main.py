from flask import Flask, request
import traceback

# pipeline:
# 1. Coref resolution
# 2. NER (xem loại từ của các từ (Nouns, Verb, ...))
# 3. Entity linking (nối với wiki-id để xác định loại từ (VD như Humans, City,...))
# 4. Co-occurence graph - check sự tương quan
# 4. Information extraction (2 cách: - Rule based hoặc NLP model)


app = Flask(__name__)


@app.route('/')
def information_extraction():
    try:
        print("Hello")
        text = request.args.get('text', None)
        if not text:
            return "Missing text parameter."
        return "server running!"

    except Exception as e:
        return 'An error has occured:' + str(e) + " " + traceback.format_exc()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
