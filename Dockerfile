# Use the official ESP-IDF image
FROM espressif/idf:v5.2.2

# Set ESP-IDF path
ENV IDF_PATH="/opt/esp/idf/"

WORKDIR "/"

# Create directory for files
RUN mkdir -p /fs_build

# Clone and build mklittlefs
RUN git clone https://github.com/earlephilhower/mklittlefs.git && \
    cd mklittlefs && \
    git submodule update --init && \
    make dist

# Copy the main.py to the build directory
COPY src/main.py /fs_build/main.py

# Generate the filesystem binary
RUN cd mklittlefs && \
    ./mklittlefs -c /fs_build -b 4096 -p 256 -s 0x200000 /fs.bin && \
    echo "Filesystem binary created successfully" && \
    ls -la /fs.bin

CMD ["/bin/bash"]