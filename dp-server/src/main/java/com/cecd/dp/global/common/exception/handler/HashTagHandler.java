package com.cecd.dp.global.common.exception.handler;

import com.cecd.dp.global.common.code.BaseErrorCode;
import com.cecd.dp.global.common.exception.GeneralException;

public class HashTagHandler extends GeneralException {
    public HashTagHandler(BaseErrorCode code) {
        super(code);
    }
}
