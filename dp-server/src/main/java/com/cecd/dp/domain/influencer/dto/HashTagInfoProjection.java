package com.cecd.dp.domain.influencer.dto;

public interface HashTagInfoProjection {
  Integer getUsageCount();

  Integer getMaxEngagement();

  Integer getAvgEngagement();

  Integer getTotalEngagement();

  String getHashTagName();
}
