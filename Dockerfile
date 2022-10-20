FROM python:3.9.5

# set up location of code
WORKDIR /code

# RUN echo $PYTHONPATH
# RUN echo ${POSTGRES_USER}

# install cron
RUN apt-get update && apt-get install cron -y

# install python requirements
ADD ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy repo
COPY ./ /code/

# Copy schedule.crontab file to the cron.d directory
COPY ./schedule.cron /etc/cron.d/schedule.cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/schedule.cron

# Apply cron job
RUN crontab /etc/cron.d/schedule.cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run cron
CMD cron && tail -f /var/log/cron.log