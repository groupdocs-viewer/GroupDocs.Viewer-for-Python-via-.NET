FROM python:3.13-slim

# System dependencies for the .NET runtime and cross-platform rendering:
#  - libicu-dev: .NET globalization (ICU)
#  - libfontconfig1 + fontconfig: font discovery
#  - fonts-dejavu + fonts-liberation: real fonts so text renders; the
#    Liberation set is metric-compatible with Arial/Times/Courier.
#  - ttf-mscorefonts-installer: the actual Microsoft core fonts (Arial etc.).
#    Required since 26.9 renders MS Project files on Linux: without them every
#    render_project_* example fails with "Cannot find fallback font 'Generic
#    Sans Serif'" -- Liberation does not satisfy that lookup. It lives in
#    Debian "contrib" (not enabled on the slim base image), so that component
#    is enabled first; the debconf line pre-accepts its EULA and wget is needed
#    for its font download.
# Without fonts, font-dependent rendering throws (e.g. "trueTypeFont" null
# or a font type-initializer exception).
#
# libgdiplus is deliberately NOT installed: since 26.9 no rendering path needs
# it -- every example passes in a container that has neither libgdiplus nor
# cairo/pango/harfbuzz.
RUN set -eux; \
    if [ -f /etc/apt/sources.list.d/debian.sources ]; then \
        sed -i 's/^Components: main$/Components: main contrib/' /etc/apt/sources.list.d/debian.sources; \
    else \
        sed -i 's/ main$/ main contrib/' /etc/apt/sources.list; \
    fi; \
    apt-get update -qq; \
    echo "ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true" | debconf-set-selections; \
    apt-get install -y --no-install-recommends \
        libicu-dev libfontconfig1 fontconfig \
        fonts-dejavu fonts-liberation wget ttf-mscorefonts-installer; \
    fc-cache -f; \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install the package
COPY Examples/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy examples and sample files
COPY Examples/ ./Examples/

# Run all examples
CMD ["python", "Examples/run_all_examples.py"]
