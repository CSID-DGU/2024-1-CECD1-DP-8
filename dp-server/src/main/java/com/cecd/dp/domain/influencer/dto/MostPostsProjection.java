package com.cecd.dp.domain.influencer.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class MostPostsProjection {

  private String permaLink; //
  private Integer likeCnt;
  private Integer commentsCnt;

  public MostPostsProjection(String permaLink, Integer likeCnt, Integer commentsCnt) {
    this.permaLink = permaLink + "media?size=l";
    this.likeCnt = likeCnt;
    this.commentsCnt = commentsCnt;
  }
}
