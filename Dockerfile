FROM python:3.13-slim

# System dependencies for the .NET runtime and cross-platform rendering:
#  - libicu-dev: .NET globalization (ICU)
#  - libgdiplus + libfontconfig1 + fontconfig: GDI+/font support used by
#    several rendering paths (PDF, presentations, Visio, CAD, eBooks)
#  - fonts-dejavu + fonts-liberation: real fonts so text renders; the
#    Liberation set is metric-compatible with Arial/Times/Courier.
# Without fonts, font-dependent rendering throws (e.g. "trueTypeFont" null
# or a font type-initializer exception).
RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends \
        libicu-dev libgdiplus libfontconfig1 fontconfig \
        fonts-dejavu fonts-liberation \
    && fc-cache -f \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install the package
COPY Examples/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy examples and sample files
COPY Examples/ ./Examples/

# Run all examples
CMD ["python", "Examples/run_all_examples.py"]
