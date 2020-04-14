""" Defines the JobGroup repository """

from models import JobGroup


class JobGroupRepository:
    """ The repository for the user model """

    @staticmethod
    def get(name):
        """ Query a JobGroup by name """
        job_group = JobGroup.query.filter_by(name=name).one_or_none()
        return job_group

    @staticmethod
    def create(name):
        """ Create a new JobGroup """
        wage = 0
        if name == 'A':
            wage = 20
        elif name == 'B':
            wage = 30
        job_group = JobGroup(name=name, wage=wage)
        return job_group.save()
