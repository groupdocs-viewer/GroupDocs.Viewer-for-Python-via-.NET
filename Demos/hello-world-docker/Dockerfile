# docker build -f Dockerfile -t groupdocs-viewer-for-python-via-net:hello-world-docker .
# docker run --rm -v "${PWD}/output:/output" groupdocs-viewer-for-python-via-net:hello-world-docker

# Python 3.13 slim (Debian bookworm). The manylinux wheel is py3-none, so it
# runs on any CPython 3.x; this base image matches the repo's Examples/ Dockerfile.
FROM python:3.13-slim

ENV DEBIAN_FRONTEND=noninteractive

# System dependencies for the .NET runtime and cross-platform rendering —
# the Examples/ Dockerfile at the repo root minus the Microsoft core fonts:
#  - libicu-dev: .NET globalization (ICU)
#  - libfontconfig1 + fontconfig: font discovery (no libgdiplus: since 26.9
#    no rendering path needs it)
#  - fonts-dejavu + fonts-liberation: real fonts so text renders; the
#    Liberation set is metric-compatible with Arial/Times/Courier (no EULA,
#    no contrib component, no SourceForge download — reliable builds).
# This demo renders a DOCX, which Liberation covers. The repo-root image also
# installs ttf-mscorefonts-installer because MS Project files need it.
RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends \
        libicu-dev libfontconfig1 fontconfig \
        fonts-dejavu fonts-liberation \
    && fc-cache -f \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install the pinned groupdocs-viewer-net version
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt

# Copy the sample document and rendering script
COPY . .

# Render sample.docx to output/page_{1,2,...}.html on container start
CMD ["python3", "render_docx_to_html.py"]
