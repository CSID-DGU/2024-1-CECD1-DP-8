package com.cecd.dp.domain.influencer.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class MostPostsProjection {

  private String uniqueCode;

  public MostPostsProjection(String uniqueCode) {
    this.uniqueCode = uniqueCode;
  }
}
