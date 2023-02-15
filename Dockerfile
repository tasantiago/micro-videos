FROM python:3.10.10-slim

RUN apt update && apt install -y --no-install-recommends \
                    default-jre \
                    git \
                    zsh \
                    curl \
                    wget \
                    fonts-powerline

RUN useradd -ms /bin/bash python

USER python

WORKDIR /home/python/app

ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

# Default powerline10k theme, no plugins installed
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.5/zsh-in-docker.sh)" \
    -t https://github.com/romkatv/powerlevel10k \
    -p git \
    -p gitflow \
    -p https://github.com/zdharma/fast-syntax-highlighting \
    -p https://github.com/zsh-users/zsh-autosuggestions \
    -p https://github.com/zsh-users/zsh-completions \
    -a 'export TERM=xterm-256color'

RUN echo '[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh' >> ~/.zshrc

CMD ["tail", "-f", "/dev/null"]