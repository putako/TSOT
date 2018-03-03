#uses ubuntu image
FROM ubuntu:16.04

#RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && \
#    apt-get install --no-install-recommends -y \
#    openssh-server \
#    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# found this from a nice tutorial
RUN apt-get update && apt-get install -y openssh-server
RUN apt-get install -y iputils-ping
RUN apt-get install -y nmap
RUN apt-get install -y net-tools
RUN mkdir /var/run/sshd
RUN echo 'root:toor' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config


# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22


# By default, just run `ssh -D`
CMD ["/usr/sbin/sshd", "-D"]
