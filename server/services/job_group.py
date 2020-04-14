""" Defines the JobGroup service """

from repositories import JobGroupRepository


class JobGroupService:
    """ The service for the JobGroup """

    @staticmethod
    def create_if_not_exists(data_frame):
        """ Create a JobGroup if not exists """
        try:
            job_groups = data_frame['job_group'].drop_duplicates()
            for name in job_groups.values.tolist():
                job_group = JobGroupRepository.get(name=name)
                if job_group is None:
                    new_job_group = JobGroupRepository.create(name=name)

        except Exception as e:
            raise e
