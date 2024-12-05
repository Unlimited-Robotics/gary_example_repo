ARG REGISTRY_ENDPOINT
FROM ${REGISTRY_ENDPOINT}/raya.core.base_images.ros_humble:jetsonorin.4.9.beta

RUN echo "===================================================================="
RUN echo "         Hello from example component initialization!"
RUN echo "===================================================================="