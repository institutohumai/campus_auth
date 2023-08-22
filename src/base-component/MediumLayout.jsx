import React from 'react';

import { getConfig } from '@edx/frontend-platform';
import { useIntl } from '@edx/frontend-platform/i18n';
import { Hyperlink, Image } from '@edx/paragon';
import classNames from 'classnames';

import messages from './messages';

const MediumLayout = () => {
  const { formatMessage } = useIntl();

  return (
    <>
      {/* <div className="w-100 medium-screen-top-stripe" /> */}
      <div className="w-100 p-0 mb-3 d-flex">
        <div className="col-md-10">
          <Hyperlink destination={getConfig().MARKETING_SITE_BASE_URL}>
            <Image alt={getConfig().SITE_NAME} className="logo" src={getConfig().LOGO_WHITE_URL} />
          </Hyperlink>
          <div className="d-flex align-items-center justify-content-center mb-4 w-100">
            <div className={classNames({ 'mt-1 medium-yellow-line': getConfig().SITE_NAME === 'edX' })} />
            <div>
              <h1
                className={classNames(
                  'display-2 text-white mt-5 mb-5 mr-2',
                  { 'ml-4.5': getConfig().SITE_NAME !== 'edX' },
                )}
              >
                {/* <span className="mr-2">{formatMessage(messages['start.learning'])}</span> */}
                <span className="text-login-info">Aprendé sobre Inteligencia Artificial</span> 
                <span className="text-accent-orange">
                  {formatMessage(messages['with.site.name'], { siteName: getConfig().SITE_NAME })}
                </span>
              </h1>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default MediumLayout;
