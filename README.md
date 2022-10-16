1) Use this command:
git clone https://github.com/21TeeKayy/NFT

2) Go to "NFT" directory
cd NFT

3) Connect your database by changing this part of the code:
database="postgres", user = "postgres", password = "04120412", host = "127.0.0.1", port = "5433"

4) Create virtual environment:
python -m venv venv

5) Activate venv:
.\venv\Scripts\activate

6) Install this
pip install -r requirements.txt

7) Go to "src" directory
cd src

8) Run our app
flask --app p.py run
