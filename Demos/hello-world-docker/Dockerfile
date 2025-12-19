# docker build -f Dockerfile -t groupdocs-viewer-for-python-via-net:hello-world-docker .
# docker run --rm -v "${PWD}/output:/output" groupdocs-viewer-for-python-via-net:hello-world-docker

# Use slim base image which is smaller than the default image
FROM python:3.11-slim

# Microsoft Fonts
ENV DEBIAN_FRONTEND=noninteractive
RUN sed -i 's/deb \(.*\) main$/deb \1 main contrib/g' /etc/apt/sources.list 2>/dev/null || \
    sed -i 's/Components: main/Components: main contrib/g' /etc/apt/sources.list.d/*.sources 2>/dev/null || true && \
    apt-get update && \
    echo "ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true" | debconf-set-selections && \
    apt-get install -y --no-install-recommends \
        wget \
        cabextract \
        xfonts-utils \
        ttf-mscorefonts-installer && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# System.Drawing.Common dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgdiplus libc6-dev

# Globalization and cryptography dependencies
ENV SNAPSHOT_DATE=20220328T000000Z
RUN echo "deb [trusted=yes] http://snapshot.debian.org/archive/debian/${SNAPSHOT_DATE} bullseye main" \
        > /etc/apt/sources.list.d/debian-archive.list && \
    apt-get -o Acquire::Check-Valid-Until=false update && \
    apt-get install -y --no-install-recommends \
        libicu67 \
        libssl1.1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy and install test requirements
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt

# Copy test and out folders
COPY . .

# Run the app
CMD ["python3", "render_docx_to_html.py"]
