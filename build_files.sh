apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
        build-essential \
        libssl-dev \
        libffi-dev \
        python3-dev \
        build-essential \
        libjpeg-dev \
        zlib1g-dev \
        gcc \
        libpq-dev \
        libc-dev \
        bash \
        git \
    && pip3 install --upgrade pip

pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput
