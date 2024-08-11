package com.cecd.dp.domain.api.report.dto;

import lombok.Builder;

@Builder
public record ReportTagDto(
        String name // 해시태그 이름
)
{
}
