
python3 manage.py migrate

# one time create admin
#python3 manage.py createsuperuser

# collect statis html and css files
python3 manage.py collectstatic

# deploy locally
python3 manage.py runserver

# optional to set project value
#gcloud config set project gcp-project-253602
gcloud app deploy