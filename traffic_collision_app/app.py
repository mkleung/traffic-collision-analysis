from flask import Flask, request, render_template
# from model import predict_collision

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        data = request.form.to_dict()

        # data_df = pd.DataFrame([data])
        # prediction = predict_collision(data_df)
        # return render_template('index.html', prediction=prediction)
        return render_template('index.html')
    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)