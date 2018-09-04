from flask import Flask,render_template,request,url_for
from regform import RegistrationForm


app = Flask(__name__)



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('success.html'))
    return render_template('new.html', form=form)



if __name__=='__main__':
    app.run(debug=True)
