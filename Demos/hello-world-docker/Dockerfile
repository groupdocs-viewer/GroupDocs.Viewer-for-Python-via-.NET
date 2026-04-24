# docker build -f Dockerfile -t groupdocs-viewer-for-python-via-net:hello-world-docker .
# docker run --rm -v "${PWD}/output:/output" groupdocs-viewer-for-python-via-net:hello-world-docker

# Python 3.11 slim (Debian bookworm) — matches the manylinux wheel's runtime
FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

# System.Drawing.Common dependency (libgdiplus), fontconfig, and Microsoft
# TrueType fonts. The ttf-mscorefonts-installer package lives in the
# Debian 'contrib' component, so enable it before installing.
RUN sed -i 's/deb \(.*\) main$/deb \1 main contrib/g' /etc/apt/sources.list 2>/dev/null || \
    sed -i 's/Components: main/Components: main contrib/g' /etc/apt/sources.list.d/*.sources 2>/dev/null || true && \
    apt-get update && \
    echo "ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true" | debconf-set-selections && \
    apt-get install -y --no-install-recommends \
        libgdiplus \
        libfontconfig1 \
        libicu-dev \
        ttf-mscorefonts-installer \
        fontconfig && \
    fc-cache -f && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install the pinned groupdocs-viewer-net version
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt

# Copy the sample document and rendering script
COPY . .

# Render sample.docx to output/page_{1,2,...}.html on container start
CMD ["python3", "render_docx_to_html.py"]
