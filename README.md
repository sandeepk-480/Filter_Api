<h1>Filter API:</h1>
<p>Technologies Used: Python, Django Rest framework</p>
<br>
Filters Data according to the parameters provided in the url. <br>
Load time under 100ms. <br>
Used pagination and Indexing <br>

<h3>Api Endpoints</h3>
- http://127.0.0.1:8000/Api/    (Root url)<br>
- http://127.0.0.1:8000/Api/?ticker=ZS     (data were ticker is equal to 'ZS')<br>
- http://127.0.0.1:8000/Api/?ticker=ZS&column=revenue,gp     (data were ticker is equal to 'ZS' and returns only revenue and gp column)<br>
- http://127.0.0.1:8000/Api/?ticker=ZS&column=revenue,gp&period=5y     (returns past 5 years worth of data)<br>
<br>
How to Use???<br>
<br>
Open any of your code editor, like vs code or pycharm.<br>
open Terminal and run this commands-<br>
Create a seperate Virtual environment (Not must, but recommended). <br>
1- git clone https://github.com/sandeepk-480/Authentication-Project-Assign-.git <br>
2- cd Authentication-Project-Assign <br>
3- pip install -r requirements.txt <br>
4- python manage.py runserver <br>
