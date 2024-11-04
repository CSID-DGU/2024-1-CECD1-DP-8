package com.cecd.dp.global.common.code;

import lombok.Builder;
import lombok.Getter;
import org.springframework.http.HttpStatus;

@Builder
@Getter
public class ReasonDTO {
  private HttpStatus httpStatus;
  private boolean isSuccess;
  private String code;
  private String message;
}
