 #Now, imagine you are given data from a website that
# has people's CVs. The data comes
# as a list of dictionaries and each
# dictionary looks like this:
#
# { 'user': 'george', 'jobs': ['bar', 'baz', 'qux']}
# e.g. [{'user': 'john', 'jobs': ['analyst', 'engineer']},
#       {'user': 'jane', 'jobs': ['finance', 'software']}]
# we will refer to this as a "CV".

cv = [{'user': 'john', 'jobs': ['analyst', 'engineer']}, {'user': 'jane', 'jobs': ['finance', 'software']},
      {'user': 'majo', 'jobs': ['finance', 'data scientist','head of ops']},]

# 4)
# Create a function called "has_experience_as"
# that has two parameters:
# 1. A list of CV's.
# 2. A string (job_title)
#
# The function should return a list of strings
# representing the usernames of every user that
# has worked as job_title.

def has_experience_as(cv, job_title):
    previous_job_titles = []
    for cv in cv:
        if job_title in cv['jobs']:
            previous_job_titles.append(cv['user'])
    return previous_job_titles
        
print(has_experience_as(cv, 'engineer'))
print(has_experience_as(cv, 'finance'))


# 5)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.


def job_counts(cv):
    number_of_jobs = {}
    for cv in cv:
        for job in cv['jobs']:
            if job in number_of_jobs:
                number_of_jobs[job] += 1
            else:
                number_of_jobs[job] = 1
    return number_of_jobs

print(job_counts(cv))


# 6)
# Create a function, called "most_popular_job"
# that has one parameter: a list of CV's, and
# returns a tuple (str, int) that represents
# the title of the most popular job and the number
# of times it was held by people on the site.
#
# HINT: You should probably use your "job_counts"
# function!
#
# HINT: You can use the method '.items' on
# dictionaries to iterate over them like a
# list of tuples.

def most_popular_job(cv):
    jobs = job_counts(cv)
    most_popular = ("", 0)
    for job, count in jobs.items():
        if count > most_popular[1]:
            most_popular = (job, count)
    return most_popular

print(most_popular_job(cv))
