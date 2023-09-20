from tutor import hooks

hooks.Filters.ENV_PATCHES.add_items(
    [
        (
            "mfe-lms-development-settings",
            '''
MFE_CONFIG["LOGO_TRADEMARK_URL"] = "https://raw.githubusercontent.com/institutohumai/campus_auth/my_palm/src/sass/logo_dark.svg"
MFE_CONFIG["LOGO_URL"] = "https://raw.githubusercontent.com/institutohumai/campus_auth/my_palm/src/sass/logo_dark.svg"
'''
        ),
        (
            "mfe-lms-production-settings",
            '''
MFE_CONFIG["LOGO_TRADEMARK_URL"] = "https://raw.githubusercontent.com/institutohumai/campus_auth/my_palm/src/sass/logo_dark.svg"
MFE_CONFIG["LOGO_URL"] = "https://raw.githubusercontent.com/institutohumai/campus_auth/my_palm/src/sass/logo_dark.svg"
'''

        ),
        (
            "lms-env-features",
        """
"ENABLE_BULK_ENROLLMENT_VIEW": true
"""
        )
    ]
)