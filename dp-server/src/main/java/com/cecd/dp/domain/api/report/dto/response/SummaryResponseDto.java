package com.cecd.dp.domain.api.report.dto.response;

public record SummaryResponseDto (
    String type, // 게시글 타입
    Integer count // 해당 게시글 개수
)
{

}
