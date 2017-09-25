from celery import Celery

app = Celery('celery_project',
             broker='redis://localhost',
             backend='redis://localhost',
             include=['celery_project.tasks']
             )
app.config_from_object('config')

if __name__ == '__main__':
    app.start()
