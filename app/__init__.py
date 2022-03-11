import os
import app 

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.ge("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False