package com.cecd.dp.global.common.code;

import lombok.Builder;
import lombok.Getter;
import org.springframework.http.HttpStatus;

@Builder
@Getter
public class ErrorReasonDTO {
  private HttpStatus httpStatus;
  private String code;
  private String message;
  private boolean isSuccess;
}
