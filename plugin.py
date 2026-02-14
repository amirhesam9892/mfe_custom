from tutor import hooks

hooks.Filters.ENV_PATCHES.add_items(
    [
        (
            "mfe-dockerfile-post-install",
            """
# Create directories
RUN mkdir -p /openedx/app/public/fonts
RUN mkdir -p /openedx/app/public/assets

# Copy fonts
COPY ./plugins/mfe_custom/Vazirmatn-Regular.woff2 /openedx/app/public/fonts/
COPY ./plugins/mfe_custom/Vazirmatn-Bold.woff2 /openedx/app/public/fonts/

# Copy logo
COPY ./plugins/mfe_custom/logo.png /openedx/app/public/assets/logo.png

# Copy SCSS
COPY ./plugins/mfe_custom/mfe_custom.scss /openedx/app/src/mfe_custom.scss

# Override Footer
COPY ./plugins/mfe_custom/footer_override.js /openedx/app/src/components/Footer/index.jsx
"""
        ),
    ]
)
