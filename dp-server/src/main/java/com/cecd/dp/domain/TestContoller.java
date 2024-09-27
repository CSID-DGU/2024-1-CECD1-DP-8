package com.cecd.dp.domain;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class TestContoller {

  @GetMapping("/test")
  public String test() {
    return "hello";
  }
}
