FROM relaysh/core:latest-python
COPY "./handler.py" "/trigger-bitbucket-event-fired.py"
ENTRYPOINT []
CMD ["python3", "/trigger-bitbucket-event-fired.py"]

LABEL "org.opencontainers.image.title"="Bitbucket event fired"
LABEL "org.opencontainers.image.description"="This trigger takes in the contents of a Bitbucket event and presents it as an output event"
LABEL "sh.relay.sdk.version"="v1"
