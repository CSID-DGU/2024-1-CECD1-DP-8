package com.cecd.dp.domain.influencer.dto;

import java.time.LocalDateTime;


public interface FollowerChartProjection {
    Integer followerCnt();
    LocalDateTime createdAt();
}
