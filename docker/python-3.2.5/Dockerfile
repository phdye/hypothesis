FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y build-essential wget libssl-dev zlib1g-dev \
    libncurses5-dev libreadline-dev libsqlite3-dev libgdbm-dev \
    libbz2-dev libexpat1-dev liblzma-dev tk-dev uuid-dev && \
    rm -rf /var/lib/apt/lists/*

RUN wget https://www.python.org/ftp/python/3.2.5/Python-3.2.5.tgz && \
    tar -xzf Python-3.2.5.tgz && \
    cd Python-3.2.5 && \
    ./configure --prefix=/opt/python-3.2.5 --enable-shared && \
    make -j$(nproc) && \
    make install && \
    cd .. && \
    rm -rf Python-3.2.5 Python-3.2.5.tgz

ENV PATH="/opt/python-3.2.5/bin:$PATH"

CMD ["python3.2", "--version"]
