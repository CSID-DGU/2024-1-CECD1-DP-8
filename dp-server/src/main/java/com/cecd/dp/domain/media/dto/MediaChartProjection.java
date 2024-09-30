package com.cecd.dp.domain.media.dto;

import lombok.Getter;
import lombok.Setter;

import java.util.Date;


public interface MediaChartProjection {
    Integer getTotalCnt();
    Date getPostedAt();
}
