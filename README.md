# flask-react-seed
## development
1. Setup virtualenv

        virtualenv -p `which python3` env
        source env/bin/activate

2. Install requirements

        pip install -U pip
        pip install -r requirements.txt
        pip install -r requirements_dev.txt

3. Run docker

        docker-compose -f docker-compose-dev.yml up

4. Run migrations

        python manage.py db upgrade

5. Run api

        python manage.py runserver

6. Run py.test via pytest-watch (pytest-watch re-runs py.test when a file in project changes)

        ptw src

## Heroku
1. Login to [Heroku Dashboard](http://dashboard.heroku.com)
2. Create new application
3. Go to project directory on your machine and execute

        heroku login
        heroku git:remote -a <your-app-name>
        heroku buildpacks:add --index 1 heroku/nodejs
        heroku buildpacks:add --index 2 heroku/python

4. Add addons

        heroku addons:create heroku-postgresql:hobby-dev

5. Setup environment variables

        heroku config:set WEB_CONCURRENCY=3
        heroku config:set API_CONFIG=config.Production
        heroku config:set SECRET_KEY=<random-string>

6. Run migrations

        heroku run python manage.py db upgrade

7. Push app to your newly created heroku instance

        git push -u heroku master
