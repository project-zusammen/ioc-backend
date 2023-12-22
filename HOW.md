### ENV
```bash
python3 -m venv venv --upgrade-deps
. venv/bin/activate
```
### INSTALL
```bash
pip install -r ./requirements.txt 
```
### PLAY
```bash
flask db --help             # migration
flask run --debug
```
### GENERATED DB
```bash
instance/app.db             # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
sqlite3 instance/app.db
.tables
INSERT INTO user (id, name) VALUES (1, Phil)
INSERT INTO user (id, name) VALUES (2, Dom)
.exit
```
### ENDPOINT
```
http://localhost:5000/user/1
http://localhost:5000/user/2
```
