package com.cecd.dp.domain.api.report.dto.response;

import lombok.Builder;

import java.util.List;

@Builder
public record ReportResponseDto (
    ReportProfileResponseDto profile, //✅
    ReportMediaResponseDto mediaList, //✅
    ReportTagResponseDto tagList, //✅ For word-cloud
    List<String> highResponseTag, // 반응 높은 해시태그 3개
    Integer likeAvg,
    Integer replyAvg,
    Float mediaUploadCycle,
    SummaryResponseDto summary
    /* + For 팔로워 추이 그래프 데이터*/
){
    // TODO: Think.. 여기서 해당 DTO 반환 로직 다 가져갈까?

}

