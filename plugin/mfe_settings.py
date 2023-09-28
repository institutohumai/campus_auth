from tutormfe.hooks import MFE_APPS

@MFE_APPS.add()
def _add_my_mfe(mfes):

    mfes["authn"] = {
        "repository": "https://github.com/institutohumai/campus_auth",
        "port": 2001,
        "version": "humai_stable_v1.1"
    }
    print('Custom plugin')
    return mfes