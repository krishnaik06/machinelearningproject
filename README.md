### Start Machine Learning Project

### Software And Tools Requirements:
1. [Github Account](https://github.com)
2. [Heroku Account](https://heroku.com)
3. [VS Code IDE](https://code.visualstudio.com/)
4. [GIT CLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line) 

Creating Conda Environment 

```
conda create -p venv python==3.7 -y
```

```
conda activate venv/
```

```
Create requirement.txt
Write Down You Libraries name 
```
To Add files To Git
```
git add .
```
Or
```
git add File_name
```
> Note: To ignore file or folder from git we can write name of the file/folder in .gitignore file

To send changes/version  to github
```
git push origin main
```


To Check remote url
```
git remote -v
```

To Check Branch
```
git branch
```

To Set up CI/CD pipeline in heroku we need 3 information 

1. Heroku_Email=krishnaik06@gmail.com
2. Heroku_API_Key=454e3899-0522-43e0-8d0d-0fd83eda40ce
3. Heroku_APP_NAME=air-foil

BUILD DOCKER Images

```
docker build -t <image_name>:<tagname> .
```
> Note:Image name for docker must be lowercase

Check image that got created, To list docker images
```
docker images
```

Run Docker Images
```
docker run -p 5000:5000 -e PORT=5000 fe6ef5c7a427
```
To check running container
```
docker ps
```
Stop Docker container
```
docker stop <container-id>
```
Set up setup.py file
```
python setup.py install
```
Or
```
pip install -r requirements.txt
```