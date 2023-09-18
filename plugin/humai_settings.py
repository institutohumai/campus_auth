from tutormfe.hooks import MFE_APPS
from tutor import hooks

@MFE_APPS.add()
def _add_my_mfe(mfes):

    mfes["authn"] = {
        "repository": "https://github.com/institutohumai/campus_auth",
        "port": 2001,
        "version": "humai_stable_v1.0"
    }
    print('Custom plugin')
    return mfes

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