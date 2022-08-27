sudo apt-get install puthon3.8-venv
python3 -m venv /home/banzai/hillel/env
source /home/banzai/hillel/env/bin/activate
pip3 install requests
pip3 install python-telegram-bot
cd /home/banzai/hillel/projects/ban7ai_23-07-2022
pip3 freeze > requirements.txt
deactivate
