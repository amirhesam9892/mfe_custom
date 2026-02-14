from tutor import hooks

hooks.Filters.ENV_PATCHES.add_items([
    # Override logos and favicon
    (
        "mfe-lms-development-settings",
        """
MFE_CONFIG["LOGO_URL"] = "/assets/logo.png"
MFE_CONFIG["FAVICON_URL"] = "/assets/logo.png"
"""
    ),
    (
        "mfe-lms-production-settings",
        """
MFE_CONFIG["LOGO_URL"] = "/assets/logo.png"
MFE_CONFIG["FAVICON_URL"] = "/assets/logo.png"
"""
    ),
])

# Frontend Plugin Slot برای Footer
hooks.Filters.MFE_FRONTEND_PLUGIN_SLOTS.add_items([
    (
        "all",
        "footer_slot",
        """
{
    op: PLUGIN_OPERATIONS.Hide,
    widgetId: 'default_contents',
}
"""
    ),
    (
        "all",
        "footer_slot",
        """
{
    op: PLUGIN_OPERATIONS.Insert,
    widget: {
        id: 'custom_footer',
        type: DIRECT_PLUGIN,
        RenderWidget: () => (
            <footer className='custom-footer'>
                <div style={{textAlign: 'center', padding: '20px'}}>
                    <img src='/assets/logo.png' alt='University Logo' height='60'/>
                    <div style={{marginTop: '10px'}}>
                        <a href='/about'>درباره ما</a> | 
                        <a href='/contact'>تماس با ما</a> | 
                        <a href='/privacy'>حریم خصوصی</a> | 
                        <a href='/terms'>قوانین استفاده</a>
                    </div>
                    <div style={{marginTop: '10px'}}>
                        © 2026 سامانه آموزش الکترونیکی
                    </div>
                </div>
            </footer>
        ),
    },
}
"""
    )
])
