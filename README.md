# fastapi

pip install fastapi
pip install "uvicorn[standard]"
<!-- pip install requests -->


or

pip install -r requirements.txt

uvicorn main:app --reload 
uvicorn main:app --proxy-headers --reload 

<!-- docker build -t myimage .
docker run -d --name mycontainer -p 80:80 myimage -->

docker build -t fastapi .
docker run -d --name fastapi -p 80:80 fastapi