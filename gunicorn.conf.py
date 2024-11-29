import multiprocessing

# from oc_lettings_site.settings import PORT

# number of worker and threads:
# according to gunicorn docs (https://docs.gunicorn.org/en/stable/design.html#asyncio-workers)
# n workers should be equel to (2 x $num_cores) + 1

# according to Cambring (https://guidebook.devops.uis.cam.ac.uk/notes/gunicorn-tuning/)
# n workers X n tread shoudl be equal to 4


workers = multiprocessing.cpu_count() * 2 + 1
# Calculate the number of threads such that the total number of workers x threads is at least 4
# Ensure at least 1 thread is used
threads = max(1, (4 // workers) + (1 if 4 % workers != 0 else 0))

# for development
# workers = 1
# threads = 1

timeout = 120
bind = "0.0.0.0:8000"
accesslog = "-"
errorlog = "-"
loglevel = "info"
