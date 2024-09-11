package com.cecd.dp.global.common.code.status;

import com.cecd.dp.global.common.code.BaseErrorCode;
import com.cecd.dp.global.common.code.ErrorReasonDTO;
import lombok.AllArgsConstructor;
import lombok.Getter;
import org.springframework.http.HttpStatus;

@AllArgsConstructor
@Getter
public enum ErrorStatus implements BaseErrorCode {

    // 기본 에러
    _INTERNAL_SERVER_ERROR(HttpStatus.INTERNAL_SERVER_ERROR, "COMMON500", "서버 에러, 관리자에게 문의 바랍니다."),
    _BAD_REQUEST(HttpStatus.BAD_REQUEST, "COMMON400", "잘못된 요청입니다."),
    _UNAUTHORIZED(HttpStatus.UNAUTHORIZED, "COMMON401", "인증이 필요합니다."),
    _FORBIDEN(HttpStatus.FORBIDDEN, "COMMON403", "금지된 요청입니다."),

    // User 에러
    _NOT_FOUND_USER(HttpStatus.NOT_FOUND, "USER400", "사용자가 존재하지 않습니다."),

    // Media 관련 에러
    _NOT_FOUND_MEDIA(HttpStatus.NOT_FOUND, "MEDIA400", "미디어가 존재하지 않습니다.(관리자에게 문의 바랍니다.)"),

    // Tag 관련 에러
    _NOT_FOUND_TAG(HttpStatus.NOT_FOUND, "TAG400", "해시 태그가 존재하지 않습니다.");

    private final HttpStatus httpStatus;
    private final String code;
    private final String message;

    @Override
    public ErrorReasonDTO getReason() {
        return ErrorReasonDTO.builder()
                .message(message)
                .code(code)
                .isSuccess(false)
                .build();
    }

    @Override
    public ErrorReasonDTO getReasonHttpStatus() {
        return ErrorReasonDTO.builder()
                .message(message)
                .code(code)
                .isSuccess(false)
                .httpStatus(httpStatus)
                .build();
    }
}
