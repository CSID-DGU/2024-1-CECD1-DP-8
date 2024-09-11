package com.cecd.dp.global.common.exception.handler;

import com.cecd.dp.global.common.code.BaseErrorCode;
import com.cecd.dp.global.common.exception.GeneralException;

public class MediaHandler extends GeneralException {
    public MediaHandler(BaseErrorCode code) {
        super(code);
    }
}
