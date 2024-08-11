package com.cecd.dp.domain.api.report.dto;

import com.cecd.dp.domain.media.entity.Media;
import lombok.Builder;
import lombok.NoArgsConstructor;

/*@NoArgsConstructor*/
@Builder
public record ReportMediaDto(
    Long mediaId,
    String imageURL,
    Integer likeCnt,
    Integer replyCnt
) {
}