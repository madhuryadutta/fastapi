## 📦 Repository Archived

> ⚠️ **Status: Archived / Learning Project**

This project was created as part of my **learning journey** while exploring a new **framework / language / feature**.

The learning phase is now **complete**, and I am now focusing on **real-world projects and production work**.

This repository will remain available for **reference and learning purposes** (and memories 😄).

⚡ **Note:** No further updates or maintenance will be made to this repository.
---

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
