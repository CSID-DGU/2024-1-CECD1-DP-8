package com.cecd.dp.domain;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
@Tag(name = "Test API", description = "Swagger Test용 API")
public class TestContoller {

  @Operation(summary = "테스트API", description = "안녕 이라는 문자열 html을 반환")
  @GetMapping("/test")
  public String test() {
    return "hello";
  }
}
